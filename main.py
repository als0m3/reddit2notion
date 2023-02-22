import os
import dotenv
import sqlite3
import hashlib
import time
from termcolor import colored

dotenv.load_dotenv()


from src.notion import Notion
from src.reddit import *
from src.setup import checkSetup
from src.storage import *


def config():
    db = sqlite3.connect("config.sqlite3")

    return {
        "NOTION": {
            "key": db.execute(
                "SELECT * FROM config WHERE key = 'NOTION_KEY'"
            ).fetchone()[1],
            "database_id": db.execute(
                "SELECT * FROM config WHERE key = 'NOTION_DATABASE_ID'"
            ).fetchone()[1],
        },
        "REDDIT": {
            "username": db.execute(
                "SELECT * FROM config WHERE key = 'REDDIT_USERNAME'"
            ).fetchone()[1],
            "feed": db.execute(
                "SELECT * FROM config WHERE key = 'REDDIT_FEED_ID'"
            ).fetchone()[1],
        },
    }


def main():
    checkSetup()

    config_ = config()

    notion_ = Notion()
    notion_.setKey(config_["NOTION"]["key"])
    notion_.setGalleryID(config_["NOTION"]["database_id"])

    reddit_ = Reddit()
    reddit_.setFeedID(config_["REDDIT"]["feed"])
    reddit_.setUsername(config_["REDDIT"]["username"])

    print("Checking for new articles...")
    while True:
        for article in reddit_.query_all_saved_content():
            hash = hashlib.sha256(article["url"].encode("utf-8")).hexdigest()

            if is_news_already_stored(hash):
                continue
            else:

                print("New article found!", end="")
                print(
                    colored(
                        f"""
┌--
|  -> From: {article["source"]}
|  -> Title: {article["title"]}
└--                           """,
                        "green",
                    ),
                )

                store_news(
                    {
                        "hash": hash,
                        "date": datetime.datetime.now(),
                        "title": article["title"],
                        "content": article["content"],
                        "url": article["url"],
                        "source": article["source"],
                    }
                )
                notion_.createGalleryItem(article)
        time.sleep(60)


if __name__ == "__main__":

    print(
        colored(
            """

██████╗ ███████╗██████╗ ██████╗ ██╗████████╗    ██████╗     ███╗   ██╗ ██████╗ ████████╗██╗ ██████╗ ███╗   ██╗
██╔══██╗██╔════╝██╔══██╗██╔══██╗██║╚══██╔══╝    ╚════██╗    ████╗  ██║██╔═══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║
██████╔╝█████╗  ██║  ██║██║  ██║██║   ██║        █████╔╝    ██╔██╗ ██║██║   ██║   ██║   ██║██║   ██║██╔██╗ ██║
██╔══██╗██╔══╝  ██║  ██║██║  ██║██║   ██║       ██╔═══╝     ██║╚██╗██║██║   ██║   ██║   ██║██║   ██║██║╚██╗██║
██║  ██║███████╗██████╔╝██████╔╝██║   ██║       ███████╗    ██║ ╚████║╚██████╔╝   ██║   ██║╚██████╔╝██║ ╚████║
╚═╝  ╚═╝╚══════╝╚═════╝ ╚═════╝ ╚═╝   ╚═╝       ╚══════╝    ╚═╝  ╚═══╝ ╚═════╝    ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
 ██████╗  █████╗ ██╗     ██╗     ███████╗██████╗ ██╗   ██╗
██╔════╝ ██╔══██╗██║     ██║     ██╔════╝██╔══██╗╚██╗ ██╔╝
██║  ███╗███████║██║     ██║     █████╗  ██████╔╝ ╚████╔╝ 
██║   ██║██╔══██║██║     ██║     ██╔══╝  ██╔══██╗  ╚██╔╝  
╚██████╔╝██║  ██║███████╗███████╗███████╗██║  ██║   ██║   
 ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝   ╚═╝   
    """,
            "red",
        )
    )

    print(colored("Notion Reddit Gallery", "green"))
    print(colored("Author : @ALS0M3", "green"))

    main()
