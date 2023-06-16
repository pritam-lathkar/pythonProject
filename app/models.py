from django.db import models

class Student(models.Model):
    student_id=models.SmallIntegerField(max_length=100,primary_key=True)
    student_name=models.CharField(max_length=100,unique=True)
    DOB=models.DateField()
    M_No=models.SmallIntegerField()

    def __str__(self) -> str:
        return self.student_name
        

class Book(models.Model):
    student_id=models.ForeignKey(Student, on_delete=models.CASCADE,unique=True)
    book_id=models.SmallIntegerField()
    book_name=models.CharField(max_length=20)
    checkout_date=models.DateField()
    due_date=models.DateField()

    def __str__(self) -> str:
        return self.book_name

class Author(models.Model):
    book_name=models.ForeignKey(Book, on_delete=models.CASCADE)
    author_id=models.SmallIntegerField()
    author_name=models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.author_name
