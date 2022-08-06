from django.shortcuts import render, redirect
from .models import Post, Author, Comment
from .forms import CommentForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    latest_blog = Post.objects.all().order_by('-date')[:5]
    return render(request, 'blogposts/index.html', {"posts": latest_blog})

def allposts(request):
    all_blog = Post.objects.all()
    return render(request, 'blogposts/index.html', {"posts": all_blog})

def post_detail(request, slug):
    single_post = Post.objects.get(slug=slug)
    form = CommentForm()
    comments = Comment.objects.filter(post=single_post)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if request.user.is_authenticated:
            if form.is_valid():
                print(form.cleaned_data)
                comment = form.save(commit=False) #IntegrityError at /posts/aayur-Blog/
                comment.post = single_post
                comment.save()

                form = CommentForm()
                return redirect('post-detail', slug=slug)
        # print("Hello1")
        return render(request, 'blogposts/post_detail.html', {"post": single_post, "form":form, "allcomments":comments})
    return render(request, 'blogposts/post_detail.html', {"post": single_post, "form":form, "allcomments":comments})

