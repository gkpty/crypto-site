from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=100)
	body = models.CharField(max_length=2000)
	post_date = models.DateTimeField('date published')
	def __str__(self):
		return self.title


class Register(models.Model):
	full_name = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	reg_date = models.DateTimeField('date published')
	def __str__(self):
		return self.email

class Referral(models.Model):
	full_name = models.CharField(max_length=200)
	referrer_email = models.CharField(max_length=200)
	referred_email = models.CharField(max_length=200)
	ref_date = models.DateTimeField('date published')
	def __str__(self):
		return self.email


class Contact_Us(models.Model):
	full_name = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	phone = models.CharField(max_length=200)
	question = models.CharField(max_length=1000)
	contact_date = models.DateTimeField('date published')
	def __str__(self):
		return self.question