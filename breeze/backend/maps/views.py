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

import random
import requests
import pickle
import json
import pandas as pd
# from bs4 import BeautifulSoup  
# from urllib.request import urlopen
from selenium import webdriver
import re


KAKAO_KEY = config('KAKAO_KEY')

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
@check_login
def get_store(request, category_id, filter_id):
    # 중간역에 해당하는 가게들 선택, 그 중 해당 카테고리 선택
    category_store = Place.objects.filter(middle_name=request.data['middlePlace'], category_num=category_id)
    
    # 전체 결과가 10개 이하면 다 반환
    if len(category_store) < 11:
        stores = category_store
    else:
        if filter_id == 0:
            # 인기순
            stores = category_store.order_by('review').desc()[:10]
        elif filter_id == 1:
            # 평점순
            stores = category_store.order_by('score').desc()[:10]
        elif filter_id == 2:
            # 랜덤
            random.shuffle(category_store)
            stores = category_store[:10]
    
    data = {
        'access_token': request.access_token,
        'stores': stores
    }
    return Response(data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def store_info(request):
    # 카페 데이터 받아오기
    headers = {
        'Authorization': f'KakaoAK {KAKAO_KEY}',
    }

    # 중간 역 위도 경도 가져와서 역 별 api 요청
    subway_data = pd.read_csv('data/subway.csv', encoding='utf-8')
    data = pd.DataFrame()
    # for c, subway in subway_data.iteritems():
    for index, row in subway_data.iterrows():
        middle_name = row['name']
        middle_latitude = row['latitude']
        middle_longitude = row['longitude']
        
        for i in range(1, 4):
            params = (
                # ('category_group_code', 'FD6'),
                ('category_group_code', 'CE7'),
                ('radius', '1000'),
                ('y', middle_latitude),
                ('x', middle_longitude),
                ('page', i)
            )

            response = requests.get('https://dapi.kakao.com/v2/local/search/category.json', headers=headers, params=params).json()
            documents = response['documents']
            
            stores = []
            for document in documents:
                id = document.get('id')
                name = document.get('place_name')
                address = document.get('road_address_name')
                phone = document.get('phone')
                kakao_url = document.get('place_url')
                latitude = document.get('y')
                longitude = document.get('x')

                # category_num = 0
                category_num = 1
                if '술집' in document.get('category_name') or '호프' in document.get('category_name') or '와인' in document.get('category_name'):
                    continue
                stores.append([id, name, address, phone, kakao_url, latitude, longitude, middle_name, category_num])
            
            df = pd.DataFrame(stores, columns=['id', 'name', 'address', 'phone', 'kakao_url', 'latitude', 'longitude', 'middle_name', 'category_num'])
            data = pd.concat([data, df])
                
            if response['meta']['is_end']:
                break
        print(len(data))
    data.to_csv('data/cafe.csv', index=False)
    # data.to_csv('data/foodie.csv', index=False)
            

def get_alcohol(request):
   
    headers = {
        'Authorization': f'KakaoAK {KAKAO_KEY}',
    }

    data = {
        'query': '술집'
    }

    # 중간 역 위도 경도 가져와서 역 별 api 요청
    subway_data = pd.read_csv('data/subway.csv', encoding='utf-8')
    category_num = 2
    stores = pd.DataFrame()
    # for c, subway in subway_data.iteritems():
    for index, row in subway_data.iterrows():
        middle_name = row['name']
        middle_latitude = row['latitude']
        middle_longitude = row['longitude']
        
        for i in range(1, 4):
            params = (
                ('category_group_code', 'FD6'),
                ('radius', '1000'),
                ('y', middle_latitude),
                ('x', middle_longitude),
                ('page', i)
            )

            response = requests.get('https://dapi.kakao.com/v2/local/search/keyword.json', headers=headers, params=params, data=data).json()
            documents = response['documents']
            
            store = []
            for document in documents:
                id = document.get('id')
                name = document.get('place_name')
                address = document.get('road_address_name')
                phone = document.get('phone')
                kakao_url = document.get('place_url')
                latitude = document.get('y')
                longitude = document.get('x')

                store.append([id, name, address, phone, kakao_url, latitude, longitude, middle_name, category_num])
            
            df = pd.DataFrame(store, columns=['id', 'name', 'address', 'phone', 'kakao_url', 'latitude', 'longitude', 'middle_name', 'category_num'])
            stores = pd.concat([stores, df])
                
            if response['meta']['is_end']:
                break
        print(len(stores))
    stores.to_csv('data/alcohol.csv', index=False)


def data_integration(request):
    cafe = pd.read_csv('data/cafe.csv')
    alcohol = pd.read_csv('data/alcohol.csv')
    foodie = pd.read_csv('data/foodie.csv')

    # null 확인
    print(cafe.isnull().sum())
    print(alcohol.isnull().sum())
    print(foodie.isnull().sum())

    # 데이터 합치기
    store_data = pd.concat([cafe, alcohol, foodie])
    store_data.to_csv('data/store_data.csv', index=False)


from selenium.common.exceptions import NoSuchElementException
import time

def get_rate(request):
    
    num = 48300
    
    while num < 60000:
        print(num)
        auto_crawl(num)
        num += 150
        time.sleep(600)

    # chrome driver 사용: forbidden 문제 해결 필요
    # selenium: hidden으로 표시되는 부분 문제 해결 필요
    # store_data = pd.read_csv('data/store_data.csv')
    # for url in store_data['kakao_url'][:100]:
    #     html = urlopen(url)
    #     soup  = BeautifulSoup(html, "html.parser")
    #     review_list = soup.select('.list_evaluation > li')

    # review_rate = pd.DataFrame({ 'review_cnt': comment_list, 'rate': rate_list})
    # review_rate.to_csv('data/review_rate.csv', index=False)


def auto_crawl(n):
    review_rate = pd.read_csv('data/review_rate.csv')
    store_data = pd.read_csv('data/store_data.csv')

    options = webdriver.ChromeOptions()
    options.add_argument("no-sandbox") 
    options.add_argument("disable-gpu") 
    options.add_argument("--lang=ko_KR") 
    options.add_argument( 'user-agent=Mozilla/5.0 Chrome/95.0.4638.54')
    
    driver = webdriver.Chrome(r"C:\Temp\chromedriver.exe", chrome_options=options)

    # 여기에서 개수를 조정한 후 돌려주세요! (최대 개수 150개)
    for url in store_data['kakao_url'][n:n+150]:
        driver.get(url)
        driver.implicitly_wait(10)
        try:
            rate_cnt = driver.find_element_by_xpath('//*[@id="mArticle"]/div[1]/div[1]/div[2]/div/div/a[1]/span[2]').text
            rate_cnt = re.findall("\d+", rate_cnt)
            rate = driver.find_element_by_xpath('//*[@id="mArticle"]/div[1]/div[1]/div[2]/div/div/a[1]/span[1]').text
            review_cnt = driver.find_element_by_xpath('//*[@id="mArticle"]/div[1]/div[1]/div[2]/div/div/a[2]/span').text
            review_cnt = re.findall("\d+", review_cnt)
            review = int(rate_cnt[0]) + int(review_cnt[0])
            driver.implicitly_wait(10)
            data = {'review': review, 'rate': float(rate)}
            review_rate = review_rate.append(data, ignore_index=True)
            
        # 후기 미제공일 때
        except:
            try:
                review_cnt = driver.find_element_by_xpath('//*[@id="mArticle"]/div[1]/div[1]/div[2]/div/div/a/span').text
                data = {'review': int(review_cnt) , 'rate': 0.0}
            except:
                data = {'review': 0.0 , 'rate': 0.0}
            review_rate = review_rate.append(data, ignore_index=True)

    driver.quit()
    review_rate.to_csv('data/review_rate.csv', index=False)
