from django.http import HttpResponse,Http404
from django.shortcuts import render
from News.models import NewsItem

PREVIEW_LENGTH=1000

def index(request):
	latest_news=NewsItem.objects.order_by('-pub_date')[:5]
	previews = {}
	for newsItem in latest_news:
		newsItem.preview=newsItem.article[:len(newsItem.article) if len(newsItem.article) <=PREVIEW_LENGTH else PREVIEW_LENGTH]
	return render(request,'News/index.html',{'latest_news':latest_news})

def detail(request,news_id):
	try:
		newsItem=NewsItem.objects.get(pk=news_id)
	except NewsItem.DoesNotExist:
		raise Http404()
	return render(request,'News/detail.html',{'newsItem':newsItem})
