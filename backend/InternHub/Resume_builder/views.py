from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view, schema
from rest_framework.response import Response
from rest_framework import status
from .models import Resume_model
from .serializer import *
from .util_ai import SkillPrediction
import json


# Create your views here.

@api_view(['GET'])
def get_resume(request, id):
    resume_obj = Resume_model.objects.filter(id=id).first()
    if not resume_obj:
        return Response('No data found!', status=status.HTTP_404_NOT_FOUND)
    serializer = ResumeSerializer(resume_obj)
    return Response(serializer.data)
    


@api_view(['POST'])
def create_resume(request):
    data = ResumeSerializer(data=request.data)
    if data.is_valid():
        data.save()
        return Response("Data Saved Successfully!", status.HTTP_201_CREATED)
    else:
        print(data)
        return Response("Invalid Format", status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_resume(request, id):
    check = Resume_model.objects.check(id=id)
    if check:
        data = ResumeSerializer(data=request.data)
        if data.is_valid():
            data.update()
            return Response("Data Updated Successfully!", status.HTTP_200_OK)
        else:
            return Response("Invalid Schema!", status.HTTP_400_BAD_REQUEST)
    else:
        return Response("Data Does Not Exists!", status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_resume(request, id):
    check = Resume_model.objects.check(id=id)
    if check:
        Resume_model.objects.filter(id=id).delete()
        return Response("Deleted Successfully!", status.HTTP_200_OK)
    else:
        return Response("Data Not Found!", status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def predict_skills(request, id):
    data = Resume_model.objects.filter(id=id).values("skills", 'role').first()

    if not data:
        return Response(f"Data Not Found for ID-{id}", status.HTTP_404_NOT_FOUND)

    skills = SkillSerializer(data=data)
    if skills.is_valid():
        skills_list = skills.validated_data
        prediction_class = SkillPrediction(skills_list['skills'], skills_list['role'])
        predictions = list(prediction_class.make_prediction())
        response = {"predictions": predictions}
        return Response(response)

    return Response("Success", status.HTTP_200_OK)
