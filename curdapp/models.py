from django.db import models



class Employeedata(models.Model):
     employee_id=models.CharField(max_length=20)
     first_name=models.CharField(max_length=50)
     last_name=models.CharField(max_length=50)
     Emailid = models.CharField(max_length=255)
     Mobile=models.IntegerField(max_length=10)
     location=models.CharField(max_length=50)

     def __str__(self) -> str:
          return super().__str__()