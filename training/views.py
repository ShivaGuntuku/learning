from django.shortcuts import render

# Create your views here.

def tutorial_create(request):
    #TDE Create Tutorial Function
    return render(request, 'tutorial_index.html', {})

def tutorial_view(request):
    #TDE list Tutorial Function
    return render(request, 'tutorial_index.html', {})

def tutorial(request):
    #TDE ALL Tutorial Function
    return render(request, 'tutorial_index.html', {})

def tutorial_update(request):
    #TDE uodate the post Tutorial Function
    return render(request, 'tutorial_index.html', {})
    
def tutorial_delete(request):
    #TDE delete post Tutorial Function
    return render(request, 'tutorial_index.html', {})