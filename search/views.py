from django.shortcuts import render
from db.models import Post
# Create your views here.
def result_search(request, **kwargs):
	text = request.POST['search']
	posts = Post.objects.filter(title__contains=text)
	return render(request, 'search/result.html', {'posts': posts})
