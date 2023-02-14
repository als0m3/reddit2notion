import requests
import configparser
from bs4 import BeautifulSoup

from src.notion import createNewsBlock

config = configparser.ConfigParser()
config.read("config.ini")

HEADERS = {
    "User-Agent": "My User Agent 1.0",
}


def query_all_saved_content():
    article_list = []
    try:
        r = requests.get(
            f'{config["REDDIT"]["url"]}?feed={config["REDDIT"]["feed"]}&user={config["REDDIT"]["username"]}',
            headers=HEADERS,
        )
        soup = BeautifulSoup(r.content, features="xml")

        articles = soup.findAll("entry")
        for a in articles:
            title = a.find("title").text
            link = a.find("link").get("href")
            article = {"title": title, "url": link}
            article_list.append(article)

        return article_list
    except Exception as e:
        print("The scraping job failed. See exception: ")
        print(e)


if __name__ == "__main__":
    for article in query_all_saved_content():
        createNewsBlock(article)

