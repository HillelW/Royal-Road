from django.urls import path
from . import views

urlpatterns = [
    path('', views.python_interpreter, name='python_interpreter'),
    path('python_interpreter', views.python_interpreter, name='python_interpreter')
]