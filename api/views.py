from students.models import Student
from employees.models import Employee
from .serializers import StudentSerializer, EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import mixins, generics, viewsets
from django.shortcuts import get_object_or_404
from .paginations import CustomPagination
from employees.filters import EmployeeFilter

# ------------------------------------------ Function based views -------------------------------------#
@api_view(['GET', 'POST'])
def studentView(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def studentDetailView(request, id):
    try:
        student = Student.objects.get(pk=id)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ------------------------------------------ Class based views -------------------------------------#
# class Employees(APIView):
#     def get(self, request):
#         try:
#             employees = Employee.objects.all()
#             serializer = EmployeeSerializer(employees, many=True)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         except:
#             return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#     def post(self, request):
#         try:
#             serializer = EmployeeSerializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             return Response(status=status.HTTP_400_BAD_REQUEST)
#         except:
#             return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# class EmployeeDetail(APIView):
    # def get_object(self, id):
    #     try:
    #         return Employee.objects.get(pk=id)
    #     except Employee.DoesNotExist:
    #         raise Http404

    # def get(self, request, id):
    #     employee = self.get_object(id)
    #     serializer = EmployeeSerializer(employee)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    # def put(self, request, id):
    #     employee = self.get_object(id)
    #     serializer = EmployeeSerializer(employee, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, id):
    #     employee = self.get_object(id)
    #     employee.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

# ------------------------------------------ Mixin based views -------------------------------------#

# class Employees(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

#     def get(self, request):
#         return self.list(request)

#     def post(self, request):
#         return self.create(request) 

# class EmployeeDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,  generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     lookup_field="id"

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
    
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

# ------------------------------------------ Generic views -------------------------------------#

# class Employees(generics.ListCreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     lookup_field="id"

# class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     lookup_field="id"

# ------------------------------------------ View Sets -------------------------------------#
# class EmployeeViewSet(viewsets.ViewSet):
#     lookup_field='id'

#     def list(self, request):
#         queryset = Employee.objects.all()
#         serializer = EmployeeSerializer(queryset, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def create(self, request):
#         serializer = EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     def retrieve(self, request, id):
#         employee = get_object_or_404(Employee, pk=id)
#         serializer = EmployeeSerializer(employee)
#         return Response(serializer.data)

#     def update(self, request, id):
#         employee = get_object_or_404(Employee, pk=id)
#         serializer = EmployeeSerializer(employee, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, id):
#         employee = get_object_or_404(Employee, pk=id)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# ------------------------------------------ Model View Sets -------------------------------------#

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('id')
    serializer_class = EmployeeSerializer
    pagination_class = CustomPagination
    filterset_class = EmployeeFilter