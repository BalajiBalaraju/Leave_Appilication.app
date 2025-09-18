from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('', views.leave_list, name='leave_list'),
    path('leave/new/', views.leave_create, name='leave_create'),
    path('leave/<int:pk>/edit/', views.leave_update, name='leave_update'),
    path('leave/<int:pk>/delete/', views.leave_delete, name='leave_delete'),
]
