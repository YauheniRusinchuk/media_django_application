from django.shortcuts import render, HttpResponse
from db.models import Post
from comments.models import Comment
from comments.forms import FormComments
from django.views.decorators.http import require_http_methods
# Create your views here.
import json



@require_http_methods(['GET', 'POST'])
def article(request, **kwargs):
	post = Post.objects.get(pk=kwargs['pk'])
	comments = Comment.objects.filter(post=post)
	form = FormComments()
	if request.is_ajax() and request.POST:
		text = request.POST.get('comment')
		comment = Comment(text=text, post=post)
		comment.save()
		data = {'message': request.POST.get('comment')}
		return HttpResponse(json.dumps(data), content_type='application/json')
	return render(request, 'articles/article.html', {'post': post, 'com': comments, 'form': form})
