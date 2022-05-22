from django.urls import path
from Users.views import Login_user, SignUpView #type: ignore


urlpatterns = [
    path('login/', Login_user.as_view(), name="login"),
    path('sign-up/', SignUpView.as_view(), name = 'sign_up'),
]