### A Django template for Fig/Docker

---
#####Requirements:
- [Docker](https://www.docker.io/)
- [Fig](http://orchardup.github.io/fig/install.html)
- [Django](https://www.djangoproject.com/)

***
#####Setup:
```shell
django-admin.py startproject --name=fig-dist.yml --name=Procfile --name=.gitignore --template=https://github.com/bradleyg/django-docker-template/archive/master.zip [project_name]
```
In the project folder:
```shell
cp fig-dist.yml fig.yml
```
Add your AWS keys/config to ```fig.yml```.
```bash
fig build
fig up -d db redis
fig run web python manage.py syncdb
fig up web
```
Point your browser to your docker IP at port 5000.
***
#####Heroku required addons:
- [Redis Cloud](https://addons.heroku.com/rediscloud)
- [Heroku Postgres](https://addons.heroku.com/heroku-postgresql)
