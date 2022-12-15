# from django.shortcuts import render
# Class based views 

from django.views.generic import TemplateView,ListView,DetailView,CreateView     
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime

from notes.models import Notes
from .form import NotesForm
# Template view
class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'today':datetime.today(),'name':"FaizanNazir"}

# Login required
class AuthorizeView(LoginRequiredMixin ,TemplateView):
    template_name = 'home/authorize.html'
    login_url = '/admin'

# Listview of notes

class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"    # updating default object name objects to notes
    template_name = "notes/notes_list.html"

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"                 
    template_name = "notes/notesdetails.html"

class NotesCreateView(CreateView):
    model = Notes
    fields = ['title','text']
    success_url = '/classview/notes'
    template_name = 'notes/new_notes.html'

class DjangoNotesCreateView(CreateView):
    model = Notes
    success_url = '/classview/notes'
    form_class = NotesForm
    template_name = 'notes/notes_form.html'