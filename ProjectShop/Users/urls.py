from django.urls import path
from Users.views import Login_user, SignUpView, logoutview, user_side #type: ignore

urlpatterns = [
    path('login/', Login_user.as_view(), name="login"),
    path('sign-up/', SignUpView.as_view(), name = 'sign_up'),
    path("logout/", logoutview, name="logout"),
    path("user-side/<id>", user_side, name="user_side"),
]