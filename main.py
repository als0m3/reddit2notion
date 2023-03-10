import dotenv
import hashlib
import time
from configparser import ConfigParser

from src.utils.display import banner, display_new_articles
from src.notion.notion import Notion
from src.reddit.reddit import Reddit
from src.storage.setup import checkSetup
from src.storage.storage import *


dotenv.load_dotenv()
config_ = ConfigParser()
config_.read("config.ini")


def main():
    checkSetup()

    notion_ = Notion(
        config_["NOTION.secrets"]["NOTION_DATABASE_ID"],
        config_["NOTION.secrets"]["NOTION_KEY"],
    )

    reddit_ = Reddit(
        config_["REDDIT.secrets"]["REDDIT_USERNAME"],
        config_["REDDIT.secrets"]["REDDIT_FEED_ID"],
    )

    while True:
        print("Checking for new articles...")
        for article in reddit_.query_all_saved_content():
            hash = hashlib.sha256(article["url"].encode("utf-8")).hexdigest()

            if is_news_already_stored(hash):
                continue
            else:
                display_new_articles(article)
                store_news(
                    {
                        "hash": hash,
                        "date": datetime.datetime.now().isoformat(),
                        "title": article["title"],
                        "content": article["content"],
                        "url": article["url"],
                        "source": article["source"],
                    }
                )
                notion_.createGalleryItem({
                        "hash": hash,
                        "date": datetime.datetime.now().isoformat(),
                        "title": article["title"],
                        "content": article["content"],
                        "url": article["url"],
                        "source": article["source"],
                    })
        time.sleep(int(config_["DEFAULT"]["refresh_interval"]))


if __name__ == "__main__":
    banner()
    main()
