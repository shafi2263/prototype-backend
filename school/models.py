from django.db import models
from django.contrib.auth.models import User

USER_TYPE = (
			(1, 'Admin'),
			(2, 'Teacher'),
			(3, 'Parents'),
	)

class UserType(models.Model):
	user = models.OneToOneField(User)
	user_type = models.CharField(choices = USER_TYPE, max_length=2)
	
	#def __unicode__(self):
	#	return self.user.username;

class Marks(models.Model):
   subject1=models.IntegerField()
   subject2=models.IntegerField()


class Student(models.Model):
	name=models.CharField(max_length=200)
	class_field = models.IntegerField()
	section=models.CharField(max_length=1)
	marks = models.ForeignKey(Marks)
	def __str__(self):
		return self.name


class Parents(models.Model):
	name_parents=models.CharField(max_length=200)
	student = models.ForeignKey(Student)
	email=models.EmailField(max_length=50)
	usertype = models.ForeignKey(UserType)

	def __str__(self):              
		return self.username

class Teacher(models.Model):
    name_teacher=models.CharField(max_length=200)
    class_field_teacher=models.IntegerField(null=True, blank = True)
    section = models.CharField(max_length=1, null = True, blank = True)
    email=models.EmailField(max_length=50)
    usertype = models.ForeignKey(UserType)
    
    def __str__(self):              
        return self.username


