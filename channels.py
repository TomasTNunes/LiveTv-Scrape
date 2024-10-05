channels = {
            'Sport TV 1': {'url':'https://www.pirilampo.tv/live-tv/sport-tv-1.html', 
                           'm3u8_url_init':'https://love2live.wideiptv.top/SPT1/index.fmp4.m3u8?token=', 
                           'replace_identifier':'[Sport TV 1 - m3u8 url]'},
            
            'Sport TV 2': {'url':'https://www.pirilampo.tv/live-tv/sport-tv-2.html', 
                           'm3u8_url_init':'https://love2live.wideiptv.top/SPT2/index.fmp4.m3u8?token=', 
                           'replace_identifier':'[Sport TV 2 - m3u8 url]'},

            'Sport TV 3': {'url':'https://www.pirilampo.tv/live-tv/sport-tv-3.html', 
                           'm3u8_url_init':'https://love2live.wideiptv.top/SPT3/index.fmp4.m3u8?token=', 
                           'replace_identifier':'[Sport TV 3 - m3u8 url]'},
            
            'Sport TV 4': {'url':'https://www.pirilampo.tv/live-tv/sport-tv-4.html', 
                           'm3u8_url_init':'https://love2live.wideiptv.top/SPT4/index.fmp4.m3u8?token=', 
                           'replace_identifier':'[Sport TV 4 - m3u8 url]'},
            
            'Sport TV 5': {'url':'https://www.pirilampo.tv/live-tv/sport-tv-5.html', 
                           'm3u8_url_init':'https://love2live.wideiptv.top/SPT5/index.fmp4.m3u8?token=', 
                           'replace_identifier':'[Sport TV 5 - m3u8 url]'},
            
            'Sport TV 6': {'url':'https://www.pirilampo.tv/live-tv/sport-tv-6.html', 
                           'm3u8_url_init':'https://love2live.wideiptv.top/SPT6/index.fmp4.m3u8?token=', 
                           'replace_identifier':'[Sport TV 6 - m3u8 url]'},

            'Sport TV 7': {'url':'https://www.pirilampo.tv/live-tv/sport-tv-7.html', 
                           'm3u8_url_init':'https://love2live.wideiptv.top/SPT7/index.fmp4.m3u8?token=', 
                           'replace_identifier':'[Sport TV 7 - m3u8 url]'},
            
            'DAZN 1': {'url':'https://www.pirilampo.tv/live-tv/dazn-1.html', 
                           'm3u8_url_init':'https://love2live.wideiptv.top/ELEVEN1/index.fmp4.m3u8?token=', 
                           'replace_identifier':'[DAZN 1 - m3u8 url]'},
            
            'DAZN 2': {'url':'https://www.pirilampo.tv/live-tv/dazn-2.html', 
                           'm3u8_url_init':'https://love2live.wideiptv.top/ELEVEN2/index.fmp4.m3u8?token=', 
                           'replace_identifier':'[DAZN 2 - m3u8 url]'},
            
            'DAZN 3': {'url':'https://www.pirilampo.tv/live-tv/dazn-3.html', 
                           'm3u8_url_init':'https://love2live.wideiptv.top/ELEVEN3/index.fmp4.m3u8?token=', 
                           'replace_identifier':'[DAZN 3 - m3u8 url]'},
            
            'DAZN 4': {'url':'https://www.pirilampo.tv/live-tv/dazn-4.html', 
                           'm3u8_url_init':'https://love2live.wideiptv.top/ELEVEN4/index.fmp4.m3u8?token=', 
                           'replace_identifier':'[DAZN 4 - m3u8 url]'},
            
            'DAZN 5': {'url':'https://www.pirilampo.tv/live-tv/dazn-5.html', 
                           'm3u8_url_init':'https://love2live.wideiptv.top/ELEVEN5/index.fmp4.m3u8?token=', 
                           'replace_identifier':'[DAZN 5 - m3u8 url]'},
            
            'DAZN 6': {'url':'https://www.pirilampo.tv/live-tv/dazn-6.html', 
                           'm3u8_url_init':'https://love2live.wideiptv.top/ELEVEN6/index.fmp4.m3u8?token=', 
                           'replace_identifier':'[DAZN 6 - m3u8 url]'},
            
            'BTV': {'url':'https://www.pirilampo.tv/live-tv/benfica-tv.html', 
                           'm3u8_url_init':'https://love2live.wideiptv.top/BTV1/index.fmp4.m3u8?token=', 
                           'replace_identifier':'[BTV - m3u8 url]'},
           }

# for common key values
for n, c in channels.items():
    c['m3u8_url'] = ''