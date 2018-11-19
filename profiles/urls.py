from django.urls import path, include
from profiles.views import profiles


app_name = 'profiles'


urlpatterns = [
    path('id<int:pk>/<str:name>', profiles, name='profiles_page')
]
