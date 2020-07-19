# docker-compose-product

A simple setup to deploy your product. 
* DB: 
	* MySQL 
	* redis
* Web: 
	* django
	* traefik: 
		* Auto create a certificate with the let's encrypt HTTP. 
		* Reverse proxy.
		* Load balancer, 
	* nginx: django static files.
* api: 
	* fastapi
