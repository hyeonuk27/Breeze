from os import access
from decouple import config
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from functools import wraps

import requests

REST_API_KEY = config('REST_API_KEY')
User = get_user_model()

def check_login(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        try: 
            if request.method == 'GET':
                user_id = request.GET.get('id')
            elif request.method == 'POST':
                user_id = request.POST.get('id')
            elif request.method == 'DELETE':
                user_id = request.DELETE.get('id')
            
            access_token = request.headers["Authorization"]
            # 토큰 유효성 확인
            token_status = get_token_status(access_token)
            user = User.objects.get(id=user_id)

            if token_status == 200:
                request.user = user
            else:
                refresh_token = user['token']
                new_access_token, new_refresh_token = update_token(refresh_token)
                if new_refresh_token:
                    pass
                
        except User.DoesNotExist:
            return JsonResponse({'message' : 'INVALID_USER'}, status=400)
        
        return func(request, *args, **kwargs)
    return wrapper

def get_token_status(access_token):
    # 토큰 정보보기 -- 만료되었다고 뜨면 -- 리프레시 토큰으로 갱신
    headers = {
        'Authorization': f'Bearer {access_token}',
    }

    response = requests.get('https://kapi.kakao.com/v1/user/access_token_info', headers=headers)
    
    # 200 / 400 / 401
    return response.status_code

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