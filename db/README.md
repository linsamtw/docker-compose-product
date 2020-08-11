## DB

### Contents
- docker-compose
	- [MySQL](https://github.com/linsamtw/docker-compose-product/tree/master/db#mysql)
	- [redis](https://github.com/linsamtw/docker-compose-product/tree/master/db#redis)
- swarm
	- [MySQL](https://github.com/linsamtw/docker-compose-product/tree/master/db#mysql)
	- [redis](https://github.com/linsamtw/docker-compose-product/tree/master/db#redis)

#### docker compose

###### MySQL

	docker-compose -f docker-compose.mysql.yml up -d
    
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)


###### Redis

	docker-compose -f docker-compose.redis.yml up -d

* host: `localhost`
* port: `6379`
* `no password`

download [medis](https://github.com/luin/medis)
![Medis](http://getmedis.com/screen.png)


#### Swarm

##### MySQL

	docker-compose -f docker-compose.mysql.yml up -d

