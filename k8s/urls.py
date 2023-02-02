from django.urls import path,re_path
from rest_framework.routers import SimpleRouter
from . import views


router = SimpleRouter()
router.register("pipeline",views.PipelineViewSet,basename="pipeline")
router.register("project",views.ProjectViewSet,basename="project")
router.register("env",views.ProjectEnvViewSet,basename="env")
router.register("resource",views.ProjectResourceViewSet,basename="resource")
router.register("stage",views.StageViewSet,basename="stage")
router.register("releasetask",views.ReleaseTaskViewSet,basename="releasetask")
router.register("configmap",views.ConfigMapViewSet,basename="configmap")


urlpatterns = [

]

urlpatterns += router.urls
print(f"k8s url: {urlpatterns}")
