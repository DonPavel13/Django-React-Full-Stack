from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        # specify the model that we want to serialize as the " User " model
        # The " User " model is built in Django
        model = User
        # fields taht we want to serialize we accepting  a new user and returning 
        fields = ['id','username','password']
        # this tells to django that we accept write a new password but we don't want
        # to returing it on the authentication phase, no one can read the password 
        extra_kwargs = {'password': {'write_only': True}}
        
        # implementing a method that will call it when we want to create a new version of this user
        def create(self, validated_data):
            user = User.objects.create_user(**validated_data)
            return user
        
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id","title","content","created_at","author"]
        extra_kwargs = {"author": {"read_only": True}}