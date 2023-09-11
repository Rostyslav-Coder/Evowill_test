"""Unut Test Module"""

# import sys
import json
import sqlite3
import unittest
from unittest.mock import patch

from src.bored_api import BoredApi
from src.database import ActivityDB

# sys.path.insert(0, './src')


class TestBoredApi(unittest.TestCase):
    @patch("urllib.request.urlopen")
    def test_get_random_activity(self, mock_urlopen):
        mock_urlopen.return_value.__enter__.return_value.read.return_value.decode.return_value = json.dumps(
            {"activity": "Test activity"}
        )
        api = BoredApi()
        activity = api.get_random_activity()
        self.assertEqual(activity, {"activity": "Test activity"})


# class TestActivityDB(unittest.TestCase):
#     def setUp(self):
#         self.db = ActivityDB()

#     def test_save_and_get_activity(self):
#         activity = {
#             "activity": "Test activity",
#             "type": "Test type",
#             "participants": 1,
#             "price": 0.1,
#             "link": "Test link",
#             "key": "Test key",
#             "accessibility": 0.1
#         }
#         # Добавляем активность 5 раз
#         for _ in range(5):
#             self.db.save_activity(activity)
        
#         # Получаем последние активности
#         activities = self.db.get_latest_activities()
        
#         # Проверяем, что возвращено 5 активностей
#         self.assertEqual(len(activities), 5)
        
#         # Проверяем, что у всех активностей тип - 'Test type'
#         for activity in activities:
#             self.assertEqual(activity[2], 'Test type')

#         # Удаляем тестовые данные из базы данных
#         self.db.cursor.execute('DELETE FROM activities WHERE type = ?', ('Test type',))


class TestActivityDB(unittest.TestCase):
    def setUp(self):
        # global conn
        self.conn = sqlite3.connect(":memory:")
        self.db = ActivityDB()
    
    def tearDown(self):
        """Cleanup the database after each test."""
        self.db.cursor.execute("DELETE FROM activities WHERE type = 'Test type'")
        self.db.conn.commit()

    def test_save_and_get_activity(self):
        activity = {
            "activity": "Test activity",
            "type": "Test type",
            "participants": 1,
            "price": 0.1,
            "link": "Test link",
            "key": "Test key",
            "accessibility": 0.1,
        }
        self.db.save_activity(activity)
        activities = self.db.get_latest_activities()
        self.assertEqual(
            activities[0][1:],
            ("Test activity", "Test type", 1, 0.1, "Test link", "Test key", 0.1),
        )


if __name__ == "__main__":
    unittest.main()
