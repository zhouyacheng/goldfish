from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .auth import BearerTokenAuthentication
from .serializer import AuthorizationSerializer
from django.contrib.auth.models import User

class LoginView(GenericAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = AuthorizationSerializer
    queryset = User.objects.filter(is_active=1)
    def post(self,request:Request,*args,**kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class LogoutView(GenericAPIView):
    queryset = User.objects.filter(is_active=1)
    def get(self,request:Request,*args,**kwargs):
        if request.user:
            BearerTokenAuthentication().logout(request.auth)
        return Response(status=status.HTTP_204_NO_CONTENT)
