from rest_framework import serializers
from .models import Appointment, Appointmentplace, Participant


class AppointmentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'


class AppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        fields = '__all__'


class AppointmentplaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointmentplace
        fields = '__all__'


class ParticipantSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Participant
        fields = '__all__'