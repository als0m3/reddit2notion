import requests
import sys


class Linkedin:
    def __init__(self, li_at):
        self.__li_at = li_at

        self.__cookies = {
            "li_at": self.__li_at,
            "JSESSIONID": '"csrf:linkedin"',
        }

        self.__headers = {
            "Cookie": ";".join(
                [key + "=" + value for key, value in self.__cookies.items()]
            ),
            "csrf-token": "csrf:linkedin",
        }

        self.__host = "https://www.linkedin.com"

        self.__url_params = {
            "q": "all",
            "query": "(flagshipSearchIntent:SEARCH_MY_ITEMS_SAVED_POSTS)",
            "start": "0",
            "count": "100",
        }

        self.__url = "/voyager/api/search/dash/clusters?" + "&".join(
            [key + "=" + value for key, value in self.__url_params.items()]
        )

    def query_all_saved_content(self):
        try:
            response = requests.get(self.__host + self.__url, headers=self.__headers)
        except requests.exceptions.RequestException as e:
            print(e)
            sys.exit(1)

        articles_list = []

        # print(response.json()["elements"][0]["items"][0]["itemUnion"]["entityResult"])

        for article in response.json()["elements"][0]["items"]:
            article = article["itemUnion"]["entityResult"]

            print(article)
            print(type(article))

            try:
                icon = (
                    requests.get(
                        "https://unsplash.com/napi/search?query=TECH "
                        + article["primarySubtitle"]["text"]
                        + "&page=1&per_page=1",
                        headers={"User-Agent": "Reddit2Notion/0.1"},
                    )
                    .json()
                    .get("photos")
                    .get("results")[0]
                    .get("urls")
                    .get("small")
                )

            except Exception as e:
                print(
                    "Could not get icon for "
                    # + article["primarySubtitle"]["text"]
                    + ". See exception: {e}"
                )
                icon = None

            articles_list.append(
                {
                    "title": (
                        article["summary"]["text"][:68] + " ..."
                        if "summary" in article
                        else ""
                    ),
                    "category": "...",
                    "source": "LINKEDIN",
                    "content": (
                        article["summary"]["text"] if "summary" in article else ""
                    ),
                    "url": "https://www.linkedin.com/feed/update/"
                    + article["trackingUrn"],
                    "icon": icon,
                }
            )

        # print(articles_list)
        return articles_list
