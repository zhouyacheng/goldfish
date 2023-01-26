from rest_framework.views import exception_handler
from django.db import DatabaseError
from rest_framework.response import Response
from rest_framework import status
def customer_execptions(exc, context):
    """自定义异常"""
    # 优先调用drf本身的异常处理，它的返回值要么是None，要么是response
    response = exception_handler(exc, context)

    if response is None:
        # 判断是否是数据库
        if isinstance(exc, DatabaseError):
            view = context['view']
            print( '[%s]: %s' % (view, exc) )
            response = Response(data={"msg":"服务器内部存储错误！请联系管理员！"}, status=status.HTTP_507_INSUFFICIENT_STORAGE)

    return response