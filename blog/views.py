from django.shortcuts import render,redirect
from .models import Post
from .forms import PostForm
from django.http import HttpResponse
# Create your views here.
def post_list(request):
    all_p = Post.objects.all()
    res = '<ul>'
    for i in all_p:
        res += f'<li>{i}</li>'
    res += '</ul>'
    return HttpResponse(res)
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/posts/')
        else:
            return HttpResponse('Ошибка')
    else:
        form = PostForm()
    return render(request,'add_post.html',{'form':form})
def home(request):
    return render(request,'home.html')