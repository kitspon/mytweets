from django.views.generic import View
from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import View
from user_profile.models import User
from models import Tweet


class Index(View):
    def get(self, request):
        params = {}
        params["name"] = "Django" 
        return render(request, 'base.html', params)

class Profile(View):
    def get(self, request, username):
        params = dict()
        user = User.objects.get(username=username)
        tweets = Tweet.objects.filter(user=user)
        params["tweets"] = tweets
        params["user"] = user 
        return render(request, 'profile.html', params) 
#def index(request):
 #   if request.method == 'GET':
  #      return HttpResponse('I am called from a get Request')
   # elif request.method == 'POST':
    #    return HttpResponse('I am called from a post Request')

# Create your views here.
