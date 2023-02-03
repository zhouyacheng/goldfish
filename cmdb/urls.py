from django.urls import path,re_path
from .views import CiTypeModelViewSet,CiModelViewSet,CiTypeRetriveModelViewSet
from rest_framework_mongoengine.routers import SimpleRouter


urlpatterns = [
    # path("citypes/", CiTypeModelViewSet.as_view({"get":"list"})),
    # re_path("citypes/(?P<id>[^/.]+)/$", CiTypeRetriveModelViewSet.as_view()),
    # re_path("citype/(?P<name>[^/.]+)/(?P<version>\d+)/$", CiTypeModelViewSet.as_view({"get": "get_by_name_and_version"})),
    #
    path("citypes/", CiTypeModelViewSet.as_view({"get":"list"})),
    re_path("citypes/(?P<id>[^/.]+)/$", CiTypeRetriveModelViewSet.as_view({"get":"get_by_name_and_version"})),
    re_path("citypes/(?P<name>[^/.]+)/(?P<version>\d+)/$", CiTypeRetriveModelViewSet.as_view({"get": "get_by_name_and_version"})),
]

router = SimpleRouter()
# router.register('citypes',CiTypeModelViewSet)
router.register('cis',CiModelViewSet)
urlpatterns += router.urls

print(urlpatterns)


# urlpatterns = [
#     path("citypes/",views.CiTypeModelViewSet.as_view({'get': 'list'})),
# ]
