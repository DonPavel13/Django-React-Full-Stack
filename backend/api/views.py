from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note

# Create your views here.
# this is a generic list view
class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)
    
    # serialize it self ( NoteSerializer ) passed with different data, will check if it is valid or not
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else: 
            print(serializer.errors)
     
# deleting notes       
class NoteDelete(generics.DestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)
    
# this is a generic view built in into Django that handles creating a new user or object for us
class CreateUserView(generics.CreateAPIView):
    # here's a list of all the different object that we going to look at when creating a new user
    # to make sure we don't create a user that already exists
    queryset = User.objects.all()
    # this tell as what kind of data we need to accept to make a new user ( username, password )
    serializer_class = UserSerializer
    # specify who can actually calls it, in this case anyone " AllowAny "
    permission_classes = [AllowAny]