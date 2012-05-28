from django.db import models

# Create your models here.
class Entry(models.Model):
	title = models.CharField(max_length=128)
	content = models.TextField()
	pub_date = models.DateTimeField()

class Meta:
	get_latest_by = 'pub_date'
	ordering = ['-pub_date']
	verbose_name_plural = 'Entries'