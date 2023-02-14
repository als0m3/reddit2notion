import os
import requests
import json
import dotenv
import configparser

from src.objects import newsObj 

config = configparser.ConfigParser()
config.read('config.ini')
dotenv.load_dotenv()

HEADERS = {
    'Authorization': 'Bearer ' + os.environ.get("NOTION_KEY"),
    'Content-Type': 'application/json',
    'Notion-Version': '2022-02-22',
}

def createNewsBlock(article):
    response = requests.patch(
        f'https://api.notion.com/v1/blocks/{config["NOTION"]["reddit_parent"]}/children',
        headers=HEADERS,
        json=newsObj(article),
    )
    if response.status_code == 200:
        print("Success")
    else:
        print("Failed")
        print(response.status_code)
        print(response.text)