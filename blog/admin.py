from django.contrib import admin
from models import Entry

class EntryAdmin(admin.ModelAdmin):
	list_display = ['id', 'title', 'content', 'pub_date']

admin.site.register(Entry, EntryAdmin)

