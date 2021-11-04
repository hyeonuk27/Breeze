from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from .serializers import PlaceListSerializer
from accounts.utils import check_login
from .models import Place

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

import random

@api_view(['POST'])
def get_middle(request):
    pass


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