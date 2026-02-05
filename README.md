# Redis_Caching_Concept
This repository consists of Python+Flask code that utilizes Redis caching strategy to display contents of Mysql DB for the end-user. When data  is retrived for the first time the data is cached and kept in Redis until ttl expires. When end user tries to fetch the data next time it is fetched from Redis resulting in increase in fetch speed.

# Components
1. Used Redis and Mysql which is running in my local dockers.
2. Used Docker Desktop + WSL2 to setup dockers for Redis and MySQL.
3. Written simple Python + Flask app to display contents to end-users.

# Steps to run the application
1. Setup Redis and MySQL in the localhost
2. Change the connection settings for redis and MySQL in code
3. Simply run python main.py
4. Application should be running in port 5000
5. Open URL http://localhost:5000
