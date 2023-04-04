def galleryItem(article, gallery_id):
    return {
        "parent": {
            "database_id": gallery_id,
        },
        "icon": {"type": "emoji", "emoji": "🗞️"},
        "cover": {
            "external": {
                "url": article["icon"],
            },
        },
        "properties": {
            "title": {
                "title": [
                    {
                        "text": {
                            "content": article["title"],
                        },
                    },
                ],
            },
            "Category": {
                "select": {
                    "name": article["category"],
                },
            },
            "Date": {
                "date": {
                    "start": article["date"],
                },
            },
            "Source": {
                "select": {
                    "name": article["source"],
                },
            },
            "Title": {
                "rich_text": [
                    {
                        "text": {
                            "content": article["title"],
                        },
                    }
                ],
            },
            "Link": {
                "url": article["url"],
            },
            "Status": {
                "status": {
                    "name": "To read",
                }
            },
        },
        "children": [
            {
                "object": "block",
                "type": "heading_2",
                "heading_2": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": article["title"],
                            },
                        },
                    ],
                },
            },
            {
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": article["content"],
                                "link": {
                                    "url": article["url"],
                                },
                            },
                        },
                    ],
                },
            },
        ],
    }
