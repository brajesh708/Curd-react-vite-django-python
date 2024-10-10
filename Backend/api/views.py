from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
import io

# Create your views here.
class Employeeviewset(viewsets.ModelViewSet):
    queryset = EmployeeData.objects.all()
    serializer_class = EmployeeSerializers