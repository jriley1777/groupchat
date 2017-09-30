from django.shortcuts import render
from groupchat import tasks

# Create your views here.

def index(request):
	tasks.print_hello.delay()
	return render(request,'index.html')