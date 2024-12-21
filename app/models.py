from django.db import models

# Create your models here.
class Dept(models.Model): 
     deptno = models.CharField(max_length=10, primary_key=True) 
     deptname = models.CharField(max_length=100)
     location = models.CharField(max_length=100)
class Emp(models.Model):
           empno = models.IntegerField(primary_key=True) 
           ename = models.CharField(max_length=100) 
           job = models.CharField(max_length=100) 
           sal = models.DecimalField(max_digits=10, decimal_places=3) #
           comm = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) 
           hiredate = models.DateField()











