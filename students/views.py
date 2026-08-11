from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def all_students(request):
    students=[{'id':1, 'name': 'neer', 'age':29}]
    return HttpResponse(students)