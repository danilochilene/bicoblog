# -*- coding: utf8 -*-
from django.utils.translation import ugettext as _
from django.contrib.syndication.views import Feed
from datetime import datetime
from django.db import models

# Create your models here.
class Entry(models.Model):
	title = models.CharField(max_length=128)
	content = models.TextField()
	pub_date = models.DateTimeField(default=datetime.now, blank=True)

	class Meta:
		get_latest_by = 'pub_date'
		ordering = ['-pub_date']
		verbose_name_plural = 'Entries'

	def __unicode__(self):
		return self.title


class LatestEntriesFeed(Feed):
    title = "My site news"
    link = "/sitenews/"
    description = "Updates on changes and additions."

    def items(self):
        return Entry.objects.all()

    def item_title(self, item):
        return item.title
    
    def item_id(self, item):
        return item.id

    def item_description(self, item):
        return item.content

    def item_link(self, item):
    	return "/lastentries/"