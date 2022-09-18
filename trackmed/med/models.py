from django.db import models
from django.contrib.auth.models import User


class PatientBio(models.Model):
	GENDER_CHOICES = (('M', 'Male'),('F', 'Female'),)
	user =models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null= True)
	full_name = models.CharField(max_length=100)
	DOE = models.DateField(blank=True, null= True)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
	location = models.CharField(max_length=50)
	height =  models.FloatField()
	weight = models.PositiveIntegerField(blank=True, null= True)

	class Meta:
		verbose_name = 'PatientBio'
		verbose_name_plural = 'PatientData'

	def __str__(self):
		return self.full_name


class HealthData(models.Model):
	user =models.ForeignKey(User, on_delete=models.CASCADE)
	ailments = models.TextField()
	history_of_ailment =  models.TextField()
	previous_tests = models.TextField()

	class Meta:
		verbose_name_plural = 'HealthData'

	


class Medication(models.Model):
	user =models.ForeignKey(User, on_delete=models.CASCADE)
	medicine = models.CharField(max_length=50)
	days_to_take = models.PositiveIntegerField()
	schedule = models.CharField(max_length=50)

	def __str__(self):
		return self.user.username	







