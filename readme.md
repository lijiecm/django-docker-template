### A Django template for Fig/Docker

---
#####Requirements:
- [Docker](https://www.docker.io/)
- [Fig](http://www.fig.sh/install.html)
- [Django](https://www.djangoproject.com/)

***
#####Setup:
```shell
django-admin.py startproject --name=fig-dist.yml --name=Procfile --name=.gitignore --template=https://github.com/bradleyg/django-docker-template/archive/master.zip [project_name]
```
In the project folder:
```shell
cp fig-dist.yml fig.yml
fig up -d db redis
fig run web python3 manage.py syncdb
fig up
```
Point your browser to your docker IP at port 5000.
***
#####Required environment variables:
```shell
STATIC_HOST: ''
DATABASE_URL: ''
REDIS_URL: ''
SECRET_KEY: ''
DEBUG: 1 # Remove to turn off debugging.
```
