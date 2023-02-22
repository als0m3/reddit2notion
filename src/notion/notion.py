import requests

from .object_templates.galleryItem import galleryItem


class Notion:
    def __init__(self, database_id, notion_key):
        self.__database_id = database_id
        self.__notion_key = notion_key


    def createGalleryItem(self, data_):
        headers = {
            'Authorization': 'Bearer ' + self.__notion_key,
            'Content-Type': 'application/json',
            'Notion-Version': '2022-02-22',
        }
        try:
            response = requests.post(
                "https://api.notion.com/v1/pages", headers=headers, json=galleryItem(data_, self.__database_id)
            )
            if not response.status_code == 200:
                print(f"Failed to create gallery item. See response: {response.json()}")

        except Exception as e:
            print(f"Failed to create gallery item. See exception: {e}")
