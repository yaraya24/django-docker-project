from django.urls import path
from .views import HomePageView, AboutMePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutMePageView.as_view(), name='about_me')
]