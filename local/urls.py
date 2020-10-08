from django.urls import path
from . import views

app_name = "local"
urlpatterns = [
    path('', views.auth, name="auth"),
    path('edit/', views.edit, name="edit"),
    path('order/', views.orders, name="orders"),
]
