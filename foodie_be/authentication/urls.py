from django.urls import path

from .views import SignUpView, SignInView

app_name = "authentication"

urlpatterns = [
    path("signup", SignUpView.as_view()),
    path("signin", SignInView.as_view()),

]