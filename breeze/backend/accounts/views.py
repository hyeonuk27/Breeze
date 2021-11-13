from django.http.response import JsonResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib import auth
from .utils import check_login

from decouple import config

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

import requests


REST_API_KEY = config('REST_API_KEY')
User = get_user_model()


@api_view(['GET'])
def login(request):
    code = request.GET.get('code')
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'grant_type': 'authorization_code',
        'client_id': REST_API_KEY,
        'code': code,
    }
    response = requests.post('https://kauth.kakao.com/oauth/token', headers=headers, data=data).json()

    access_token = response.get('access_token')
    refresh_token = response.get('refresh_token')
    
    user_info = get_user_info(access_token, refresh_token)
    user = User.objects.get(id=user_info['id'])
    if refresh_token != user.token:
        user.token = refresh_token
        user.save()
        
    return Response(data=user_info, status=status.HTTP_201_CREATED)


def get_token_status(access_token):
    headers = {
        'Authorization': f'Bearer {access_token}',
    }
    response = requests.get('https://kapi.kakao.com/v1/user/access_token_info', headers=headers)
    
    return response.status_code


def get_user_info(access_token, refresh_token):
    headers = {
        'Authorization': f'Bearer {access_token}',
    }
    profile_json = requests.get('https://kapi.kakao.com/v2/user/me', headers=headers).json()
    user_id = profile_json.get('id')
    user_name = profile_json.get('kakao_account').get('profile').get('nickname')
    
    if not User.objects.filter(id = user_id).exists():
        new_user = User(
            id = user_id,
            username = user_name,
            token = refresh_token,
        )
        new_user.save()
        
    user_info = {
        'id': user_id,
        'username': user_name,
        'access_token': access_token,
        'refresh_token': refresh_token,
    }
    return user_info


def update_token(refresh_token):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'grant_type': 'refresh_token',
        'client_id': REST_API_KEY,
        'refresh_token': refresh_token,
    }
    response = requests.post('https://kauth.kakao.com/oauth/token', headers=headers, data=data).json()
    new_access_token = response.get('access_token')
    new_refresh_token = response.get('refresh_token')
    return [new_access_token, new_refresh_token]

    
@api_view(['POST'])
@check_login
def logout(request):
    if (request.access_token):
        access_token = request.access_token
    else:
        access_token = request.headers["Authorization"].split()[1]
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': f'Bearer {access_token}',
    }
    response = requests.post('https://kapi.kakao.com/v1/user/logout', headers=headers)
    return Response(response)


@api_view(['GET'])
@check_login
def check(request):
    if (request.access_token):
        access_token = request.access_token
    else:
        access_token = request.headers["Authorization"].split()[1]
    response = {
        'access_token': access_token
    }
    return Response(data=response, status=status.HTTP_201_CREATED)
