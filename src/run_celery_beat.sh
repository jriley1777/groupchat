

celery -A control_room beat -s celerybeat-schedule --scheduler django_celery_beat.schedulers:DatabaseScheduler
