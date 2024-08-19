from django.db import models

# Create your models here.



class Fan(models.Model):
    name=models.CharField(max_length=200)


    def __str__(self):
        return self.name



class Student(models.Model):
    ismi=models.CharField(max_length=200)
    familyasi=models.CharField(max_length=200)
    fan_nomi=models.ForeignKey(Fan,on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.ismi} | {self.familyasi}"



class Baholar(models.Model):
    fan=models.ForeignKey(Fan,on_delete=models.CASCADE)
    talaba=models.ForeignKey(Student,on_delete=models.CASCADE)
    baho=models.DecimalField(max_digits=3,decimal_places=1)



    def __str__(self):
        return f"{self.talaba} {self.fan} - {self.baho}"


