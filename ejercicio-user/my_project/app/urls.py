from django.urls import path
from .views import UserView, RoleView

urlpatterns = [
    path('users/', UserView.as_view()),
    path('roles/', RoleView.as_view()),
]