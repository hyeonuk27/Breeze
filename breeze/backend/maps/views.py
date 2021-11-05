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
    passenger = pd.read_csv('data/passenger.csv')
    participants = request.data.get('participants')
    # participants = [[37.52, 126.88], [37.68, 127.06], [37.53, 126.96]]
    
    # 중간 지점 찾기 (연산 줄이기가 필요하다면 그라함 스캔 알고리즘)
    P = Polygon(participants)
    center = P.centroid

    # 위도 기준으로 차이가 적은 후보 역들 추리기
    diff = []
    for lat in passenger['latitude']:
        diff.append(abs(lat - center.x)) 
    passenger['diff'] = diff
    subway_list = passenger.sort_values('diff')[:20]

    # 후보 역들과 중간 지점의 거리 구하기
    dis = []
    for lat, long in zip(subway_list['latitude'], subway_list['longitude']):
        dis.append(np.sqrt((float(lat) - center.x)**2 + (float(long) - center.y)**2))
    subway_list['dis'] = dis
    final_subway = subway_list.sort_values('dis')[:10]
    final_subway = final_subway.drop(['diff'], axis=1)
    final_subway = final_subway.drop(['id'], axis=1)
    print(final_subway)

    mode1 = request.data.get('mode1')
    name, latitude, longitude = '', '' ,''
    # 완벽한 중간: 중간 지점에서 거리차가 제일 적은 지하철 역
    if mode1 == 0:
        subway = final_subway.iloc[0]
        name = subway['name']
        latitude = subway['latitude']
        longitude = subway['longitude']
        print(subway)
    # 핫플레이스: 지하철 승하차승객수가 가장 많은 역
    elif mode1 == 1:
        subway = subway_list.sort_values('passenger', ascending=False).iloc[0]
        name = subway['name']
        latitude = subway['latitude']
        longitude = subway['longitude']
    # 코로나멈춰: 지하철 승하차승객수가 가장 적은 역
    else:
        subway = subway_list.sort_values('passenger').iloc[0]
        name = subway['name']
        latitude = subway['latitude']
        longitude = subway['longitude']

    
    # 중간 지점 찾고 사용자가 중간 지점으로 오는 거리와 시간
    participant_info_list = []
    for participant in participants:
        participant_lat = participant.get('partLatitude ')
        participant_long = participant.get('partLongitude ')

        headers = {
        'Authorization': f'KakaoAK {REST_API_KEY}',
        }

        params = (
            ('origin', f'{participant_long},{participant_lat}'),
            ('destination', f'{longitude},{latitude}'),
            ('waypoints', ''),
            ('priority', 'RECOMMEND'),
            ('car_fuel', 'GASOLINE'),
            ('car_hipass', 'false'),
            ('alternatives', 'false'),
            ('road_details', 'false'),
        )

        response = requests.get('https://apis-navi.kakaomobility.com/v1/directions', headers=headers, params=params).json()
        time_min = response.get('routes')[0].get('summary').get('duration')
        time_sec = round(time_min/60)
        participant_info = [{
            'barami_type': participant.get('baramiType'),
            'time': time_sec,
        }]
        participant_info_list.append(participant_info)

    middle_data = [{
        'middle_place_type': mode1,
        'name': name,
        'latitude': latitude,
        'longitude': longitude,
        'participants': participants,
    }]

    data = {
        'access_token': request.access_token,
        'middle_data': middle_data,
    }
    return Response(data, status=status.HTTP_200_OK)


@api_view(['POST'])
def get_store(request):
    pass