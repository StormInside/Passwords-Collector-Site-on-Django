from django.urls import path
from .views import PostDetailView, PostUpdateView, PostDeleteView
from . import views


urlpatterns = [
    path('',views.home, name='home'),
    path('register/',views.register, name='register'),
    path('example/',views.example, name='example'),
    path('profile/',views.profile,name='loged_in'),
    path('profile/update/',views.user_update, name='user_update'),
    # path('password/<int:pk>/', PostDetailView.as_view(), name='password_detail'),
    path('password/<int:pk>/update/', PostUpdateView.as_view(), name='password_detail'),
    path('password/<int:pk>/delete/', PostDeleteView.as_view(), name='password_delete'),
    
    

]