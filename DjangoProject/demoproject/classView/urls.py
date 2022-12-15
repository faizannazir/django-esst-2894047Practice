from django.urls import path

from . import views

urlpatterns = [
    path('',views.HomeView.as_view(), name='home'),
    path('authorize', views.AuthorizeView.as_view(),name='authorize'),
    path('notes',views.NotesListView.as_view(), name='notes_list'),
    path('notes/<int:pk>',views.NotesDetailView.as_view(),name="detail"),
    path('newnote',view=views.NotesCreateView.as_view(),name='newnote'),
    path('djangonote',view=views.DjangoNotesCreateView.as_view(),name='djangonote'),
]
