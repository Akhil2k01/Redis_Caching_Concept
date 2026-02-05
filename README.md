# Redis_Caching_Concept
This repository consists of Python+Flask code that utilizes Redis caching strategy to display contents of Mysql DB for the end-user. When data  is retrived for the first time the data is cached and kept in Redis until ttl expires. When end user tries to fetch the data next time it is fetched from Redis resulting in increase in fetch speed.
