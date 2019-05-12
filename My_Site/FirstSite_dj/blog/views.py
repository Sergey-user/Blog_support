
from django.shortcuts import render, redirect

# Create your views here.
from .models import Post, Tag
from django.views.generic import View
from .forms import TagForm, PostForm
from .utils import *

def blog_page(request):
	posts = Post.objects.all()
	return render(request, 'blog/blog_page.html', context={'posts':posts})

def post_detail(request, slug):
	post = Post.objects.get(slug__iexact=slug)
	return render(request, 'blog/post_detail.html', context={'post': post})

def  tags_list(request):
	tags = Tag.objects.all()
	return render(request, 'blog/tags_list.html', context={'tags': tags})

def tag_detail(request, slug):
	tag = Tag.objects.get(slug__iexact=slug)
	return render(request, 'blog/tag_detail.html', context={'tag': tag})


class PostCreate(ObjectCreateMixin, View):

	model_form = PostForm
	template = 'blog/post_create.html'

class TagCreate(ObjectCreateMixin, View):

	model_form = TagForm
	template = 'blog/tag_create.html'


class TagUpdate(View):
	def get(self, request, slug):
		tag = Tag.objects.get(slug_iexact=slug)
		bound_form = TagForm(instance=tag)
		return render(request, 'blog/tag_update_form.html', context={'form': bound_form, 'tag': tag})

	def post(self, request, slug):
		tag = Tag.objects.get(slug__iexact=slug)
		bound_form = TagForm(request.POST, instance=tag)

		if bound_form.is_valud():
			update_tag = bound_form.save()
		return render(request, 'blog/tag_update_url', context={'form': bound_form, 'tag': tag})
