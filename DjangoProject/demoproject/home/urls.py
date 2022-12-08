from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home, name="Home"),
    path('', views.index, name="HomePage"),
    path('authorized', views.authorized, name="authorized")
]
