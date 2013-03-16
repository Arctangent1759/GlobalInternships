from django.http import HttpResponse,Http404
from django.shortcuts import render
from Event.models import Event
from News.models import NewsItem
from datetime import datetime

# Create your views here.

#detail constants
NUM_REL_STORIES=3
DETAIL_PREVIEW_LENGTH=200


def index(request):
	#Get random related stories
	randomized_stories=NewsItem.objects.order_by('?');
	related_stories=randomized_stories[:min(NUM_REL_STORIES,len(randomized_stories))]
	for story in related_stories:
		story.preview=story.article[:len(story.article) if len(story.article) <=DETAIL_PREVIEW_LENGTH else DETAIL_PREVIEW_LENGTH]
	return render(request,'Event/index.html',{'related_stories':related_stories,'upcoming_events':Event.objects.filter(start__gte=datetime.today()).order_by("start")})
def event(request,event_id):
	try:
		event=Event.objects.get(pk=event_id)
	except Event.DoesNotExist:
		raise Http404()
	upcoming_events=Event.objects.filter(start__gte=datetime.today())
	return render(request,'Event/eventDetail.html',{'event':event,'upcoming_events':upcoming_events.order_by("start")})
