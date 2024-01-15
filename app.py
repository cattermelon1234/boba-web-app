from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import sqlite3
from datetime import datetime
import mysql.connector

#RUNNING INSTRUCTIONS
#docker network create testNetwork
#docker network connect testNetwork containerid-1
#docker network connect myNetwork containerid-2
#docker network inspect testNetwork, and put in the sql network ip as host
#docker exec -it both containers bash
# you can also test with curl (host_ip):3306

app = Flask(__name__)
CORS(app)

db = mysql.connector.connect(
  host="172.18.0.2", #may be different, check network inspect
  user="root",
  passwd="Lingwei1!", 
  database="entries"
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
       response = jsonify({'some': 'data'})
       response.headers.add('Access-Control-Allow-Origin', '*')
       if len(events_list) > 0:
          # encode list of events in json
          #mycursor.execute("SELECT CONCAT('[', GROUP_CONCAT(JSON_OBJECT('name', name, 'phone', phone)),']') FROM Entries")
          entries = []
          print("inside get")
          mycursor.execute("SELECT * FROM Entries")
          data = mycursor.fetchall()
          fields=mycursor.description

          column_list = []
          for i in fields:
            column_list.append(i[0])

          final_resultset = []
          for row in data:
            result = {}
            result[column_list[0]] = row[0]
            result[column_list[1]] = row[1]
            result[column_list[2]] = row[2]
            final_resultset.append(result)

          j=json.dumps(final_resultset)
          print(j)
          print("exited for loop")
          return jsonify(final_resultset)
       else:
           'Event not found', 404
  
   if request.method == 'POST':
       response = jsonify({'some': 'data'})
       response.headers.add('Access-Control-Allow-Origin', '*')

       name = request.json['name']
       title = request.json['title']
       text = request.json['text']

       mycursor.execute("INSERT INTO Entries(name, title, text) VALUES(%s,%s,%s)", (name, title, text))
       db.commit()
       return f"event with the id: 0 created successfully", 201


       #new_obj = {
           #'id':iD,
           #'event_type': new_event_type,
           #'event_name': new_event_name
       #}


       #events_list.append(new_obj)
       #return jsonify(events_list), 201


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
   app.run(host='0.0.0.0', port=5000, debug=True)
