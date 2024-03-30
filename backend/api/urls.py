from django.urls import path
from . import views

urlpatterns = [
    path("notes/", views.NoteListCreate.as_view(), name="note-list"),
    # <int:pk> stands for pirmary key which is a integer the " id " 
    path("notes/delete/<int:pk>/", views.NoteDelete.as_view(), name="delete-note"),
]