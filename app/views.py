from django.shortcuts import render

# Create your views here.
def india(request):
    return render(request,'india.html')

def form(request):
    return render(request,'form.html')

def table1(request):
    return render(request,'table1.html')