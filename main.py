import dotenv
import hashlib
import time
from termcolor import colored

dotenv.load_dotenv()

from configparser import ConfigParser

config_ = ConfigParser()
config_.read("config.ini")

from src.notion import Notion
from src.reddit import *
from src.setup import checkSetup
from src.storage import *

def main():
    checkSetup()

    notion_ = Notion()
    notion_.setKey(config_["NOTION.secrets"]["NOTION_KEY"])
    notion_.setGalleryID(config_["NOTION.secrets"]["NOTION_DATABASE_ID"])

    reddit_ = Reddit()
    reddit_.setFeedID(config_["REDDIT.secrets"]["REDDIT_FEED_ID"])
    reddit_.setUsername(config_["REDDIT.secrets"]["REDDIT_USERNAME"])

    while True:
        print("Checking for new articles...")
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
        time.sleep(int(config_["DEFAULT"]["refresh_interval"]))


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
