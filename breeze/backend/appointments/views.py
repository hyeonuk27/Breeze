from os import stat
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth import get_user_model
from .serializers import AppointmentSerializer, AppointmentplaceSerializer, ParticipantSerializer
from .models import Appointment, Appointmentplace, Participant
from accounts.utils import check_login

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

import datetime
# import crypto
# import sys
# sys.modules['Crypto'] = crypto

# import base64
# from Crypto import Random
# from Crypto.Cipher import AES


User = get_user_model()

@api_view(['POST'])
@check_login
def appointment(request):
    user = get_object_or_404(User, id=request.user.id)
    # 쪽지 저장
    note_data = {
        'datetime': request.data['dateTime'],
        'middle_place': request.data['middlePlace'],
    }
    sereializer = AppointmentSerializer(data=note_data, partial=True)
    if sereializer.is_valid(raise_exception=True):
        sereializer.save(user=user)
    
    # 약속장소 저장
    note_id = sereializer.data.get('id')
    appointment = get_object_or_404(Appointment, id=note_id)
    
    for place in request.data['places']:
        place_data = {
            'name': place['placeName'],
            'category': place['placeCategory'],
            'url': place['placeUrl'],
        }
        sereializer = AppointmentplaceSerializer(data=place_data, partial=True)
        if sereializer.is_valid(raise_exception=True):
            sereializer.save(appointment=appointment)

    # 참가자 저장
    for paricipant in request.data['participants']:
        paricipant_data = {
            'name': paricipant['partName'],
            'time': paricipant['time'],
            'barami_type': paricipant['baramiType'],
        }
        sereializer = ParticipantSerializer(data=paricipant_data, partial=True)
        if sereializer.is_valid(raise_exception=True):
            sereializer.save(appointment=appointment)

    # node_id 암호화하여 보내기
    secret_code = AESCipher(bytes(key)).encrypt(str(note_id))  

        
    data = { 
        'access_token': request.access_token,
        'note_id': note_id,
        'secret_code': secret_code,
    }
    return Response(data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def appointment_note(request, secret_code):
    note_id = AESCipher(bytes(key)).decrypt(secret_code).decode('utf-8')
    note = get_object_or_404(Appointment, id=note_id)
    places = get_list_or_404(Appointmentplace, appointment_id=note_id)
    participants = get_list_or_404(Participant, appointment_id=note_id)
    
    place_data = []
    for place in places:
        serializer = AppointmentplaceSerializer(place)
        place_data.append(serializer.data)
    
    participant_data = []
    for participant in participants:
            serializer = ParticipantSerializer(participant)
            participant_data.append(serializer.data)

    data = {
        'datetime': note.datetime,
        'middle_place': note.middle_place,
        'places': place_data,
        'participants': participant_data,
    }
    
    return Response(data, status=status.HTTP_200_OK)


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
    # 이미 디데이 지난 약속 지우고 시작
    now = datetime.datetime.now()
    prevs = Appointment.objects.filter(datetime__lt=now)
    for prev in prevs:
        prev.delete()

    appointments = Appointment.objects.filter(user_id=request.user.id)
    appointment_data = []
    for appointment in appointments:
        # 디데이 구하기
        d_day = (now - appointment.datetime).days
        appointment_data.append({
            'appointment_id': appointment.id,
            'datetime': appointment.datetime,
            'middle_place': appointment.middle_place,
            'd_day': d_day,
        })

    data = {
        'access_token': request.access_token,
        'my_appointment': appointment_data,
    }

    return Response(data, status=status.HTTP_200_OK)


key = [0x10, 0x01, 0x15, 0x1B, 0xA1, 0x11, 0x57, 0x72, 0x6C, 0x21, 0x56, 0x57, 0x62, 0x16, 0x05, 0x3D,
           0xFF, 0xFE, 0x11, 0x1B, 0x21, 0x31, 0x57, 0x72, 0x6B, 0x21, 0xA6, 0xA7, 0x6E, 0xE6, 0xE5, 0x3F]

class AESCipher:
    def __init__( self, key ):
        self.key = key

    def encrypt( self, raw ):
        BS = 16
        pad = lambda s: s + (BS - len(s.encode('utf-8')) % BS) * chr(BS - len(s.encode('utf-8')) % BS)
        raw = pad(raw)
        iv = Random.new().read( AES.block_size )
        cipher = AES.new( self.key, AES.MODE_CBC, iv )
        return base64.b64encode( iv + cipher.encrypt( raw.encode('utf-8') ) )

    def decrypt( self, enc ):
        unpad = lambda s : s[:-ord(s[len(s)-1:])]
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv )
        return unpad(cipher.decrypt( enc[16:]))