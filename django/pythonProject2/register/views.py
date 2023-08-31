from django.shortcuts import render


def registerView(request):
    return render(request, 'register.html')

def questionnaireView(request):
    length = str(request.GET.get('length'))
    return render(request, 'questionnaire.html')