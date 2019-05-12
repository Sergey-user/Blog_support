from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time

# Create your models here.

def slug_gen(string):
	new_slug = slugify(string, allow_unicode=True)
	return new_slug + '-' + str(int(time()))

class Post(models.Model):
	title = models.CharField(max_length=100, db_index=True)
	slug = models.SlugField(max_length=100, blank=True, unique=True)
	body = models.TextField(blank=True, db_index=True)
	date_pub = models.DateTimeField(auto_now_add=True)
	tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
	
	def get_absolute_url(self):
		return reverse('post_detail_url', kwargs={'slug':self.slug})

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slug_gen(self.title)
		super().save(*args, *kwargs)

	def __str__(self):
		return self.title


class Tag(models.Model):
	title = models.CharField(max_length=50)
	slug = models.SlugField(max_length=50, unique=True)

	def get_absolute_url(self):
		return reverse('tag_detail_url', kwargs={'slug':self.slug})

	def __str__(self):
		return self.title