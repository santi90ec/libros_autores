from django.db import models
from django.db.models.fields.related import create_many_to_many_intermediary_model

class Book (models.Model):
    title=models.CharField(max_length=255)
    desc=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    def __repr__(self):
        return f"<Book object: {self.title} Id: {self.id}"
class Author(models.Model):
    first_name=models.CharField(max_length=45)
    last_name=models.CharField(max_length=45)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    notas=models.CharField(max_length=100,null=True)
    books=models.ManyToManyField(Book, related_name="authors")
    def __repr__(self):
        return f"<Author object: {self.first_name} {self.last_name} Id: {self.id}"
# Create your models here.
