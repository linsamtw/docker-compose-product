# docker-compose-product

A simple setup to deploy your product by docker. 
* [DB](https://github.com/linsamtw/docker-compose-product/tree/master/db): 
	* MySQL
	* redis
* [Web](https://github.com/linsamtw/docker-compose-product/tree/master/django): 
	* django
	* traefik: 
		* Auto create a certificate with the let's encrypt HTTP. 
		* Reverse proxy.
		* Load balancer, 
	* nginx: django static files.
* [api](https://github.com/linsamtw/docker-compose-product/tree/master/api): 
	* fastapi
	
* [message queue](https://github.com/linsamtw/docker-compose-product/tree/master/message_queue):
	* rabbitgmq
