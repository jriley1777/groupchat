from django.conf import settings

from control_room.celery import app

@app.task
def print_hello():
	print 'hello'