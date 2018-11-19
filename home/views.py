from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from db.models import Post



# Create your views here.
def home(request):
	result = Post.objects.all()
	paginator = Paginator(result,10)
	page = request.GET.get('page',1)
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	return render(request,'home/home.html',{"posts": posts})
