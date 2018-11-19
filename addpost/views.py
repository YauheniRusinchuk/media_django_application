from django.shortcuts import render, redirect
from addpost.forms import PostForm
from db.models import Post
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods



@login_required(login_url='/')
def add_post(request):
    form = PostForm()
    if request.method == "POST":
        postform = PostForm(request.POST,request.FILES or None)
        if postform.is_valid():
            post = Post(user=request.user, title=request.POST['title'],
                    description=request.POST['description'],
                    content=request.POST['content'],
                    img=request.FILES['img'] or None)
            post.save()
        return redirect('/')
    return render(request, 'addpost/add_post.html', {'form': form})
