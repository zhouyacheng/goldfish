from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView
from rest_framework.response import Response
# from rest_framework.viewsets import ModelViewSet,GenericViewSet
from rest_framework.views import APIView
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from utils.paginations import CustomPageNumberPagination
from rest_framework.decorators import action
from .models import CiType,CiTypeField,Ci
from .serializers import CiTypeModelSerializer,CiModelSerializer,CiTypeRetriveModelSerializer,CiTypeFieldModelSerializer
from rest_framework_mongoengine.viewsets import ModelViewSet,GenericViewSet,ReadOnlyModelViewSet
from rest_framework_mongoengine.generics import RetrieveAPIView,ListAPIView

class CiTypeRetriveModelViewSet(RetrieveAPIView,GenericViewSet):
    queryset = CiType.objects.all()
    serializer_class = CiTypeRetriveModelSerializer

    def get_by_name_and_version(self, request, name, version):
        print(f"name: {name}, version: {version}")
        try:
            obj = self.get_queryset().get(name=name, version=version)
            print(obj)
            serializer = self.serializer_class(instance=obj)
        except Exception as e:
            raise ValueError(f"未知错误: {str(e)}")
        return Response(data=serializer.data, status=status.HTTP_200_OK)



class CiTypeModelViewSet(ListAPIView,GenericViewSet):
    queryset = CiType.objects.all()
    serializer_class = CiTypeModelSerializer

    # @action(detail=False,url_path="(?P<name>[^/.]+)/(?P<version>\d+)/")
    # def get_by_name_and_version(self, request, name, version):
    #     print(f"name: {name}, version: {version}")
    #     try:
    #         obj = self.get_queryset().get(name=name, version=version)
    #         print(obj)
    #         serializer = self.serializer_class(instance=obj)
    #     except Exception as e:
    #         raise ValueError(f"未知错误: {str(e)}")
    #     return Response(data=serializer.data, status=status.HTTP_200_OK)

    # @action(methods=['GET'],detail=False)
    # def all(self, request):
    #     queryset = self.filter_queryset(self.get_queryset())
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)

    # @action(methods=["GET"],detail=True)
    # def retrieve(self, request, pk=None,*args, **kwargs):
    #     # print("+" * 50)
    #     # print(pk)
    #     if not pk:
    #         queryset = self.filter_queryset(self.get_queryset())
    #         serializer = self.get_serializer(queryset, many=True)
    #         return Response(serializer.data)
    #     serializer_class = CiTypeRetriveModelSerializer
    #     instance = self.get_object()
    #     serializer = serializer_class(instance)
    #     return Response(serializer.data)

    # def get_serializer_class(self):
    #     if 'id' in self.kwargs or 'pk' in self.kwargs:
    #         return CiTypeRetriveModelSerializer
    #     return CiTypeModelSerializer

class CiModelViewSet(ModelViewSet):
    queryset = Ci.objects.all()
    serializer_class = CiModelSerializer

