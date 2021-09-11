from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def Home(request):
    return render(request,'generator/home.html')

def About(request):
    return render(request,'generator/about.html')

def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('specialcharacters'):
        characters.extend(list('!@#$%^&*'))

    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    Length = int(request.GET.get('length'))
    thepassword = ''
    for x in range(Length):
        thepassword += random.choice(characters)
    return render(request,'generator/password.html',{'password':thepassword})
