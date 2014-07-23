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
#####Required environment variables:
```shell
AWS_ACCESS_KEY_ID: ''
AWS_SECRET_ACCESS_KEY: ''
AWS_STORAGE_BUCKET_NAME: ''
AWS_S3_CUSTOM_DOMAIN: ''
DJANGO_SETTINGS_MODULE: ''
DATABASE_URL: ''
REDIS_URL: ''
DEBUG: 1 # Remove to turn off debugging.
```
