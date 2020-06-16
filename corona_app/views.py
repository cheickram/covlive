from django.shortcuts import render, redirect
import requests
from .models import *

# Create your views here.

def home(request):    
    response = requests.get('https://api.covid19api.com/summary')
    data = response.json()
    
    NewConfirmed = data['Global']['NewConfirmed']
    TotalConfirmed = data['Global']['TotalConfirmed']
    NewDeaths = data['Global']['NewDeaths']
    TotalDeaths = data['Global']['TotalDeaths']
    NewRecovered = data['Global']['NewRecovered']
    TotalRecovered = data['Global']['TotalRecovered']
    
    countries = []
    for i in range(len(data['Countries'])):    
        countries.append(data['Countries'][i])
    
    comments = Comment.objects.all()[:10]
    print(comments)
    
    
    if request.method == 'POST':
        email = request.POST.get('email')
        
        newSuscriber = Suscriber(email= email, )
        newSuscriber.save()
        
    
    return render(request, 'corona_app/index.html', locals())


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        comment = request.POST.get('comment')
        
        newContact = Contact(name= name, email= email, phone= phone, comment= comment)
        newContact.save()
        
        name = name.capitalize()
        
        print(' {} - {} \n {} '.format(name, email, comment))
        sent = True
        print(sent)
        return render(request, 'corona_app/contact.html', locals())

    sent = False
    print(sent)
    return render(request, 'corona_app/contact.html', locals())


def donnees_par_pays(request):    
    response = requests.get('https://api.covid19api.com/summary')
    data = response.json()
    
    NewConfirmed = data['Global']['NewConfirmed']
    TotalConfirmed = data['Global']['TotalConfirmed']
    NewDeaths = data['Global']['NewDeaths']
    TotalDeaths = data['Global']['TotalDeaths']
    NewRecovered = data['Global']['NewRecovered']
    TotalRecovered = data['Global']['TotalRecovered']
    
    countries = []
    for i in range(len(data['Countries'])):    
        countries.append(data['Countries'][i])
    
    return render(request, 'corona_app/donnees_par_pays.html', locals())


def apropos(request):
    return render(request, 'corona_app/apropos.html', locals())


def cas_conf(request):
    
    comments = Comment.objects.filter(linked_to=0)
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        linked_to = 0
        name = name.capitalize()

        newComment = Comment(name= name, email= email, comment= comment, linked_to = linked_to)
        newComment.save()
        
        sent = True
        return render(request, 'corona_app/nbr_cas_conf.html', locals())

    sent = False
    return render(request, 'corona_app/nbr_cas_conf.html', locals())


def cas_deces(request):
    
    comments = Comment.objects.filter(linked_to=1)
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        linked_to = 1
        name = name.capitalize()

        newComment = Comment(name= name, email= email, comment= comment, linked_to = linked_to)
        newComment.save()
        
        sent = True
        return render(request, 'corona_app/nbr_deces.html', locals())

    sent = False
    return render(request, 'corona_app/nbr_deces.html', locals())


def tests(request):
    
    comments = Comment.objects.filter(linked_to=2)
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        linked_to = 2
        name = name.capitalize()

        newComment = Comment(name= name, email= email, comment= comment, linked_to = linked_to)
        newComment.save()
        
        sent = True
        return render(request, 'corona_app/tests.html', locals())

    sent = False
    return render(request, 'corona_app/tests.html', locals())


def act_medias(request):
    
    comments = Comment.objects.filter(linked_to=3)
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        linked_to = 3
        name = name.capitalize()

        newComment = Comment(name= name, email= email, comment= comment, linked_to = linked_to)
        newComment.save()
        
        sent = True
        return render(request, 'corona_app/act_medias.html', locals())

    sent = False
    return render(request, 'corona_app/act_medias.html', locals())



def act(request):
    
    comments = Comment.objects.filter(linked_to=4)
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        linked_to = 4
        name = name.capitalize()

        newComment = Comment(name= name, email= email, comment= comment, linked_to = linked_to)
        newComment.save()
        
        sent = True
        return render(request, 'corona_app/activites.html', locals())

    sent = False
    return render(request, 'corona_app/activites.html', locals())


def medias_sociaux(request):
    
    comments = Comment.objects.filter(linked_to=5)
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        linked_to = 5
        name = name.capitalize()

        newComment = Comment(name= name, email= email, comment= comment, linked_to = linked_to)
        newComment.save()
        
        sent = True
        return render(request, 'corona_app/medias_sociaux.html', locals())

    sent = False
    return render(request, 'corona_app/medias_sociaux.html', locals())


def info(request):
    
    comments = Comment.objects.filter(linked_to=6)
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        linked_to = 6
        name = name.capitalize()

        newComment = Comment(name= name, email= email, comment= comment, linked_to = linked_to)
        newComment.save()
        
        sent = True
        return render(request, 'corona_app/info.html', locals())

    sent = False
    return render(request, 'corona_app/info.html', locals())

def analyses(request):
    return render(request, 'corona_app/analyses.html', locals())

