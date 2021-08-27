

from database.database_function import create_connection, select_bieu_hien
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import mysql.connector as mysql


class ActionBieuHien(Action):
    

    def name(self) -> Text:
        return "action_bieu_hien"

    async def run(self, dispatcher, tracker, domain):

        benh = tracker.get_slot("ten_benh")

        conn = create_connection('health_assistant')

        data = select_bieu_hien(conn,benh)

        dispatcher.utter_message(text = data)

        return []
    
