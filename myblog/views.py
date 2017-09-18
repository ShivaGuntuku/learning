from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .forms import PostForm
from .models import Posts


def post_create(request):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit = False)
		instance.user = request.user
		instance.save()
		messages.success(request, "Post Successfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		'form' : form
	}
	return render(request,'blog_create.html',context)

def post_detail(request, slug = None):
	instance = get_object_or_404(Posts, slug = slug)
	if instance.publish > timezone.now().date() or instance.draft:
		if not request.user.is_staff or not request.user.is_superuser:
			raise Http404
	context = {
		'title' : instance.title,
		'instance' : instance,
	}
	return render(request,'blog_detail.html',context)

def post_list(request):
	today = timezone.now().date()
	queryset_list = Posts.objects.active()
	if request.user.is_staff or request.user.is_superuser : 
		queryset_list = Posts.objects.all()
	query = request.GET.get('q')
	if query :
		queryset_list = queryset_list.filter(
			Q(title__icontains = query)|
			Q(content__icontains = query)|
			Q(user__first_name__icontains = query)|
			Q(user__last_name__icontains = query)
			).distinct()
	paginator = Paginator(queryset_list, 5)
	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		queryset = paginator.page(1)
	except EmptyPage:
		queryset = paginator.page(paginator.num_pages)
	context = {
		'object_list' : queryset,
		'title' : 'Post List',
		'page_request_var' : page_request_var,
		'today' : today,
	}
	return render(request,'blog.html',context)

def post_update(request,slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Posts, slug = slug)
	form = PostForm(request.POST or None, request.FILES or None, instance=instance)
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

def post_delete(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Posts, slug = slug)
	instance.delete()
	messages.success(request, "Post is Deleted.")
	return redirect("posts:list")