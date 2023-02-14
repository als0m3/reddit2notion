def newsObj(article):
    return {
    "children": [
        {
            "object": "block",
            "type": "callout",
            "callout": {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {"content": article["title"], "link": None},
                        "annotations": {
                            "bold": True,
                            "italic": False,
                            "strikethrough": False,
                            "underline": False,
                            "code": False,
                            "color": "default",
                        },
                        "plain_text": "Hello, world!",
                        "href": None,
                    },
                    {
                        "type": "text",
                        "text": {"content": "\n", "link": None},
                        "annotations": {
                            "bold": False,
                            "italic": False,
                            "strikethrough": False,
                            "underline": False,
                            "code": False,
                            "color": "default",
                        },
                        "plain_text": " - ",
                        "href": None,
                    },
                    {
                        "type": "text",
                        "text": {"content": "link", "link": {"url": article["url"]}},
                        "annotations": {
                            "bold": False,
                            "italic": True,
                            "strikethrough": False,
                            "underline": False,
                            "code": False,
                            "color": "gray",
                        },
                        "plain_text": "link",
                        "href": None,
                    }
                ],
                "icon": {"type": "emoji", "emoji": "🗞️"},
                "color": "orange_background",
            },
        },
    ],
}
