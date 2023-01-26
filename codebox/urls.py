"""codebox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from drf_spectacular.views import SpectacularAPIView,SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from common.views import LoginView,LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/iac/', include("iac.urls")),
    path('api/k8s/', include("k8s.urls")),

    path('api/login/', LoginView.as_view(),name="login"),
    path('api/logout/', LogoutView.as_view(),name="logout"),

    # websocket test
    path("chat/", include("chat.urls")),

    path('doc/openapi/', SpectacularAPIView.as_view(),name="openapi"),
    path('doc/swagger', SpectacularSwaggerView.as_view(url_name="openapi"),name="swagger-ui"),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh", TokenRefreshView.as_view(), name="token_refresh")
]
