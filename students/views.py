from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_http_methods
import json
from .models import Student, University
@api_view(['POST'])
def add_student(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "New student is added"})
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def get_all_students(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)



from rest_framework import generics
from .models import University      # ✅ THIS LINE IS VERY IMPORTANT
from .serializers import UniversitySerializer

class UniversityCreateView(generics.CreateAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer

class UniversityListView(generics.ListAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer



@csrf_exempt
@require_http_methods(["POST"])
def add_university(request):
    data = json.loads(request.body)
    name = data.get('name')
    uni = University.objects.create(name=name)
    return JsonResponse({'id': uni.id, 'name': uni.name})


def get_all_universities(request):
    universities = list(University.objects.values())
    return JsonResponse(universities, safe=False)
