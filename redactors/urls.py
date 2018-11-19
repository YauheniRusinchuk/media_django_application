from django.urls import path
from redactors.views import redactors


app_name = 'redactors'


urlpatterns = [
	path('', redactors, name='redactors_page')
]