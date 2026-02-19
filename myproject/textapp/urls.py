from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_record, name='add_record'),
    path('show/', views.show_records, name='show_records'),
]