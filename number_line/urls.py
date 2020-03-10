from django.urls import path
from . import views

urlpatterns = [
    path('', views.number_line, name='number_line'),
    path('blank_line', views.blank_line, name='blank_line'),
    path('line_with_ticks', views.line_with_ticks, name='line_with_ticks'),
    path('base', views.base, name='base'),
]