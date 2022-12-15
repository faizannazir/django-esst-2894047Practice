from django.contrib import admin
from . import models

# Register your models here.
class NotesAdmin(admin.ModelAdmin):
    list_display=('title',)  # display title of model in admin site


admin.site.register(models.Notes, NotesAdmin)