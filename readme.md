
This is a real time chat application using django and django-channels.

It uses a stack of postgres, redis, celery, django, flower, and celery beat.

Build and run with docker http://www.docker.com

**Current code assumes docker for mac and local install on mac.  Setting db change required for remote/Linux install/build.

Restart and rebuild
`docker-compose build && docker-compose up -d`

If you want to scale more (e.g. 3) celery workers
`docker-compose scale celery_worker=3`

Shutdown running app
`docker-compose down`

For local install, a pg database will first need to be created called `groupchat`

To migrate initial models
`docker-compose build && docker-compose up -d && docker-compose run web python manage.py migrate`

To create django-admin superuser
`docker-compose build && docker-compose up -d && docker-compose run web python manage.py createsuperuser`


The app will run from http://localhost:8000
The flower monitor will run from http://localhost:7001