from django.urls import path

from . import views
urlpatterns = [
    path('',views.list,name="notes_list"),
    path('<int:pk>',views.detail, name="detail"),
]