from django.urls import path
from Users.views import Login_user


urlpatterns = [
    path('login/', Login_user.as_view(), name="login"),
]