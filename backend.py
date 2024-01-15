from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import sqlite3
from datetime import datetime
import mysql.connector


app = Flask(__name__)
CORS(app)

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Lingwei1!", 
  database="test"
)

mycursor = db.cursor()

events_list = [
   {
       "id":0,
       "event_type": "pull_request",
       "event_name": "change_event"
   },


   {
       "id":1,
       "event_type":"release",
       "event_name":"deployment_event"
   },
   {
       "id":2,
       "event_type":"push",
       "event_name":"workflow_event"
   },
   {
       "id":3,
       "event_type": "pull_request_merged",
       "event_name":"deployment_event"
   }
]

@app.route('/events', methods=['GET', 'POST'])
def events():
   if request.method == 'GET':
       if len(events_list) > 0:
           # encode list of events in json
           name = mycursor.execute("SELECT name FROM Person")
           personID = mycursor.execute("SELECT personID FROM Person")

           return jsonify(json_arrayagg(
               json_merge(
                   json_object('name', name), 
                   json_object('personID', personID)
                )
            ))
       else:
           'Event not found', 404
  
   if request.method == 'POST':
       new_event_type = request.type['event_type']
       new_event_name = request.type['event_name']


       sql = """INSERT INTO event (event_type, event_name)
                VALUES (?, ?, ?)"""
       cursor = cursor.execute(sql, (event_type, event_name))
       db.commit()
       return f"event with the id: 0 created successfully", 201


       new_obj = {
           'id':iD,
           'event_type': new_event_type,
           'event_name': new_event_name
       }


       events_list.append(new_obj)
       return jsonify(events_list), 201


@app.route('/event/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def single_event_workflow(id):
   if request.method == 'GET':
       for event in events_list:
           if event['id'] == id:
               return jsonify(event)
           pass
   if request.method == 'PUT':
       sql = """UPDATE event
               SET event_type=?,
                   event_name=?,
               WHERE id=? """
       for event in events_list:
           if event['id'] == id:
               event['event_type'] = request.event['event_type']
               event['event_name'] = request.event['event_name']
               updated_event = {
                   'id':id,
                   'event_type': event['event_type'],
                   'event_name': event['event_name']
               }
               conn.execute(sql, (event_type, event_name, id))
               conn.commit()
               return jsonify(updated_event)

if __name__ == '__main__':
   app.run(debug=True)