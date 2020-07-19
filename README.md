# docker-compose-product

A simple setup to deploy your product by docker. 
* [DB](https://github.com/linsamtw/docker-compose-product/tree/master/db): 
	* [MySQL](https://github.com/linsamtw/docker-compose-product/tree/master/db#mysql)
	* [redis](https://github.com/linsamtw/docker-compose-product/tree/master/db#redis)
* [Web](https://github.com/linsamtw/docker-compose-product/tree/master/django): 
	* django
	* traefik: 
		* Auto create a certificate with the let's encrypt HTTP. 
		* Reverse proxy.
		* Load balancer, 
	* nginx: django static files.
* api: 
	* [fastapi](https://github.com/linsamtw/docker-compose-product/tree/master/api)
	
* [message queue](https://github.com/linsamtw/docker-compose-product/tree/master/message_queue):
	* rabbitgmq
