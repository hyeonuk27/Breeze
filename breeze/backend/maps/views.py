from django.http.response import JsonResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib import auth

from decouple import config
from accounts.utils import check_login
from .models import Place
from .serializers import PlaceListSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from shapely.geometry import Polygon
import numpy as np
import pandas as pd
import requests
import random
import json

REST_API_KEY = config('REST_API_KEY')
KAKAO_KEY = config('KAKAO_KEY')
User = get_user_model()

@api_view(['POST'])
@check_login
def get_middle(request):
    passenger = pd.read_csv('data/passenger.csv')
    middle_place_type = request.data['middle_place_type']
    participants_info = request.data['participants']
    participants_loc = []

    for participant in participants_info:
        participants_loc.append([float(participant.get('partLatitude')), float(participant.get('partLongitude'))])
    
    if len(participants_loc) >= 3:
        P = Polygon(participants_loc)
        center = P.centroid
        diff = []
        for lat, long in zip(passenger['latitude'], passenger['longitude']):
            diff.append(abs(lat - center.x) + abs(long - center.y)) 
        passenger['diff'] = diff
        subway_list = passenger.sort_values('diff')[:20]

        dis = []
        for lat, long in zip(subway_list['latitude'], subway_list['longitude']):
            dis.append(np.sqrt((float(lat) - center.x)**2 + (float(long) - center.y)**2))
        subway_list['dis'] = dis
        final_subway = subway_list.sort_values('dis')[:10]
        final_subway = final_subway.drop(['diff'], axis=1)
        final_subway = final_subway.drop(['id'], axis=1)
    else:
        x, y = [], []
        for participant in participants_loc:
            x.append(participant[0])
            y.append(participant[1])
        center = [sum(x) / 2, sum(y) / 2]

        diff = []
        for lat, long in zip(passenger['latitude'], passenger['longitude']):
            diff.append(abs(lat - center[0]) + abs(long - center[1])) 
        passenger['diff'] = diff
        subway_list = passenger.sort_values('diff')[:20]

        dis = []
        for lat, long in zip(subway_list['latitude'], subway_list['longitude']):
            dis.append(np.sqrt((float(lat) - center[0])**2 + (float(long) - center[1])**2))
        subway_list['dis'] = dis
        final_subway = subway_list.sort_values('dis')[:10]
        final_subway = final_subway.drop(['diff'], axis=1)
        final_subway = final_subway.drop(['id'], axis=1)

    middle_data = []

    if middle_place_type == 0:
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
    elif middle_place_type == 1:
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
        else:
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
    
    time_min = 0
    guides_list = []
    response = requests.get('https://apis-navi.kakaomobility.com/v1/directions', headers=headers, params=params).json()
    try:
        time_sec = response.get('routes')[0].get('summary').get('duration')
        time_min = round(time_sec/60)
    except TypeError as e:
        print(e)
    except AttributeError as e:
        print(e)
        
    try:
        guides_list = response.get('routes')[0].get('sections')[0].get('guides')
    except TypeError as e:
        print(e)
    except AttributeError as e:
        print(e)
    
    return (time_min, guides_list)


@api_view(['POST'])
@check_login
def get_store(request, category_id, filter_id):
    category_store = Place.objects.filter(middle_name=request.data['middlePlace'], category_num=category_id)

    if len(category_store) < 21:
        stores = category_store
    else:
        if filter_id == 0:
            stores = category_store.order_by('-review')[:20]
        elif filter_id == 1:
            stores = category_store.order_by('-rate')[:20]
        elif filter_id == 2:
            category_store = list(category_store)
            random.shuffle(category_store)
            stores = category_store[:20]
    
    store_data = []
    for store in stores:
        serializer = PlaceListSerializer(store)
        store_data.append(serializer.data)

    data = {
        'access_token': request.access_token,
        'stores': store_data
    }

    return Response(data, status=status.HTTP_201_CREATED)