from django.contrib import admin
from News.models import NewsItem
from News.models import Event

admin.site.register(NewsItem)
admin.site.register(Event)
