# Django-PostgreSQL-Apache-Docker

## Install it

```
./resources/setup.sh
```

It will initialize the password of the db in resources/local.ini and then the db in /opt/dcpad/

To change the folder, edit [docker-compose.yml](https://github.com/bryan-brancotte/Django-PostgreSQL-Apache-Docker/blob/master/docker-compose.yml#L9). For testing purpose you can set it to /tmp/dcpad/.

## Run it

### Production use case

```
docker-compose up --build [-d]
```

### Development use case

If you want to run the webserver with a `python manage runserver.py`, like during your development, you need to have access to the db. To do so start the database: 
```
docker-compose run db
```
 and then in your terminal: 
 ```
 python manage runserver.py
 ```
 The ip of the database is found thanks to [get_db_ip](./composeexample/db_finder.py), if you encounter any problem feel free to fix it and do a PR !

## None-apache hosting


### Using django web server
You can use django to server the project:
```
docker-compose run web django
```
which is a shortcut for
```
docker-compose run web python manage.py runserver 0.0.0.0:80
```
It will be served at [http://172.18.0.3](http://172.18.0.3)

### Using gunicorn

You can use gunicorn to serve in https the project:
```
docker-compose run web gunicorn
```
It will serve in https using the certs specified in default.ini/local.ini

It will be served at [https://172.18.0.3](https://172.18.0.3)

### No hosting, just a shell
You can enter the container by typing
```
docker-compose run web bash
```

### No hosting, just the db
You can enter the container by typing
```
docker-compose run db
```

