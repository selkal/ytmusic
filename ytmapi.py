from ytmusicapi import YTMusic
ytmusic = YTMusic('headers_auth.json')

myhistory = ytmusic.get_history()
print(myhistory[0]['title']) #title of most recently played item in history.
print(myhistory[0]['artists'][0]['name'])