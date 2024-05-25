from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    birth_date = models.DateField()

    def __str__(self):
        return f"{self.name} {self.last_name}"

class Book(models.Model):
    isbn = models.CharField(max_length=13, primary_key=True, unique=True, null=False)
    title = models.CharField(max_length=100)
    anio = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    
    def __str__(self):
        return f"{self.isbn} {self.title}"
    