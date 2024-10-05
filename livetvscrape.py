from playwright.sync_api import sync_playwright
from channels import channels
import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Function to create full file paths
def get_full_path(filename):
    return os.path.join(script_dir, filename)

# Scrape first url with token
def get_token_url(page, url):
    # Create a variable to store the first token URL
    token_url = None

    # Define a callback to handle network requests
    def handle_request(request):
        nonlocal token_url  # Access the outer scope variable
        if 'token' in request.url and 'no_check_ip' not in request.url and token_url is None:
            token_url = request.url

    # Listen for all requests
    page.on("request", handle_request)

    # Navigate to the page
    page.goto(url)

    # Wait for some time to allow network requests to be made
    page.wait_for_timeout(2000)  # Adjust time as needed

    return token_url


#---------------------------------- MAIN ----------------------------------#

# Scrape
with sync_playwright() as p:
    for name, channel in channels.items():
        browser = p.chromium.launch()
        try:
            page = browser.new_page()
            token_url = get_token_url(page, channel['url'])
            token = token_url.split("token=")[1]
            channel['m3u8_url'] = channel['m3u8_url_init'] + token
        except Exception as e:
            print(f'Error: {e}\n')
        finally:
            browser.close()

# Read livetv.m3u.template
with open(get_full_path('livetv.m3u.template'), 'r') as f1:
    content = f1.read()

# Write livetv.m3u
for name, channel in channels.items():
    content = content.replace(channel['replace_identifier'], channel['m3u8_url'])

with open(get_full_path('livetv.m3u'), 'w') as file:
    file.write(content)