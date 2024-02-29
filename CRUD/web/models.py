from django.db import models

# Create your models here.
class student(models.Model):
    sid = models.IntegerField(default = 000)
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    batch = models.IntegerField()
    email = models.EmailField()
    grade = models.FloatField()


    def __str__(self) -> str:
        return f'student: {self.first_name} {self.last_name}'
    
class course(models.Model):
    name = models.CharField(max_length = 50)
    instructor = models.CharField(max_length = 20)
    code = models.CharField(max_length = 20)
    crdthr  = models.IntegerField()


