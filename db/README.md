## DB

### Contents
- docker-compose
	- [MySQL](https://github.com/linsamtw/docker-compose-product/tree/master/db#mysql)
	- [redis](https://github.com/linsamtw/docker-compose-product/tree/master/db#redis)
- swarm
	- [MySQL](https://github.com/linsamtw/docker-compose-product/tree/master/db#mysql-1)
	- [redis](https://github.com/linsamtw/docker-compose-product/tree/master/db#redis-1)

#### docker compose

###### MySQL

	docker-compose -f docker-compose.mysql.yml up -d
    
[http://127.0.0.1:8000/](http://127.0.0.1:8000/) ( `root` / `password` )

mysql config

* host: `localhost`
* port: `3306`
* root user/password: `root`/`password`
* other user/password: `django`/`password`


###### Redis

	docker-compose -f docker-compose.redis.yml up -d

* host: `localhost`
* port: `6379`
* `no password`

[medis](https://github.com/luin/medis)
![Medis](http://getmedis.com/screen.png)


#### Swarm

##### MySQL

	docker stack deploy -c docker-compose.mysql.swarm.yml mysql
    
[http://127.0.0.1:8080/](http://127.0.0.1:8080/) ( `root` / `password` )

mysql config

* host: `localhost`
* port: `3306`
* root user/password: `root`/`password`
* other user/password: `django`/`password`

##### redis

	docker stack deploy -c docker-compose.redis.swarm.yml redis
    
* host: `localhost`
* port: `6379`
* password: `password`
    
   
