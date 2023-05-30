"""
This code defines a Django form, 'StudentForm', which is used to create a form for collecting student information. 
The form is based on the 'Student' model, imported from the local 'models.py' file.
The fields in the form include 'student_number', 'first_name', 'last_name', 'email', 'field_of_study', and 'gpa'.
Each field is associated with a label to provide a clear description for users.
To enhance the form's appearance and functionality, various widgets are applied to the fields. The widgets include 'NumberInput' 
for 'student_number' and 'gpa', 'TextInput' for 'first_name', 'last_name', and 'field_of_study', and 'EmailInput' for 'email'. 
CSS class 'form-control' is added to each widget to apply a consistent styling.
By utilizing this form, users can easily input and submit student information in a structured and user-friendly manner.
"""

from django import forms
from .models import Student

class StudentForm (forms.ModelForm):
    class Meta:
        model = Student
        fields = [ 'student_number','first_name','last_name','email', 'field_of_study','gpa' ]
        labels = {
            'student_number': 'Student Number',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email' : 'Email', 
            'field_of_study': 'Field of Study',
            'gpa': 'GPA',
        }
        widgets = {
            'student_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'first_name':forms.TextInput(attrs={'class': 'form-control'}),
            'last_name':forms.TextInput(attrs={'class': 'form-control'}),
            'email' :forms.EmailInput(attrs={'class': 'form-control'}),
            'field_of_study':forms.TextInput(attrs={'class': 'form-control'}),
            'gpa':forms.NumberInput(attrs={'class': 'form-control'}),
        }