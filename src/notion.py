import requests

from src.object_templates.galleryItem import galleryItem


class Notion:
    parent_id = ""
    database_id = ""
    notion_key = ""

    def setParentID(self, parent_id):
        self.parent_id = parent_id
    
    def setGalleryID(self, database_id):
        self.database_id = database_id

    def setKey(self, notion_key):
        self.notion_key = notion_key

    def createGalleryItem(self, data_):
        headers = {
            'Authorization': 'Bearer ' + self.notion_key,
            'Content-Type': 'application/json',
            'Notion-Version': '2022-02-22',
        }
        return requests.post(
            "https://api.notion.com/v1/pages", headers=headers, json=galleryItem(data_, self.database_id)
        )
    