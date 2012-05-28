from django.contrib.syndication.views import *

from .models import Entry

class LastEntries(Feed):
    title = 'Last Entries'
    link = '/'

    def items(self):
        return Entry.objects.all()

    def item_link(self, entry):
        return '/entry/%d/'%entry.id