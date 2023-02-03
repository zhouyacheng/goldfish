from django.urls import path,re_path
from . import views
from rest_framework.routers import SimpleRouter

urlpatterns = [
    path("upload/",views.upload),
    path("uploadserver/",views.upload_server),
    path("uploadpkey/",views.private_key_upload),
    path("ssh/",views.remote_ssh),
]

router = SimpleRouter()
router.register("jmp",views.OrganizationModelViewSet)
router.register("host",views.HostModelViewSet)
urlpatterns += router.urls

print(urlpatterns)


