from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='qabot-home'),
	path('getanswer/', views.getanswer, name="getanswer")
]
