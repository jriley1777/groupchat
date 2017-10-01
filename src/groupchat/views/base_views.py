from django.shortcuts import render
from groupchat import tasks
from groupchat.models import Room, RoomMessage, User
from django.http import JsonResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.

def index(request):
	tasks.print_hello.delay()
	return render(request,'index.html')

def list_rooms(request):
	rooms = Room.objects.values('id','name').all().order_by('id')
	data = list(rooms)
	return JsonResponse(data,safe=False)

def list_friends(request):
	user = User.objects.values('id','username').exclude(username=request.user).order_by('id')
	data = list(user)
	return JsonResponse(data,safe=False)

def get_room_messages(request, room_id):
	messages = RoomMessage.objects.values('message_time','user__username','content').filter(room=room_id).order_by('message_time')
	data = list(messages)
	return JsonResponse(data,safe=False)

def add_room_message(request,room_id):
	message = RoomMessage()
	message.user = User.objects.get(pk=1)
	message.room = Room.objects.get(pk=room_id)
	message.content = request.GET.get('msg')
	message.save()
	return HttpResponseRedirect(reverse('get_room_messages',args=(room_id,)))