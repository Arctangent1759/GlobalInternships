from django.http import HttpResponse,Http404
from django.shortcuts import render
from News.models import NewsItem
from News.models import Event
from datetime import datetime

#index constants
PREVIEW_LENGTH=1100

#detail constants
NUM_REL_STORIES=3
DETAIL_PREVIEW_LENGTH=200

def index(request):
	latest_news=NewsItem.objects.order_by('-pub_date')[:5]
	upcoming_events=Event.objects.filter(start__gte=datetime.today())
	for newsItem in latest_news:
		newsItem.preview=newsItem.article[:len(newsItem.article) if len(newsItem.article) <=PREVIEW_LENGTH else PREVIEW_LENGTH]
	return render(request,'News/index.html',{'latest_news':latest_news,'upcoming_events':upcoming_events.order_by("start")})

def detail(request,news_id):
	try:
		newsItem=NewsItem.objects.get(pk=news_id)
	except NewsItem.DoesNotExist:
		raise Http404()

	#Get random related stories
	randomized_stories=NewsItem.objects.order_by('?');
	related_stories=[]
	i=0;
	while len(related_stories) < NUM_REL_STORIES and i<len(randomized_stories):
		if randomized_stories[i] != newsItem:
			related_stories.append(randomized_stories[i])
		i+=1;


	for story in related_stories:
		story.preview=story.article[:len(story.article) if len(story.article) <=DETAIL_PREVIEW_LENGTH else DETAIL_PREVIEW_LENGTH]

	return render(request,'News/detail.html',{'newsItem':newsItem,'related_stories':related_stories})

def event(request,event_id):
	try:
		event=Event.objects.get(pk=event_id)
	except Event.DoesNotExist:
		raise Http404()
	upcoming_events=Event.objects.filter(start__gte=datetime.today())
	return render(request,'News/eventDetail.html',{'event':event,'upcoming_events':upcoming_events.order_by("start")})
