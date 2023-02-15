
def galleryItem(article, gallery_id):
    return {
        "parent": {
            "database_id": gallery_id,
        },
        "icon": {"type": "emoji", "emoji": "🗞️"},
        "cover": {
            "external": {
                "url": "https://images.unsplash.com/photo-1585829365295-ab7cd400c167?ixlib=rb-4.0.3&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=2400",
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
