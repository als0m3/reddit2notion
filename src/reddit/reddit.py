import requests
from bs4 import BeautifulSoup
from markdownify import markdownify

class Reddit:
    def __init__(self, username, feed_id):
        self.__feed_id = feed_id
        self.__username = username

    def query_all_saved_content(self):
        article_list = []
        try:
            url = f"https://www.reddit.com/saved.rss?feed={self.__feed_id}&user={self.__username}"
            r = requests.get(url, headers={"User-Agent": "Reddit2Notion/0.1"})
            soup = BeautifulSoup(r.content, features="xml")

            for a in soup.findAll("entry"):
                article = {
                    "title": a.find("title").text,
                    "source": "Reddit",
                    "content": markdownify(
                        a.find("content").get_text(), heading_style="ATX"
                    ),
                    "url": a.find("link").get("href"),
                }
                article_list.append(article)

            return article_list
        except Exception as e:
            print(f"The scraping job failed. See exception: {e}")
