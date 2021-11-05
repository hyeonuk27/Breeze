from os import stat
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from .serializers import AppointmentSerializer
from .models import Appointment
from accounts.utils import check_login

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

import datetime

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
    # 이미 디데이 지난 약속 지우기로???

    appointments = Appointment.objects.filter(user_id=request.user.id)

    appointment_data = []
    for appointment in appointments:
        # 디데이 구하기 -- string으로 넘기는게 편한가요?!

        appointment_data.append({
            'appointment_id': appointment.id,
            'datetime': appointment.datetime,
            'middle_place': appointment.middle_place,
            'd_day': 0,
        })

    data = {
        'access_token': request.access_token,
        'my_appointment': appointment_data,
    }

    return Response(data, status=status.HTTP_200_OK)
