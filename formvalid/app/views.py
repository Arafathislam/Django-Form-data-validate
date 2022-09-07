from django.shortcuts import render
from .form import StudentRegistration

# Create your views here.

def showformdata(request):

    if request.method == 'POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
        #   print('Name: ',fm.cleaned_data['name'])
            name=request.POST['name']
            # name=fm.cleaned_data['name']
            email=request.POST['email']
            # email=fm.cleaned_data['email']
            print("Name: ",name,"\n","Email: ",email)
    else:
        fm=StudentRegistration()

    return render(request,'app/index.html',{'form':fm})