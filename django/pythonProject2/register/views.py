from django.shortcuts import render


def registerView(request):
    return render(request, 'register.html')
