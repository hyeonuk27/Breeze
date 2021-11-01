from django.shortcuts import get_object_or_404, get_list_or_404
from django.http.response import JsonResponse

from .models import Group, Groupmember
from .serializers import GroupmemeberSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def group_create(request):
    pass


@api_view(['GET'])
def groups(request, user_id):
    groups = Group.objects.filter(user_id=user_id)

    data = []
    for group in groups:
        group_members = get_list_or_404(Groupmember, group_id=group.pk)
        data.append(
            {
                'group_id': group.pk,
                'group_name': group.name,
                'group_members': group_members,
            }
        )
    return JsonResponse(data, safe=False)
    # serializer = GroupmemeberSerializer(group_members, many=True)
    # return Response(serializer.data)


@api_view(['DELETE'])
def group_delete(request):
    pass