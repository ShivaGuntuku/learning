from django.shortcuts import render

# Create your views here.

def tutorial_create(request):
	return render(request,'tutorial_index.html',{})

def tutorial_view(request):
	return render(request,'tutorial_index.html',{})

def tutorial(request):
	return render(request,'tutorial_index.html',{})

def tutorial_update(request):
	return render(request,'tutorial_index.html',{})
	
def tutorial_delete(request):
	return render(request,'tutorial_index.html',{})