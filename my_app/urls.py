
from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name="signup"),
    path('accounts/signin/', views.signin, name="signin"),
]