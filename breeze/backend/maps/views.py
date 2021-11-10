from django.http.response import HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth import get_user_model
from .serializers import PlaceListSerializer
from accounts.utils import check_login
from .models import Place

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from decouple import config

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
def get_middle(request):
    pass


@api_view(['POST'])
@check_login
def get_store(request, category_id, filter_id):
    # 중간역에 해당하는 가게들 선택, 그 중 해당 카테고리 선택
    category_store = Place.objects.filter(middle_name=request.data['middlePlace'][:-1], category_num=category_id)

    # 전체 결과가 10개 이하면 다 반환
    if len(category_store) < 11:
        stores = category_store
    else:
        if filter_id == 0:
            # 인기순
            stores = category_store.order_by('-review')[:10]
        elif filter_id == 1:
            # 평점순
            stores = category_store.order_by('-rate')[:10]
        elif filter_id == 2:
            # 랜덤
            category_store = list(category_store)
            random.shuffle(category_store)
            stores = category_store[:10]
    
    store_data = []
    for store in stores:
        serializer = PlaceListSerializer(store)
        store_data.append(serializer.data)

    data = {
        'access_token': request.access_token,
        'stores': store_data
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
