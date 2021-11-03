from django.http.response import JsonResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib import auth

from decouple import config

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from shapely.geometry import Polygon
import numpy as np
import pandas as pd
import requests


REST_API_KEY = config('REST_API_KEY')
User = get_user_model()


@api_view(['GET'])
def get_middle(request):
    subway = pd.read_csv('data/subway.csv')
    print(subway.columns)
    user1 = [37.52, 126.88]
    user2 = [37.68, 127.06]
    user3 = [37.53, 126.96]

    # 중간 지점 찾기
    # 연산 줄이기가 필요하다면 그라함 스캔 알고리즘
    P = Polygon([user1, user2, user3])
    center = P.centroid

    # 위도 기준으로 차이가 적은 후보 역들 추리기
    diff = []
    for lat in subway['latitude']:
        diff.append(abs(lat - center.x)) 
    subway['diff'] = diff
    subway_list = subway.sort_values('diff')[:20]

    # 후보 역들과 중간 지점의 거리 구하기
    dis = []
    for lat, long in zip(subway_list['latitude'], subway_list['longitude']):
        print(lat, long)
        dis.append(np.sqrt((float(lat) - center.x)**2 + (float(long) - center.y)**2))
    subway_list['dis'] = dis
    final_subway = subway_list.sort_values('dis')[:10]
    final_subway = final_subway.drop(['diff'], axis=1)

    name, latitude, longitude = '', '' ,''
    # 완벽한 중간: 중간 지점에서 거리차가 제일 적은 지하철 역
    if request.middle_place_type == '완벽한 중간':
        name = final_subway[0]['name']
        latitude = final_subway[0]['latitude']
        longitude = final_subway[0]['longitude']
    # 핫플레이스: 지하철 승하차승객수가 가장 많은 역
    elif request.middle_place_type == '핫플레이스':
        name = final_subway[0]
        latitude = final_subway[0]
        longitude = final_subway[0]
    # 코로나멈춰: 지하철 승하차승객수가 가장 적은 역
    else:
        name = final_subway[0]
        latitude = final_subway[0]
        longitude = final_subway[0]

    # 중간 지점 찾고 사용자가 중간 지점으로 오는 경로 제공
    headers = {
        'Authorization': 'KakaoAK {REST_API_KEY}',
    }

    params = (
        ('origin', '127.11015314141542, 37.39472714688412'),
        ('destination', f'{longitude}, {latitude}'),
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