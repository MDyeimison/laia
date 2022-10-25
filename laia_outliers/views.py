from django.shortcuts import render
from django.http import HttpResponse
from laia_outliers.forms import FileForm
# from FileForm import FileForm filename
from laia_outliers.functions import handle_uploaded_file  

def index(request):
    file_form = FileForm(request.POST, request.FILES)  
    if file_form.is_valid():  
        handle_uploaded_file(request.FILES['file'])
    # file_name = filename()  
    return render(request,"laia_outliers/index.html",{'form':file_form})    

def dashboard(request):
    # file_name = filename()  
    return render(request, "laia_outliers/dashboard.html", {'name':file_name})

def about(request):
    return render(request, "laia_outliers/about.html")

