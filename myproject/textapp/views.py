from django.shortcuts import render

from django.http import HttpResponse
from .models import TextRecord

def add_record(request):
    record = TextRecord(content="Hello from /add endpoint")
    record.save()
    return HttpResponse("Record successfully added to the database.")


def show_records(request):
    records = TextRecord.objects.all()
    output = '<h1>Text Records</h1><ul>'
    for record in records:
        output += f'<li>{record.content}</li>'
    output += '</ul>'
    return HttpResponse(output)
