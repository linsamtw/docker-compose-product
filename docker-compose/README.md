## docker-compose

### Contents
- [MySQL](https://github.com/linsamtw/docker-for-product/tree/master/docker-compose#mysql)
- [redis](https://github.com/linsamtw/docker-for-product/tree/master/docker-compose#redis)
- [rabbitmq](https://github.com/linsamtw/docker-for-product/tree/master/docker-compose#rabbitmq)
- celery
- [api](https://github.com/linsamtw/docker-for-product/tree/master/docker-compose#api)

------------------

#### create network 
因為 docker 會建立虛擬 network，為了避免 compose 之間連線問題，先建立 network，docker 再分別 external 進 network

	docker network create dev

------------------

##### MySQL

	up: docker-compose -f mysql.yml up
	down: docker-compose -f mysql.yml down
	up on background: docker-compose -f mysql.yml up -d

[http://127.0.0.1:8000/](http://127.0.0.1:8000/) ( `root` / `password` )
![phpmyadmin](https://github.com/linsamtw/docker-for-product/blob/master/docker-compose/image/phpmyadmin.png)

mysql config

* host: `localhost`
* port: `3306`
* root user/password: `root`/`password`
* other user/password: `django`/`password`

---------------------------

##### Redis

	up: docker-compose -f redis.yml up
	down: docker-compose -f redis.yml down
	up on background: docker-compose -f redis.yml up -d

* host: `localhost`
* port: `6379`
* `no password`

[medis](https://github.com/luin/medis)
![Medis](http://getmedis.com/screen.png)


--------------------------

##### rabbitmq

	up: docker-compose -f rabbitmq.yml up
	down: docker-compose -f rabbitmq.yml down
	up on background: docker-compose -f rabbitmq.yml up -d

* `flower`: 
[http://127.0.0.1:5555/](http://127.0.0.1:5555/)

* `rabbitmq web`: 
[http://127.0.0.1:15672/](http://127.0.0.1:15672/) ( `worker` / `worker` )

`celery` connect `rabbitmq` config

* host: `localhost`
* port: `5672`
* user/password: `worker`/`worker`

--------------------------

##### api

* build docker image


		make api-latest
		make api


* run


		up: docker-compose -f ./api/docker-compose.api.yml up
		down: docker-compose -f ./api/docker-compose.api.yml down
		up on background: docker-compose -f ./api/docker-compose.api.yml up -d

[http://127.0.0.1:5555/docs](http://127.0.0.1:5555/docs)
![fastapi](https://github.com/linsamtw/docker-for-product/blob/master/docker-compose/image/fastapi.png)


