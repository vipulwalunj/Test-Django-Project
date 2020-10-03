from django.db import models


# Create your models here.


class Slot1(models.Model):
    name = models.CharField(max_length=200,null=True)
    average = models.FloatField(null=True)
    strike_rate = models.FloatField( null=True)

    def __str__(self):
        return self.name

class Slot2(models.Model):
    name = models.CharField(max_length=200,null=True)
    average = models.FloatField(null=True)
    strike_rate = models.FloatField( null=True)

    def __str__(self):
        return self.name

class Slot3(models.Model):
    name = models.CharField(max_length=200,null=True)
    average = models.FloatField(null=True)
    strike_rate = models.FloatField( null=True)

    def __str__(self):
        return self.name

class Slot4(models.Model):
    name = models.CharField(max_length=200,null=True)
    average = models.FloatField(null=True)
    strike_rate = models.FloatField( null=True)

    def __str__(self):
        return self.name


class Customer(models.Model):
    slot1 = models.ForeignKey(Slot1, null=True, on_delete=models.CASCADE)
    slot2 = models.ForeignKey(Slot2, null=True, on_delete=models.CASCADE)
    slot3 = models.ForeignKey(Slot3, null=True, on_delete=models.CASCADE)
    slot4 = models.ForeignKey(Slot4, null=True, on_delete=models.CASCADE)

    name = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name