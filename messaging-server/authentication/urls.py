from django.urls import path
from rest_framework.authtoken import views
from .views import SignupView, LoginView

urlpatterns = [
    path('signup', SignupView.as_view(), name="signup"),
    path('login', LoginView.as_view(), name="login"),
]
