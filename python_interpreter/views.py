from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def python_interpreter(request):
    return render(request, 'interpreter.html')