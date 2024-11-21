from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.home, name="home"),
	path('myUrls/', views.url_list, name="url_list"),
	path('r/<str:key>/', views.redirect, name="redirect"),
	path('new/', views.new_url, name='new_url'),
	path('edit/<str:key>/', views.edit_url, name="edit_url"),
	path('delete/<str:key>/', views.del_url, name="del_url"),
    path('accounts/', include('django.contrib.auth.urls'), name="login"),
    path('accounts/signup/', views.signup, name="signup"),
    path('accounts/edit', views.edit_account, name="edit_account"),
]