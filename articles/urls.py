from django.urls import path
from articles.views import article

app_name = 'articles'


urlpatterns = [
	path('id<int:pk>/author<str:name>', article, name='article_page')
]