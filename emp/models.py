from django.db import models

class Emp(models.Model):
    ename = models.CharField(max_length=20)
    esalary = models.FloatField()
    userid = models.CharField(max_length=20)
    pswd = models.CharField(max_length=20)
    address = models.CharField(max_length=20)

    def __str__(self):
        return self.ename,str(self.esalary),self.userid,self.pswd,self.address

