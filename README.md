# Boba Web Application

Simple overview of use/purpose.

## Description

This project is the prototype of a full stack web application for boba enjoyers, especially for those in the Bay Area. The website features recommended boba shops, an introduction to what boba is, and a personal timeline of my own boba journey and recommendations. There is also a user interactive
portion to the website, which allows users to input their own name, titles, and reviews of boba shops for everyone to see. 

## Getting Started

### Dependencies

* Most of the software is run through MacOS (mac chip)
* Docker installation required
* Install MySQL and MySQLWorkbench

### Installing

* Go to https://hub.docker.com/repository/docker/brianling16/webapplication/general 
  * Go to "tags" and follow the instructions for downloading/pulling the two images
  * There should be an image: "web-server-test" and "mysql"

### Executing program
Step 0: Download everything in the "dependencies" section and follow the installation instructions

Step 1: Open terminal and make sure you are in the downloaded folder
Run: docker build -f Dockerfile . -t web-server-test
Run: docker run --rm -p 8000:5000 -it web-server-test bash
This command maps port 8000 to 5000, which is the port that our backend server is listening on
Run pip install mysql-connector-python

Step 2: start running the mysql server
Run: docker run --name some-mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=Lingwei1! -d mysql
This command creates the mysql image and begins running the container all in one step
Head to mysqlworkbench and click the “+” button with the circle around it next to “MYSQL Connections”
There, you will be prompted to input a name for the connection, port (should be default 3306, so don’t change it), and a root password. Enter in your root password Lingwei1! And you should get a screen that says “connection successful”. You can now access a command prompt in mysqlworkbench to build your database

Step 3: run docker ps and note the container ids 

Step 4: connect both containers to the same local network
Docker network create testNetwork
Docker network connect testNetwork <container_id_1>
Docker network connect testNetwork <container_id_2>
Docker network inspect testNetwork
Look for the ipv4 address of both containers, and in your app.py code you should replace host=”” with host = <ip_address_of_mysql>
You can test if both containers are in the same network by running: 
Curl <ip_address_of_mysql>:3306

You should have 2 different terminals: one for running each container
In your web-server-test container terminal: 
run docker exec -it <container_id> bash
This command lets you run commands inside your web server container
Run ls 
You should have one file, app.py
You can open the file with nano app.py or vi app.py to check its contents
In your mysql container terminal: 
Run docker exec -it <container_id> bash
This command lets you run commands inside your mysql container, although you wont need to

After exec’ing into both containers, go back to your web-server-test terminal
RUN python3 app.py
This will start the backend code for your server
The terminal should print out this text below if the connection was successful: 

* Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.17.0.2:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 182-979-884
 
In any code editor of your choice, open the appropriate index.html file and click “open live server” and paste the link into chrome. 


## Help

Any advise for common problems or issues.
```
command to run if program contains helper info
```

## Authors

Brian Ling (email: brianling16@gmail.com)

## Version History
* 0.1
    * Initial Release
