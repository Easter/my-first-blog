from django.urls import path
from . import views

urlpatterns = [
    path('',views.poll_list,name="post_list")
]
