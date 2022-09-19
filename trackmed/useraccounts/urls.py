from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.signupview, name="signup"),
    path("useraccount/", views.useraccount, name="useraccount"),
]
