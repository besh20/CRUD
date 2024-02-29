from django.shortcuts import render
# from django.http import HttpResponseRedirect
# from django.urls import reverse  
from .models import *
from .forms import *

# Create your views here.
def home(request):
    stud = student.objects.all()
    stud_info = {
        'stud': stud,
    }
    return render(request, "index.html", stud_info)

def view_info(request, id):
    stud = student.objects.get(id=id)
    view_info = {
        'id': id,
        'stud': stud
    }
    return render (request, "index.html",view_info)
    # return HttpResponseRedirect(reverse('index'))

def add(request):
    if request.method == 'POST':
        form = studForm(request.POST)
        if form.is_valid():
            new_sid = form.cleaned_data['sid']
            new_first_name = form.cleaned_data['first_name']
            new_last_name = form.cleaned_data['last_name']
            new_batch = form.cleaned_data['batch']
            new_email = form.cleaned_data['email']
            new_grade = form.cleaned_data['grade']

            new_stud = student(
                sid=new_sid,
                first_name=new_first_name,
                last_name=new_last_name,
                batch=new_batch,
                email=new_email,
                grade=new_grade
            )
            new_stud.save()

            return render(request, 'add.html', {
                'form': studForm(), 
                'success': True
            })
    else:  
        form = studForm()

    
    return render(request, 'add.html', {
        'form': studForm()  # Pass the form instance back to the template
    })

def update(request, id):
    if request.method == 'POST':
      stud = student.objects.get(id=id)
      form = studForm(request.POST, instance =stud)
      if form.is_valid():
          form.save()
          return render(request, 'update.html',{
             'form': form,
             'success': True 
          })
    else:
        stud = student.objects.get(id=id)
        form = studForm(instance =stud)
    return render(request, 'update.html',{
        'form': form
    })

def delete(request, id):
    if request.method == 'POST':
        stud = student.objects.get(id=id)
        stud.delete()
    return render (request, "index.html")






