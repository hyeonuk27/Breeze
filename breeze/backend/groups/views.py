from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def group_create(request):
    pass


@api_view(['GET'])
def groups(request):
    pass


@api_view(['DELETE'])
def group_delete(request):
    pass