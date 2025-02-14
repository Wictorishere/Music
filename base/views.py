from django.shortcuts import render
from .models import Artist

def home(request):
   artists = Artist.objects.all()
   context = {
      'artists' : artists
   }
   return render(request,'base/home.html',context)
