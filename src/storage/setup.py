import requests
import dotenv
import os
import sqlite3

dotenv.load_dotenv()


def setupConfig():

    with open("config.ini", "w") as f:
        f.write(
            f"""
[NOTION.secrets]
NOTION_DATABASE_ID = {input("Please enter your Notion database ID:")}
NOTION_KEY = {input("Please enter your Notion API key:")}

[REDDIT.secrets]
REDDIT_USERNAME = {input("Please enter your Reddit username:")}
REDDIT_FEED_ID = {input("Please enter your Reddit feed ID:")}

[DEFAULT]
refresh_interval = {input("Please enter the refresh interval (in seconds):")}
"""
        )

    # db = sqlite3.connect("config.sqlite3")
    # db.execute("CREATE TABLE IF NOT EXISTS config (key TEXT, value TEXT)")

    # infos = ["NOTION_KEY", "NOTION_DATABASE_ID", "REDDIT_USERNAME", "REDDIT_FEED_ID"]

    # for info in infos:
    #     print(f"Please enter your {info}: ")
    #     db.execute("INSERT INTO config VALUES (?, ?)", (info, input()))
    #     db.commit()

    print("Config setup complete!")


def setupDatabase():
    db = sqlite3.connect("db.sqlite3")
    db.execute(
        "CREATE TABLE IF NOT EXISTS news (hash TEXT, date TEXT, title TEXT, content TEXT, url TEXT, source TEXT)"
    )
    db.commit()
    print("Database setup complete!")


def checkSetup():
    if not os.path.exists("config.ini"):
        print("No config file found. Would you like to setup the config? (y/n)")
        if input() == "y":
            setupConfig()
        else:
            print("Exiting...")
            exit()

    if not os.path.exists("db.sqlite3"):
        print("No database file found. Would you like to setup the database? (y/n)")
        if input() == "y":
            setupDatabase()
        else:
            print("Exiting...")
            exit()
