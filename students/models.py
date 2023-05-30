from django.db import models

# Create your models here.
class Student(models.Model):
    student_number = models.PositiveIntegerField()  # Field to store the student's identification number as a positive integer
    first_name = models.CharField(max_length=50)  # Field to store the student's first name as a character string with a maximum length of 50 characters
    last_name = models.CharField(max_length=50)  # Field to store the student's last name as a character string with a maximum length of 50 characters
    email = models.EmailField(max_length=100)  # Field to store the student's email address as a character string with a maximum length of 100 characters
    field_of_study = models.CharField(max_length=50)  # Field to store the student's field of study as a character string with a maximum length of 50 characters
    gpa = models.FloatField()  # Field to store the student's grade point average (GPA) as a floating-point number

    def __str__(self):
        return f"Student: {self.first_name} {self.last_name}"  # Method that returns a string representation of the Student object, displaying the student's first name and last name
