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

                subreddit = a.find("category").get("term")

                try:
                    subreddit_title = (
                        requests.get(
                            f"https://www.reddit.com/r/{subreddit}/about.json",
                            headers={"User-Agent": "Reddit2Notion/0.1"},
                        )
                        .json()
                        .get("data")
                        .get("title")
                    )
                except Exception as e:
                    print(f"Could not get icon for {subreddit}. See exception: {e}")
                    subreddit_title = None

                try:
                    icon = (
                        requests.get(
                            f"https://unsplash.com/napi/search?query=TECH {subreddit_title}&page=1&per_page=1",
                            headers={"User-Agent": "Reddit2Notion/0.1"},
                        )
                        .json()
                        .get("photos")
                        .get("results")[0]
                        .get("urls")
                        .get("small")
                    )
                except Exception as e:
                    print(f"Could not get icon for {subreddit}. See exception: {e}")
                    icon = None

                article = {
                    "title": a.find("title").text,
                    "category": subreddit_title,
                    "source": "REDDIT",
                    "content": markdownify(
                        a.find("content").get_text(), heading_style="ATX"
                    ),
                    "url": a.find("link").get("href"),
                    "icon": icon,
                }
                article_list.append(article)

            return article_list
        except Exception as e:
            print(f"The scraping job failed. See exception: {e}")
