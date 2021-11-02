from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from .serializers import PlaceListSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from decouple import config

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
def get_store(request):
    pass


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


def get_rate(request):
    
    review_rate = pd.read_csv('data/review_rate.csv')
    store_data = pd.read_csv('data/store_data.csv')
    options = webdriver.ChromeOptions()
    options.add_argument("no-sandbox") 
    options.add_argument("disable-gpu") 
    options.add_argument("--lang=ko_KR") 
    options.add_argument( 'user-agent=Mozilla/5.0 Chrome/95.0.4638.54')
    
    driver = webdriver.Chrome(r"C:\Users\multicampus\CHENNI\자율프로젝트\S05P31A202\breeze\backend\maps\chromedriver.exe", chrome_options=options)

    # 여기에서 개수를 조정한 후 돌려주세요! (최대 개수 150개)
    for url in store_data['kakao_url'][:3]:
        driver.get(url)
        driver.implicitly_wait(10)
        rate_cnt = driver.find_element_by_xpath('//*[@id="mArticle"]/div[1]/div[1]/div[2]/div/div/a[1]/span[2]').text
        rate_cnt = re.findall("\d+", rate_cnt)
        rate = driver.find_element_by_xpath('//*[@id="mArticle"]/div[1]/div[1]/div[2]/div/div/a[1]/span[1]').text
        review_cnt = driver.find_element_by_xpath('//*[@id="mArticle"]/div[1]/div[1]/div[2]/div/div/a[2]/span').text
        review_cnt = re.findall("\d+", review_cnt)
        review = int(rate_cnt[0]) + int(review_cnt[0])
        driver.implicitly_wait(10)
        data = {'review': review, 'rate': float(rate)}
        review_rate = review_rate.append(data, ignore_index=True)

    driver.quit()
    review_rate.to_csv('data/review_rate.csv', index=False)

    # chrome driver 사용: forbidden 문제 해결 필요
    # selenium: hidden으로 표시되는 부분 문제 해결 필요
    # store_data = pd.read_csv('data/store_data.csv')
    # for url in store_data['kakao_url'][:100]:
    #     html = urlopen(url)
    #     soup  = BeautifulSoup(html, "html.parser")
    #     review_list = soup.select('.list_evaluation > li')

    # review_rate = pd.DataFrame({ 'review_cnt': comment_list, 'rate': rate_list})
    # review_rate.to_csv('data/review_rate.csv', index=False)



def insta_tag(request):
    # 전체 가게 정보 불러오기
    stores = pd.read_csv('data/alcohol.csv')
    store = pd.DataFrame()
    # 태그 개수
    ids = []
    tags = []

    # 로그인
    BASE_URL = 'https://www.instagram.com/'
    CHROME_WIN_UA = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
    LOGIN_URL = BASE_URL + 'accounts/login/ajax/'
    STORIES_UA = 'Instagram 123.0.0.21.114 (iPhone; CPU iPhone OS 11_4 like Mac OS X; en_US; en-US; scale=2.00; 750x1334) AppleWebKit/605.1.15'
    TAGS_URL = BASE_URL + 'explore/tags/{0}/?__a=1'

    session = requests.Session()
    session.headers = {'user-agent': CHROME_WIN_UA}
    session.cookies.set('ig_pr', '1')

    session.headers.update({'Referer': BASE_URL, 'user-agent': STORIES_UA})

    req = session.get(BASE_URL)
    session.headers.update({'X-CSRFToken': req.cookies['csrftoken']})

    # 인스타그램 아이디/비밀번호
    login_data = {'username': '', 'password': ''}
    login = session.post(LOGIN_URL, data=login_data, allow_redirects=True)
    session.headers.update({'X-CSRFToken': login.cookies['csrftoken']})
    cookie = login.cookies
    session.headers.update({'user-agent': CHROME_WIN_UA})

    cookie_byte = pickle.dumps(cookie)
    session.cookies.update(pickle.loads(cookie_byte))
    
    for index, store in stores.iterrows():
        id = store['id']
        name = store['name'].replace(' ', '')
        print(index)

        media_url = TAGS_URL.format(name)
        try:
            response = session.get(media_url).json()
            tag_cnt = response.get('data').get('media_count')
        except:
            tag_cnt = 0

        ids.append(id)
        tags.append(tag_cnt)
    
    store['id'] = ids
    store['tag'] = tags
    store.to_csv('data/insta_alcohol.csv', index=False)