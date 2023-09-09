"""
This module provides a class for interacting with an SQLite database to store
and retrieve activities.
"""

import sqlite3

# For information on how this module works, I recommend visiting:
# https://docs.python.org/3/library/sqlite3.html
# or https://www.sqlite.org/docs.html


class ActivityDB:
    """A class used to represent an SQLite database for storing activities."""

    def __init__(self, db_name="activities.db"):
        """Constructs all necessary attributes for the ActivityDB object."""
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS activities (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                activity TEXT,
                type TEXT,
                participants INTEGEER,
                price REAL,
                link TEXT,
                key TEXT,
                accessibility REAL
            )
        """
        )
        self.conn.commit()

    def save_activity(self, activity):
        """Saves an activity in the database."""
        self.cursor.execute(
            """
            INSERT INTO activities (activity, type, participants, price, link, key, accessibility)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
            (
                activity["activity"],
                activity["type"],
                activity["participants"],
                activity["price"],
                activity["link"],
                activity["key"],
                activity["accessibility"],
            ),
        )
        self.conn.commit()

    def get_latest_activities(self):
        """Retrieves the latest activities from the database."""
        self.cursor.execute("SELECT * FROM activities ORDER BY id DESC LIMIT 5")
        return self.cursor.fetchall()
