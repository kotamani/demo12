from django.db import models

class Student(models.Model):
    fullname = models.CharField(max_length=20)
    pwd = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    userid = models.CharField(max_length=20, primary_key=True)

    def __str__(self):
        return self.userid+','+self.fullname+','+self.pwd+','+self.address


