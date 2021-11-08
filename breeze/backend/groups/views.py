from functools import partial
from django.shortcuts import get_object_or_404, get_list_or_404
from django.http.response import JsonResponse
from django.contrib.auth import get_user_model

from .models import Group, Groupmember
from .serializers import GroupSerializer, GroupmemberSerializer
from accounts.utils import check_login

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

User = get_user_model()


@api_view(['POST'])
@check_login
def group_create(request):
    group_data = {
        'name': request.data.get('groupName')
    }
    user = get_object_or_404(User, id=request.user.id)
    serializer = GroupSerializer(data=group_data, partial=True)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=user)
    group_id = serializer.data.get('id')
    group = get_object_or_404(Group, id=group_id)

    # 그룹별 멤버 저장
    members = request.data.get('groupMembers')
    print(request.data)
    for member in members:
        member_data = {
            'name': member.get('memName'),
            'building': member.get('memBuilding'),
            'latitude': member.get('memLatitude'),
            'longitude': member.get('memLongitude'),
            'barami_type': member.get('baramiType')
        }
        serializer = GroupmemberSerializer(data=member_data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save(group=group)
    data = { 'access_token': request.access_token }
    return Response(data, status=status.HTTP_201_CREATED)
    

@api_view(['GET'])
@check_login
def groups(request):
    groups = Group.objects.filter(user_id=request.user.id)

    group_data = []
    for group in groups:
        group_members = get_list_or_404(Groupmember, group_id=group.id)
        group_data.append(
            {
                'group_id': group.id,
                'group_name': group.name,
                'group_members': group_members,
            }
        )
    data = {
        'access_token': request.access_token,
        'group_data': group_data
    }
    return Response(data, status=status.HTTP_200_OK)
    # serializer = GroupmemeberSerializer(group_members, many=True)
    # return Response(serializer.data)


@api_view(['DELETE'])
@check_login
def group_delete(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    if request.user == group.user:
        group.delete()
        data = { 'access_token': request.access_token }
        return Response(data, status=status.HTTP_204_NO_CONTENT)