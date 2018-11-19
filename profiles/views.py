from django.shortcuts import render
from django.contrib.auth.models import User
from db.models import Post

# Create your views here.
def profiles(request, **kwargs):
	user = User.objects.get(pk=kwargs['pk'])
	posts = Post.objects.filter(user=user)
	return render(request, 'profiles/profiles.html', {'user_p':user,'posts':posts})
