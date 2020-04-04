
# It's a flask api project  - my planet
Author : eric ( ericlzyu@gmail.com )

# Environment: 
python 3.7

flask + mongodb + docker

# Main code: 
In server folder
# how to test  :
Run :  ``` sh test.sh ``` 


# How to start it : 
1. install docker and docker-compose

2. you can change password in config file : 
docker-compose.yml 

3. then runing: ``` sh build.sh ```


# Access api and mongo online
You can access mongodb by express 

http://localhost:8081

You can access flask api server backend online with api documents and test Api online

http://localhost:5000

# Need to import initial data to mongodb by host machine
``` python3.7 initData/import_data_to_mongodb.py ```

or 

Inside docker instance 

Run :

``` docker exec -it my_planet_flask_api_backend_with_mongo_flask-web_1 /bin/bash ```

``` python initData/import_data_to_mongodb.py ```

# Screenshots

<img src="https://github.com/elaoshi/my_planet_flask_api_backend_with_mongo/blob/master/screenshots/api.png?raw=true" width=200>
<img src="https://github.com/elaoshi/my_planet_flask_api_backend_with_mongo/blob/master/screenshots/friends.png?raw=true" width=200>
<img src="https://github.com/elaoshi/my_planet_flask_api_backend_with_mongo/blob/master/screenshots/favourite.png?raw=true" width=200>

