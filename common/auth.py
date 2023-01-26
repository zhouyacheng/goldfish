import uuid

from django.utils import timezone
from django.contrib.auth.models import User,AnonymousUser
from django_redis import get_redis_connection
from rest_framework.authentication import BaseAuthentication, get_authorization_header
from rest_framework import exceptions
from common.settings import common_settings
from datetime import timedelta


class BearerTokenAuthentication(BaseAuthentication):
    _keyword = common_settings.AUTHENTICATION_KEYWORD
    _cache = get_redis_connection(common_settings.AUTHENTICATION_STORE_CACHE_NAME)
    _prefix = common_settings.AUTHENTICATION_STORE_CACHE_PREFIX

    @classmethod
    def _key(cls,token):
        return ":".join([cls._prefix,token])

    def authenticate(self, request):
        auth = get_authorization_header(request).split()

        if not auth or auth[0].lower() != self._keyword.lower().encode():
            return (AnonymousUser(),None)
        if len(auth) == 1:
            msg = f'Invalid {self._keyword} header. No credentials provided.'
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = f'Invalid {self._keyword} header. Credentials string should not contain spaces.'
            raise exceptions.AuthenticationFailed(msg)
        token = auth[1].strip().decode()
        if len(token) == 0:
            msg = 'Invalid token header. No credentials provided.'
            raise exceptions.AuthenticationFailed(msg)
        uid = self._cache.get(self._key(token))
        try:
            user = User.objects.get(pk=uid)
            if not user.is_active:
                msg = 'User was blocked'
                raise exceptions.AuthenticationFailed(msg)
            return (user,token)
        except:
            return (AnonymousUser(),None)

    def authenticate_header(self,request):
        return self._keyword

    def login(self,user_id,ttl=common_settings.AUTHENTICATION_TOKEN_ALIVE_TIME):
        token = uuid.uuid4().hex
        expired_time = timezone.now() + timedelta(seconds=ttl)
        self._cache.setex(self._key(token),ttl,user_id)
        return (token,expired_time)

    def logout(self,token):
        self._cache.delete(self._key(token))
