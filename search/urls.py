from django.urls import path
from search.views import result_search

app_name = 'search'

urlpatterns = [
	path('', result_search, name='search_page')
]
