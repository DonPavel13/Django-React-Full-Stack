from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):
    # django uses an ORM ( object relational mapping )
    # write the model definition in python and django can automatically convert this 
    # into the correct database code
    # here we going to define the model definition in python 
    title = models.CharField(max_length=100)
    content = models.TextField()
    # the parameters indicates that it adds automatically whenever a new instace is created
    created_at = models.DateTimeField(auto_now_add=True)
    # specify who made this note
    # on_delete=models.CASCADE means that when we delete the user we delete all the notes that that user has
    # related_name="notes" means what fieldname we want to put on the user that references all of it's notes
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")
    
    def __str__(self):
        return self.title