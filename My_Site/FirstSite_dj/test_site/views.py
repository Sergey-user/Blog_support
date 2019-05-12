
from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Post


def main_page(request):
	return render(request, 'base.html')