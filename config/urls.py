from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from inforratica.views import ComputadorViewSet
from inforratica.views import ClienteViewSet
from inforratica.views import OrdemServicoViewSet
from usuario.router import router as usuario_router
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r"computadores", ComputadorViewSet)
router.register(r"clientes", ClienteViewSet)
router.register(r"ordemservico", OrdemServicoViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("api/", include(usuario_router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
