# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from database.database_function import create_connection, select_bieu_hien
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import mysql.connector as mysql


class ActionBieuHien(Action):
    

    def name(self) -> Text:
        return "action_bieu_hien"

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        benh = tracker.get_slot("ten_benh")

        conn = create_connection('health_assistant')

        data = select_bieu_hien(conn,benh)
        
        dispatcher.utter_message(text= data)

        return []

    def create_connection(databases):
        cnx = None
        try:
            cnx = mysql.connect(
            user='root', password='',
            host='localhost',
            database= databases)
        except Error as e:
            print(e)
        return cnx

    def select_bieu_hien(cons,benh):
        cur = cons.cursor()
        query = ("SELECT bh.descriptions FROM bieu_hien bh, benh b WHERE b.id_benh = bh.id_benh and b.descroptions like %s Limit 1")
        cur.execute(query,("%" + benh + "%",))

        result = cur.fetchone()
        if (result == None | result == ""):
            return "Không có thông tin về biểu hiện bệnh "+ benh
        else:
            return  result
    
