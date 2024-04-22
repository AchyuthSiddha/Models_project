from django.shortcuts import render

# Create your views here.
from app.models import Employee

def Emp_info(request):
    emp_list=Employee.objects.all()
    d={'emp_list':emp_list}
    return render(request,'index.html',d)