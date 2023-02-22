import sqlite3
import datetime

def is_news_already_stored(hash):
    db = sqlite3.connect("db.sqlite3")
    result = db.execute(
        "SELECT * FROM news WHERE hash = ?", (hash,)
    )
    return result .fetchone() is not None

def store_news(news):
    db = sqlite3.connect("db.sqlite3")
    db.execute(
        "INSERT INTO news (hash, date, title, content, url, source) VALUES (?, ?, ?, ?, ?, ?)",
        (news["hash"], news["date"], news["title"], news["content"], news["url"], news["source"])
    )
    db.commit()


