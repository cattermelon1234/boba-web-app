from datetime import datetime
import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Lingwei1!", 
  database="test"
)

mycursor = db.cursor()

mycursor.execute("SELECT * FROM Person")
#mycursor.execute("CREATE DATABASE testdatabase")

#mycursor.execute("CREATE TABLE Person (name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")
#mycursor.execute("DESCRIBE Person")
#mycursor.execute("INSERT INTO Person (name, age) VALUES (%s,%s)",("Tim", 19))
#db.commit()
#mycursor.execute("SELECT * FROM Person")
#mycursor.execute("CREATE TABLE Test (name varchar(50), created datetime, gender ENUM('M', 'F', 'O') NOT NULL, id int PRIMARY KEY NOT NULL AUTO_INCREMENT)")
#mycursor.execute("INSERT INTO Test (name, created, gender) VALUES (%s,%s,%s)", ("Joey", datetime.now(),"F"))

#mycursor.execute("ALTER TABLE Test ADD COLUMN food VARCHAR(50) NOT NULL")
#mycursor.execute("ALTER TABLE Test DROP food")
#mycursor.execute("ALTER TABLE Test CHANGE name first_name VARCHAR(50)")
#mycursor.execute("DESCRIBE Test")
#print(mycursor.fetchone())
#mycursor.execute("SELECT id FROM Test WHERE gender = 'M' ORDER BY id DESC")

#for x in mycursor:
 # print(x)

#db.commit()
