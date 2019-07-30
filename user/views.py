from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet
from user.permission import HasGroupPermission
#
# permission importing from my_permission fro APIView
# from user.my_permission import HasGroupPermission as APIViewPermission
#
from user.models import User
from user.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = (HasGroupPermission, )
    permission_groups = {
        'create': ['admin'],
        'list': ['admin', 'anonymous'],
        'retrieve': ['admin', 'anonymous'],
        'update': ['admin', 'anonymous'],
        'destroy': ['admin']
    }


# APIView defined for UserView
# class UserView(APIView):
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [APIViewPermission]
#     required_groups = {
#         'GET': ['anonymous'],
#         'POST': ['admin'],
#         'PUT': ['__all__']
#     }
#
#     def get(self, request):
#         user = User.objects.all()
#         return Response({"users": user})


class LoginView(ViewSet):
    serializer_class = AuthTokenSerializer

    @staticmethod
    def create(request):
        return ObtainAuthToken().post(request)


class LogoutView(APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
