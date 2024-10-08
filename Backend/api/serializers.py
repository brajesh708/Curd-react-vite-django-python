from rest_framework import serializers
from .models import EmployeeData

class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model=EmployeeData
        fields =["id","EmpNo","EmpName","Designation","Salary"]