import os
import requests
import json
import dotenv
import configparser

config = configparser.ConfigParser()
config.read("config.ini")
dotenv.load_dotenv()

HEADERS = {
    "Authorization": "Bearer " + os.environ.get("NOTION_KEY"),
    "Content-Type": "application/json",
    "Notion-Version": "2022-02-22",
}


def databaseItem(article):
    return {
        "parent": {
            "database_id": config["NOTION"]["database_id"],
        },
        "icon": {"type": "emoji", "emoji": "🗞️"},
        "cover": {
            "external": {
                "url": "https://images.unsplash.com/photo-1585829365295-ab7cd400c167?ixlib=rb-4.0.3&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=2400",
            },
        },
        "properties": {
            "title": {
                "title": [
                    {
                        "text": {
                            "content": article["title"],
                        },
                    },
                ],
            },
            "Source": {
                "rich_text": [
                    {
                        "text": {
                            "content": article["source"],
                        },
                    },
                ]
            },
            "Title": {
                "rich_text": [
                    {
                        "text": {
                            "content": article["title"],
                        },
                    }
                ],
            },
            "Link": {
                "url": article["url"],
            },
            "Status": {
                "status": {
                    "name": "To read",
                }
            },
        },
        "children": [
            {
                "object": "block",
                "type": "heading_2",
                "heading_2": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": article["title"],
                            },
                        },
                    ],
                },
            },
            {
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": article["content"],
                                "link": {
                                    "url": article["url"],
                                },
                            },
                        },
                    ],
                },
            },
        ],
    }


def createNewDatabaseItem(article):



def main(article):
    article = {
        "title": "Article title",
        "source": "Reddit",
        "content": "Article content",
        "url": "https://www.notion.so/Hello-world-0b1d8f8f2e2e4d0c8f0d8c8c9b9f9f9a",
    }

    response = createNewDatabaseItem(article)
    if response.status_code == 200:
        print("Success")
    else:
        print("Failed")
        print(response.status_code)
        print(response.text)


if __name__ == "__main__":
    main("article")
