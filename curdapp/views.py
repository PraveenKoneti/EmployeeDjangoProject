from django.shortcuts import render, redirect,HttpResponse
from .models import Employeedata
import random


def homepage(request):
    employees= Employeedata.objects.all()
    return render(request, 'homepage.html',{'employees':employees})

def generate_employee_id():
    prefix = 'e'
    suffix = str(random.randint(1, 100))
    employee_id = prefix + suffix
    return employee_id

# Example usage
unique_employee_id = generate_employee_id()
print(unique_employee_id)

def add_employees(request):
    error_message = ''  # Initialize the error message
    unique_employee_id = generate_employee_id()
    if request.method == "POST":
        email = request.POST.get('email')
        fname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        mobile = request.POST.get('mobile')
        location = request.POST.get('location')

        if not email:
            error_message = 'Email is required.'
        elif not fname:
            error_message = 'First Name is required.'
        elif not lastname:
            error_message = 'Last Name is required.'
        elif not mobile:
            error_message = 'Mobile No is required.'
        elif not location:
            error_message = 'Location is required.'
        else:
            # unique_employee_id = str(uuid.uuid4())[:8]  # Generate a unique ID
            Employeedata(
                employee_id=unique_employee_id,
                first_name=request.POST.get('fname'),
                last_name=request.POST.get('lname'),
                Emailid=request.POST.get('email'),
                Mobile=request.POST.get('mobile'),
                location=request.POST.get('location'),
            ).save()
            return redirect('homepage')
    
    elif request.method == "GET":
        return render(request, 'add_employees.html')

    return render(request, 'add_employees.html')  # Render the form again in case of errors 
 

def update_employees(request, id):
    employees=Employeedata.objects.get(id=id)
    if request.method =="GET":
            return render(request, 'update_employees.html',{'employees':employees})
    else:
       employees.first_name=request.POST.get('fname')
       employees.last_name=request.POST.get('lname')
       employees.Emailid=request.POST.get('email')
       employees.Mobile=request.POST.get('mobile')
       employees.location=request.POST.get('location')
       employees.save()
       return redirect('homepage')

def delete_employees(request, id):
    employees=Employeedata.objects.get(id=id)
    employees.delete()
    return redirect('homepage')



