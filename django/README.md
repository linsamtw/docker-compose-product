# Django + traefik + nginx

### QuickStart

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

