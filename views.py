from django.shortcuts import render,HttpResponse
from.forms import LoginForm



# Create your views here.
def home(request):
    #return HttpResponse('Hello')
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            username=request.POST['username']
            password=request.POST['password']
        return render(request,'contact.html',{'username','password'})
    else:
        return render(request,'contact.html',{})
