from django.urls import path
from . import views

urlpatterns =[
    path('homepage',views.get_homepage,name='homepage'),
    path('write',views.get_write,name='write'),
    path('save',views.save_blog,name='save'),
    path('all',views.show_all,name='all'),
    path('<int:bid>/',views.get_one_blog,name='oneblog'),
    path('delete/<int:bid>/',views.delete_blog,name='delblog'),
    path('update/<int:bid>/',views.updateblog,name='updateblog'),
    path('update_/<int:bid>/',views.update_blog,name='update_blog'),
]
