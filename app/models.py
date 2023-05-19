from django.db import models

# Create your models here.

class Student(models.Model):
    Sname=models.CharField(max_length=100)
    Sid=models.IntegerField(primary_key=True)
    Sage=models.IntegerField()

    def __str__(self) -> str:
        return str(self.Sid)
