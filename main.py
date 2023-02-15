import os
import dotenv
dotenv.load_dotenv()

from src.notion import Notion
from src.reddit import *

def main():
    notion_ = Notion()
    notion_.setKey(os.environ["NOTION_KEY"])
    notion_.setGalleryID(config["NOTION"]["database_id"])

    reddit_ = Reddit()
    reddit_.setFeedID(config["REDDIT"]["feed"])
    reddit_.setUsername(config["REDDIT"]["username"])

    for article in reddit_.query_all_saved_content():
        notion_.createGalleryItem(article)


if __name__ == "__main__":
    main()