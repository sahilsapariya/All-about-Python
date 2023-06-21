from django.db import models

# Create your models here.


class Student(models.Model):
    def __str__(self) -> str:
        return self.name
    
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=18)
    father_name = models.CharField(max_length=100)


class Category(models.Model):
    def __str__(self) -> str:
        return self.category_name
    category_name = models.CharField(max_length=100)


class Book(models.Model):
    def __str__(self) -> str:
        return self.book_title
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    book_title = models.CharField(max_length=100)