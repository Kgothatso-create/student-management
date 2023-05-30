from django.shortcuts import render
from .models import Student
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import StudentForm 

# Create your views here.
def index(request):
    # Render the index.html template and pass the students queryset to it
    return render(request, 'students/index.html', {'students': Student.objects.all()})

def view_student(request, id):
    # Retrieve the student with the given id from the database
    student = Student.objects.get(pk=id)
    # Redirect to the index view
    return HttpResponseRedirect(reverse('index'))

def add(request):
  if request.method == 'POST':
    form = StudentForm(request.POST)
    if form.is_valid():
      # Extract the cleaned data from the form
      new_student_number = form.cleaned_data['student_number']
      new_first_name = form.cleaned_data['first_name']
      new_last_name = form.cleaned_data['last_name']
      new_email = form.cleaned_data['email']
      new_field_of_study = form.cleaned_data['field_of_study']
      new_gpa = form.cleaned_data['gpa']

      # Create a new student instance with the extracted data
      new_student = Student(
        student_number=new_student_number,
        first_name=new_first_name,
        last_name=new_last_name,
        email=new_email,
        field_of_study=new_field_of_study,
        gpa=new_gpa
      )
      # Save the new student to the database
      new_student.save()
      # Render the add.html template with a new form and success flag
      return render(request, 'students/add.html', {
        'form': StudentForm(),
        'success': True
      })
  else:
    form = StudentForm()
  return render(request, 'students/add.html', {
    'form': StudentForm()
  })

def edit(request, id):
   if request.method == 'POST':
      student = Student.objects.get(pk=id)
      form = StudentForm(request.POST, instance=student)
      if form.is_valid():
         # Save the updated form data to the existing student instance
         form.save()
         # Render the edit.html template with the updated form and success flag
         return render (request, 'students/edit.html', {'form': form, 'success': True})
   else:
      student = Student.objects.get(pk=id)  
      form = StudentForm(instance=student)
      # Render the edit.html template with the form pre-filled with existing student data
      return render(request, 'students/edit.html', {'form': form})
   
def delete(request, id):
    if request.method == 'POST':
      # Retrieve the student with the given id from the database
      student = Student.objects.get(pk=id)
      # Delete the student from the database
      student.delete()
      # Redirect to the index view
    return HttpResponseRedirect(reverse('index'))