from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(i):
    i.session['count']=0
    
    data={
        'word':'Genetate a random word! press generate below',
        'attempt':i.session['count']
    }

    return render(i, 'rand_word/index.html',data)

def generate(i):
    i.session['count']+=1
    unique_id = get_random_string(length=14)
    data={
        'word':unique_id,
        'attempt':i.session['count']
    }
    return render(i, 'rand_word/index.html', data)

def reset(i):
    # del i.session['count']
    return redirect('/')


# Create your views here.
 