from django.shortcuts import render
from django.http import HttpResponse
from django import template
from django.db.models import Q
from django.views.generic import ListView
from django.template.loader import get_template 
import praw
from .models import News
from datetime import datetime   


def home(request):
    SubredditName()
    #newis= News.objects.all()
    #ordered_authors = Author.objects.order_by('-score', 'last_name')[:30]
    newis = News.objects.order_by('id')
    return render(request, 'base.html', {'newis': newis})


def SubredditName():
    reddit = praw.Reddit(client_id ='tarciQXpZUPk_w',
    client_secret='PPED3JSJ0ph7E1Zh-TbR_W0s_jU',
    username='russkiypython',
    password = 'Faqser95',
    user_agent='russkiypython1')

    subreddit = reddit.subreddit('popular')

    submission_list =[]
    rest_list = []
    
    newis= News.objects.all()

    for submission in subreddit.hot(limit=10):
        submission_list.append(submission.title)
  
    newis= News.objects.all()
    
    for test in newis:
        rest = test.text
        rest_list.append(rest)
        da = test.date
      
    right = list(set(rest_list))
    left = list(set(submission_list))
    for l in left:
        if l in right and left != []:
            None
        else:
            News.objects.create(text=f'{l}')
            print('Done')

def search(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(text__icontains=query)

            results= News.objects.filter(lookups).distinct()

            context={'results': results,
            'submitbutton': submitbutton}

            return render(request, 'search.html', context)

        else:
            return render(request, 'search.html')

    else:
        return render(request, 'search.html')
    
def zaplatka(request):
    newis = News.objects.order_by('-id')
    return render(request, 'zaplatka.html', {'newis': newis})


#notes = News.objects.values().filter(text = f'{rest}').values_list("text", flat=True)
#print(News.objects.values())