from typing import Union
from fastapi import FastAPI, HTTPException
from fastapi.responses import PlainTextResponse
import requests
import os

session = requests.Session()
COOKIES = {'session':os.getenv('AOC_COOKIE')}
LEADERBOARD_ID = os.getenv('AOC_LEADERBOARD_ID')


app = FastAPI()

def format_slack(members):
    """Returns leaderboard list formatted for a slack slash command"""
    members = sorted(members, key = lambda x: int(x.get('local_score',0)),reverse=True)
    for member in members:
        info = f"[{member.get('local_score',0)}] {member.get('name','Anonymous') if member.get('name') is not None else 'Anonymous' } "
        yield info

@app.post("/apps/aoc-leaderboard",response_class=PlainTextResponse)
def read_item(f: Union[str, None] = None):
    """Endpoint to request leaderboard"""
    if f != 'slack':
        raise HTTPException(status_code=404, detail="Item not found")
    response = requests.get(F"https://adventofcode.com/2023/leaderboard/private/view/{LEADERBOARD_ID}.json",cookies=COOKIES,timeout=60)
    data = response.json()['members']
    members = [details for _,details in data.items()]
    output = "\n".join(list(format_slack(members)))
    return output
