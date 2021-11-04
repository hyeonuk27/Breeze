from os import stat
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from .serializers import AppointmentSerializer
from .models import Appointment
from accounts.utils import check_login

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
@check_login
def appointment(request):
    pass


@api_view(['GET'])
def appointment_note(request, note_id):
    pass


@api_view(['DELETE'])
@check_login
def appointment_mynote(request, note_id):
    note = get_object_or_404(Appointment, id=note_id)
    if request.user == note.user:
        note.delete()
        data = { 'access_token': request.access_token }
        return Response(data, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@check_login
def appointment_list(request):
    pass
