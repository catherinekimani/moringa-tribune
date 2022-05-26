from django.shortcuts import render,redirect
from django.http import Http404,HttpResponse
from django.core.exceptions import ObjectDoesNotExist
import datetime as dt
from .models import Article

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')
def index(request):
    return render(request, 'index.html')

def news_today(request):
    date = dt.date.today()
    news = Article.today_news()
    return render(request, 'all-news/today-news.html',{"date": date, "news":news})

def past_days_news(request,past_date):
    
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()
    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
    
    if date == dt.date.today():
        return redirect(news_today)
    
    news = Article.days_news(date)
    return render(request, 'all-news/past-news.html', {"date":date,"news":news})
    
def search_results(request):


    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Article.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-news/search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html',{"message":message})
    
def article(request,article_id):
    try:
        article = Article.objects.get(id = article_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,"all-news/article.html", {"article":article})

