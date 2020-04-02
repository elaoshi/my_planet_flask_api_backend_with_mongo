# it's a flask api project 
Environment: 
python 3.7
flask + mongodb + docker

# main code: 
in server folder
# how to test  :
run : sh test.sh 


# how to start it : 
1. install docker and docker-compose

2. you can change password in config file : 
docker-compose.yml 

3. then runing: ``` sh build.sh ```


# access api and mongo online
you can access mongodb by express
http://localhost:8081

you can access flask api server backend online with api documents and test Api online
http://localhost:5000

# need to import initial data to mongodb by host machine
python3.7 initData/import_data_to_mongodb.py

or 

inside docker instance 
run : 
docker exec -it eric_flask-web_1 /bin/bash
python initData/import_data_to_mongodb.py

# screenshots
