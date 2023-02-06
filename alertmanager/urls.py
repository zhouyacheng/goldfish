from django.urls import path,re_path
from rest_framework.routers import SimpleRouter
from . import views


router = SimpleRouter()
router.register("project",views.ProjectViewSet,basename="project")
router.register("alert",views.AlertManagerViewSet,basename="alert")
router.register("userResult",views.AppAlertmanagerUserResultViewSet,basename="userResult")
router.register("jobResult",views.AppAlertmanagerJobResultViewSet,basename="jobResult")
router.register("jobStatusResult",views.AppAlertmanagerJobStatusResultViewSet,basename="jobStatusResult")


urlpatterns = [

]

urlpatterns += router.urls
print(f"alertmanager url: {urlpatterns}")
