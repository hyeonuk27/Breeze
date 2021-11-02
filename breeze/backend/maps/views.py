from django.http.response import JsonResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib import auth

from decouple import config

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

import requests


REST_API_KEY = config('REST_API_KEY')
User = get_user_model()


@api_view(['POST'])
def get_middle(request):
    # 중간 지점 찾기 알고리즘


    # 중간 지점 찾고 사용자가 중간 지점으로 오는 경로 제공
    headers = {
        'Authorization': 'KakaoAK {REST_API_KEY}',
    }

    params = (
        ('origin', '127.11015314141542,37.39472714688412'),
        ('destination', '127.10824367964793,37.401937080111644'),
        ('waypoints', ''),
        ('priority', 'RECOMMEND'),
        ('car_fuel', 'GASOLINE'),
        ('car_hipass', 'false'),
        ('alternatives', 'false'),
        ('road_details', 'false'),
    )

    response = requests.get('https://apis-navi.kakaomobility.com/v1/directions', headers=headers, params=params)


@api_view(['POST'])
def get_store(request):
    pass