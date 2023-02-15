import requests
import configparser
from bs4 import BeautifulSoup
import markdownify


config = configparser.ConfigParser()
config.read("config.ini")

HEADERS = {
    "User-Agent": "My User Agent 1.0",
}


class Reddit:
    feed_id = ""
    username = ""

    def setFeedID(self, feed_id):
        self.feed_id = feed_id
    
    def setUsername(self, username):
        self.username = username

    def query_all_saved_content(self):
        article_list = []
        try:
            r = requests.get(
                f'{config["REDDIT"]["url"]}?feed={self.feed_id}&user={self.username}',
                headers=HEADERS,
            )
            soup = BeautifulSoup(r.content, features="xml")

            articles = soup.findAll("entry")
            for a in articles:
                article = {
                    "title": a.find("title").text,
                    "source": "Reddit",
                    "content": markdownify.markdownify(
                        a.find("content").get_text(), heading_style="ATX"
                    ),
                    "url": a.find("link").get("href"),
                }
                article_list.append(article)

            return article_list
        except Exception as e:
            print("The scraping job failed. See exception: ")
            print(e)
