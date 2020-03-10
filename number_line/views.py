from django.shortcuts import render
from django.http import HttpResponse


# plan is to create a single page application using below ideas

def blank_line(request):
    return render(request, 'blank_line.html')

def line_with_ticks(request):
    return render(request, 'line_with_ticks.html')

def line_with_two_ticks(request):
    return render(request, 'line_with_two_ticks.html')

def base(request):
    return render(request, 'base.html')

def number_line(request):
    return HttpResponse('This page will contain a number line...')


