from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer
from .pagination import CustomPagination

class PostAndGetHandler(APIView):
    def get(self, request):
        users = User.objects.all()
        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(users, request)
        serializer = UserSerializer(result_page, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({
                'status': 'failed',
                'message': serializer.errors
            })

        try:
            serializer.save()
            return Response({
                'status': 'success',
                'message': 'user has been created'
            })
        except Exception as err:
            return Response({
                'status': 'failed',
                'message': err
            })


class GetPutDeleteHandler(APIView):
    def get(self, request, id):
        user = User.objects.get(id=id)
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)

    def put(self, request, id):
        user = User.objects.get(id=id)
        serializer = UserSerializer(instance=user, data=request.data)

        if not serializer.is_valid():
            return Response({
                'status': 'failed',
                'message': serializer.errors
            })

        try:
            serializer.save()
            return Response({
                'status': 'success',
                'message': 'user has been updated'
            })
        except Exception as err:
            return Response({
                'status': 'failed',
                'message': err
            })

    def delete(self, request, id):
        user = User.objects.get(id=id)
        
        try:
            user.delete()
            return Response({
                'status': 'success',
                'message': 'user has been deleted'
            })
        except Exception as err:
            return Response({
                'status': 'failed',
                'message': err
            })
