import random

from django.shortcuts import render

def indexView(request):
    return render(request, 'index.html')

def passwordView(request):
    newpassword = ''
    length = int(request.GET.get('length'))
    text = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('upper'):
        text.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if request.GET.get('numbers'):
        text.extend('0123456879')
    if request.GET.get('symbols'):
        text.extend('!"№;%:?*$#')
    for i in range(length):
        newpassword += text[random.randint(0,len(text)-1)]
    #                                           из html       из py
    return render(request, 'password.html', {'newpassword':newpassword})