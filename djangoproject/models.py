from django.db import models


# Create your models here.
class Contact(models.Model):
	fname = models.CharField(max_length = 200)
	lname = models.CharField(max_length = 200)
	email = models.CharField(max_length = 200)
	phone = models.IntegerField()
	message = models.TextField()
	date = models.DateField()


class Employees(models.Model):
	GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
	emp_no = models.AutoField(primary_key=True, db_column='emp_no')
	birth_date = models.DateField(db_column='birth_date')
	first_name = models.CharField(max_length=14, db_column='first_name')
	last_name = models.CharField(max_length=16, db_column='last_name')
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES, db_column='gender')
	hire_date = models.DateField(db_column='hire_date')
	class Meta:
		managed = False
		db_table = "employees"

	def full_name(self):
		# Return the first_name plus the last_name, with space in between.	
		full_name = '%s %s' % (self.first_name, self.last_name)
		return full_name.strip()

