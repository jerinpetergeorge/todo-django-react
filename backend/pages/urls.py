from django.urls import path

from .views import HomePageView, AboutPageView, user_list

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('users/', user_list, name="user-list")
]
