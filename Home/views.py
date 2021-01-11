from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
# Create your views here.
def homeview(request):
	if request.method=='POST':
		username=request.POST.get('username')
		option=request.POST.get('options')
		room_code=request.POST.get('roomcode')

		if option=='1':
			game=Game.objects.filter(room_code=room_code).first()
			if game is None:
				message.success(request,'Room code not found')
				return redirect('/')
			if game.is_over:
				message.success(request,'Game is over')
				return redirect('/')
			game.game_opponent= username
			game.save()
			return redirect('/play/'+ room_code +'?username='+username)

		else:
			game=Game(game_creator=username,room_code=room_code)
			game.save()
			return redirect('/play/'+ room_code +'?username='+username)

	return render(request,'home.html',{})

def playview(request,room_code):
	username=request.GET.get('username')
	context={'room_code':room_code,
				'username':username}
	return render(request,'play.html',context)