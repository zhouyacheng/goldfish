from django.urls import path,re_path
from rest_framework.routers import SimpleRouter
from . import views


router = SimpleRouter()
router.register("project",views.ProjectViewSet,basename="project")
router.register("alert",views.AlertManagerViewSet,basename="alert")


urlpatterns = [

]

urlpatterns += router.urls
print(f"alertmanager url: {urlpatterns}")
