from django.urls import path,re_path
from . import views
from rest_framework.routers import SimpleRouter

urlpatterns = [
    path('menulist/', views.menulist_view),
    path('whoami/', views.UserModelViewSet.as_view({"get":"whoami"})),
    re_path('resetpassword/(?P<pk>\d+)/', views.UserModelViewSet.as_view({"post":"reset_password"})),
]

router = SimpleRouter()
router.register('',views.UserModelViewSet)

urlpatterns += router.urls