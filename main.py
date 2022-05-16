# main.py

from fastapi import FastAPI
from ytmusicapi import YTMusic

app = FastAPI()
ytmusic = YTMusic('headers_auth.json')

@app.get("/")
async def root():
    myhistory = ytmusic.get_history()
    print(myhistory[0]['title']) #title of most recently played item in history.
    print(myhistory[0]['artists'][0]['name'])
    return {"body": myhistory[0]}