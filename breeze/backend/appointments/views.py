from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from .serializers import AppointmentSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def appointment(request):
    pass


@api_view(['GET', 'DELETE'])
def appointment_note(request):
    pass


@api_view(['GET'])
def appointment_list(request):
    pass
