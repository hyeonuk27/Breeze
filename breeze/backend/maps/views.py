from django.http.response import JsonResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib import auth

from decouple import config
from accounts.utils import check_login

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from shapely.geometry import Polygon
import numpy as np
import pandas as pd
import requests


REST_API_KEY = config('REST_API_KEY')
User = get_user_model()


@api_view(['POST'])
@check_login
def get_middle(request):
    passenger = pd.read_csv('data/passenger.csv')
    participants_info = request.data # 프론트로부터 받는 참여자 정보
    participants_loc = [] # 참여자 좌표 모음

    for participant in participants_info:
        participants_loc.append([float(participant.get('partLatitude')), float(participant.get('partLongitude'))])
    
    # 중간 지점 찾기 (연산 줄이기가 필요하다면 그라함 스캔 알고리즘)
    if len(participants_loc) >= 3:
        P = Polygon(participants_loc)
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
    else:
        center = [sum(list(map(lambda x: x[0], participants_loc))) / 2, sum(list(map(lambda x: x[1], participants_loc))) / 2]
        # 위도 기준으로 차이가 적은 후보 역들 추리기
        diff = []
        for lat in passenger['latitude']:
            diff.append(abs(lat - center[0])) 
        passenger['diff'] = diff
        subway_list = passenger.sort_values('diff')[:20]
        # 후보 역들과 중간 지점의 거리 구하기
        dis = []
        for lat, long in zip(subway_list['latitude'], subway_list['longitude']):
            dis.append(np.sqrt((float(lat) - center[0])**2 + (float(long) - center[1])**2))
        subway_list['dis'] = dis
        final_subway = subway_list.sort_values('dis')[:10]
        final_subway = final_subway.drop(['diff'], axis=1)
        final_subway = final_subway.drop(['id'], axis=1)
        print(final_subway)

    middle_data = []

    # mode1 = 0 완벽한 중간: 중간 지점에서 거리차가 제일 적은 지하철 역
    for i in range(3):
        subway = final_subway.iloc[i]
        name = subway['name']
        latitude = subway['latitude']
        longitude = subway['longitude']
        participants = []
        for participant in participants_info:
            time, guides_list = get_time(longitude, latitude, participant)
            route = []
            for guide in guides_list:
                route.append([guide.get('y'), guide.get('x')])
                
            participants.append({
                'barami_type': participant['baramiType'],
                'time': time,
                'route': route
            })
        
        middle_data.append({
            'middle_place_type': 0,
            'name': name,
            'latitude': latitude,
            'longitude': longitude,
            'participants': participants,
        })

    # mode1 = 1 핫플레이스: 지하철 승하차승객수가 가장 많은 역
    for i in range(3):
        subway = subway_list.sort_values('passenger', ascending=False).iloc[i]
        name = subway['name']
        latitude = subway['latitude']
        longitude = subway['longitude']
        participants = []
        for participant in participants_info:
            time, guides_list = get_time(longitude, latitude, participant)
            route = []
            for guide in guides_list:
                route.append([guide.get('y'), guide.get('x')])
                
            participants.append({
                'barami_type': participant['baramiType'],
                'time': time,
                'route': route
            })
        
        middle_data.append({
            'middle_place_type': 1,
            'name': name,
            'latitude': latitude,
            'longitude': longitude,
            'participants': participants,
        })
    
    # mode1 = 2 코로나멈춰: 지하철 승하차승객수가 가장 적은 역
    for i in range(3):
        subway = subway_list.sort_values('passenger').iloc[i]
        name = subway['name']
        latitude = subway['latitude']
        longitude = subway['longitude']
        participants = []
        for participant in participants_info:
            time, guides_list = get_time(longitude, latitude, participant)
            route = []
            for guide in guides_list:
                route.append([guide.get('y'), guide.get('x')])
                
            participants.append({
                'barami_type': participant['baramiType'],
                'time': time,
                'route': route
            })
        
        middle_data.append({
            'middle_place_type': 2,
            'name': name,
            'latitude': latitude,
            'longitude': longitude,
            'participants': participants,
        })

    data = {
        'access_token': request.access_token,
        'middle_data': middle_data,
    }
    return Response(data, status=status.HTTP_201_CREATED)


# 중간 지점 찾고 사용자가 중간 지점으로 오는 시간과 경로 가져오는 함수
def get_time(longitude, latitude, participant):
    participant_lat = participant.get('partLatitude')
    participant_long = participant.get('partLongitude')

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
    time_sec = response.get('routes')[0].get('summary').get('duration')
    time_min = round(time_sec/60)
    
    guides_list = response.get('routes')[0].get('sections')[0].get('guides')
        
    return (time_min, guides_list)


@api_view(['POST'])
def get_store(request):
    pass