from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


SEXES = (('M', 'Male'),
         ('F', 'Female'),
         ('U', 'Unknown'))


class User(AbstractUser):
    sex = models.CharField(choices=SEXES, max_length=2, default='U')
    birthday = models.DateField(null=True, blank=True)


class SpecializationManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_delete=False)

    def deleted(self):
        return super().get_queryset().filter(is_delete=True)


class Specialization(models.Model):
    title = models.CharField(max_length=100)
    is_delete = models.BooleanField(default=False)
    objects = SpecializationManager()

    def delete(self, using=None, keep_parents=False):
        self.is_delete = True
        self.save()


class Doctor(User):
    specializations = models.ManyToManyField(Specialization, related_name='docs')
    cabinet = models.PositiveSmallIntegerField(null=True, blank=True)


class Patient(User):
    ssn = models.CharField(max_length=10)
    mobile_number = models.CharField(max_length=20, null=True, blank=True)


class Order(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    time = models.DateTimeField()
