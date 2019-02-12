from django.urls import path
from user_extended import views

urlpatterns = [
    path('user-change/', views.user_change, name='user_change')
]
