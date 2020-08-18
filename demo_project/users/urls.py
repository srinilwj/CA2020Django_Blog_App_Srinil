from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.Signupview, name = 'signup'),
    path('login/', views.Loginview, name = 'login'),
    path('', views.Homeview, name = 'home'),
    path('home/user/', views.Userhomeview, name = 'home-user'),
    path('createblog/', views.Createblogview, name = 'create-blog'),
    path('deleteblog/<int:id>', views.Deleteblogview, name = 'delete-blog'),
    #path('editblog/<int:id>', views.Editblogview, name = 'edit-blog'),
    path('updateblog/<int:id>', views.Updateblogview, name = 'update-blog'),
    path('viewblog/<int:id>', views.Viewblogview, name = 'view-blog'),
]