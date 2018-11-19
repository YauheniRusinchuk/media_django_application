from django.urls import path
from addpost.views import add_post

app_name = 'addpost'

urlpatterns = [
    path('', add_post, name='addpost_page')
]
