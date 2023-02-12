from django.urls import path,re_path
from rest_framework.routers import SimpleRouter
from . import views


router = SimpleRouter()
router.register("terraform",views.TerraformViewSet,basename="terraform")


urlpatterns = [

]

urlpatterns += router.urls
print(f"terraform url: {urlpatterns}")
