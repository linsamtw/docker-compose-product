## docker-compose

### Contents
- [MySQL](https://github.com/linsamtw/docker-compose-product/tree/master/db#mysql)
- [redis](https://github.com/linsamtw/docker-compose-product/tree/master/db#redis)
- rabbitmq
- api
- web

------------------

##### MySQL

	up: docker-compose -f docker-compose.mysql.yml up
    down: docker-compose -f docker-compose.mysql.yml down
    up on background: docker-compose -f docker-compose.mysql.yml up -d

[http://127.0.0.1:8000/](http://127.0.0.1:8000/) ( `root` / `password` )

mysql config

* host: `localhost`
* port: `3306`
* root user/password: `root`/`password`
* other user/password: `django`/`password`

---------------------------

##### Redis

	up: docker-compose -f docker-compose.redis.yml up
    down: docker-compose -f docker-compose.redis.yml down
    up on background: docker-compose -f docker-compose.redis.yml up -d

* host: `localhost`
* port: `6379`
* `no password`

[medis](https://github.com/luin/medis)
![Medis](http://getmedis.com/screen.png)


--------------------------

##### rabbitmq

	up: docker-compose -f docker-compose.mysql.yml up
    down: docker-compose -f docker-compose.mysql.yml down
    up on background: docker-compose -f docker-compose.mysql.yml up -d

[http://127.0.0.1:8000/](http://127.0.0.1:8000/) ( `root` / `password` )

mysql config

* host: `localhost`
* port: `3306`
* root user/password: `root`/`password`
* other user/password: `django`/`password`

--------------------------

##### api

--------------------------

##### web




