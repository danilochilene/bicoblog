# Create your views here.
from django.shortcuts import render_to_response
from django.template import Context, loader
from bicoblog.blog.models import *
from django.http import HttpResponse

def index(request):
	latest_entry_list = Entry.objects.all().order_by('-pub_date')[:5]
	t = loader.get_template('blog/entry_archive.html')
	c = Context({
		'latest_entry_list': latest_entry_list,
	})
	return HttpResponse(t.render(c))

def entry(request, entry_id):
	entry = Entry.objects.get(id=entry_id)
	return render_to_response('blog/entry.html', locals())