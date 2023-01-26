from django.urls import path,re_path
from rest_framework.routers import SimpleRouter
from . import views


router = SimpleRouter()
router.register("task",views.TaskViewSet,basename="task")
router.register("repository",views.RepositoryViewSet,basename="repository")
router.register("template",views.TemplateViewSet,basename="template")
router.register("release",views.ReleaseViewSet,basename="release")
router.register("taskevent",views.TaskEventViewSet,basename="taskevent")
router.register("period",views.PeriodTaskViewSet,basename="period")

urlpatterns = [

]

urlpatterns += router.urls
print(urlpatterns)
