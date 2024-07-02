from django.urls import path
from . import views

urlpatterns =[
    path('homepage',views.get_homepage,name='homepage'),
    path('write',views.get_write,name='write'),
    path('save',views.save_blog,name='save'),
]
