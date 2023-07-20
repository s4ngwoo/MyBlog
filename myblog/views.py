from django.shortcuts import render, get_object_or_404
from .models import Post, Category


def landing(request):
    posts = Post.objects.all().order_by('-create_date') 
    categories = Category.objects.all()
    context = {'categories':categories,
               'posts': posts, 
               }
    return render(request, 'myblog/landing_post_list.html', context) 

def about(request):
    context = {}
    return render(request, 'myblog/about.html', context)

def contact(request):
    context = {}
    return render(request, 'myblog/contact.html', context)

def post(request, pk):
    post = get_object_or_404(Post, id=pk)
    context = {'pk': pk,
               'post': post}
    return render(request, 'myblog/post_detail.html', context)

def archive(request):
    posts = Post.objects.all().order_by('-create_date')
    context = {'posts': posts}
    return render(request, 'myblog/archive.html', context)