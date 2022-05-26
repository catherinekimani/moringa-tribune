from xml.dom.minidom import Document
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    path('', views.index, name='home'),
    path('newsToday/',views.news_today,name='newsToday'),
    path('search/', views.search_results, name = 'search_results'),
    path('archives/<past_date>/',views.past_days_news,name = 'pastNews'),
    path('article/<article_id>',views.article,name ='article'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)