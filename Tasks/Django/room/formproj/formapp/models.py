from django.db import models


class company_form(models.Model):
	name = models.CharField(max_length=50)
	title = models.CharField(max_length=100)
	address = models.CharField(max_length=50)
	city = models.CharField(max_length=20)
	pincode = models.IntegerField()
	discription = models.CharField(max_length=200)
	email = models.EmailField()
	url = models.URLField()
	password = models.CharField(max_length=50)