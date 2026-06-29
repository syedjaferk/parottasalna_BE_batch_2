import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Student

# Create your views here.


@csrf_exempt
def students(request):
    if request.method == "GET":
        students = Student.objects.all()

        data = []
        for student in students:
            data.append(
                {
                    "id": student.id,
                    "name": student.name,
                    "age": student.age,
                    "department": student.department,
                }
            )
        return JsonResponse(data, safe=False)

    elif request.method == "POST":
        body = json.loads(request.body)
        student = Student.objects.create(
            name=body["name"], age=body["age"], department=body["department"]
        )

        return JsonResponse(
            {
                "id": student.id,
                "name": student.name,
                "age": student.age,
                "department": student.department,
            },
            status=201,
        )

    return JsonResponse({"error": "Method Not allowed"}, status=405)
