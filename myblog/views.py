from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import PostForm
from .models import Posts


def post_create(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit = False)
		instance.save()
		messages.success(request, "Post Successfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		'form' : form
	}
	return render(request,'blog_create.html',context)

def post_detail(request, id = None):
	instance = get_object_or_404(Posts, id = id)
	context = {
		'title' : instance.title,
		'instance' : instance,
	}
	return render(request,'blog_detail.html',context)

def post_list(request):
	queryset_list = Posts.objects.all()
	paginator = Paginator(queryset_list, 5)
	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		queryset = paginator.page(1)
	except EmptyPage:
		queryset = paginator.page(paginator.num_pages)
	context = {
		'object_list' : queryset,
		'title' : 'Post List'
	}
	return render(request,'blog.html',context)

def post_update(request,id=None):
	instance = get_object_or_404(Posts, id = id)
	form = PostForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit = False)
		instance.save()
		messages.success(request, "Post is Updated.")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		'title' : instance.title,
		'instance' : instance,
		'form' : form
	}
	return render(request,'blog_create.html',context)

def post_delete(request, id=None):
	instance = get_object_or_404(Posts, id = id)
	instance.delete()
	messages.success(request, "Post is Deleted.")
	return redirect("posts:list")