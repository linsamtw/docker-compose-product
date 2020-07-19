# Django + traefik + nginx

### QuickStart
First, replace following setting: 
* [mysql host](https://github.com/linsamtw/docker-compose-product/blob/master/django/.env#L1)
* [setup.py email](https://github.com/linsamtw/docker-compose-product/blob/master/django/setup.py#L19)
* [docker-compose email](https://github.com/linsamtw/docker-compose-product/blob/master/django/docker-compose.django.yml#L17)
* [web domain name](https://github.com/linsamtw/docker-compose-product/blob/master/django/docker-compose.django.yml#L37)
* [nginx domain name](https://github.com/linsamtw/docker-compose-product/blob/master/django/docker-compose.django.yml#L53)


You can set a free domain name on [no-ip](https://www.noip.com/login?ref_url=console).

Cheap cloud machine to deploy you web [linode](https://www.linode.com/pricing/), US$ 5 /mon for one machine.

### run MySQL db for django
	
    docker-compose -f db/docker-compose.mysql.yml up -d

### generate database, django table

    cd django;
    python3 gendb.py;
    pipenv sync;
    pipenv run python web/manage.py migrate;

### build docker image
	
    docker-compose -f docker-compose.django.yml build
    
### run django

    docker-compose -f docker-compose.django.yml up

### template

[material-dashboard](https://www.creative-tim.com/product/material-dashboard)

reference: 

[https://github.com/creativetimofficial/material-dashboard](https://github.com/creativetimofficial/material-dashboard)

