from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    EmpresaViewSet,
    EquipoViewSet,
    TecnicoViewSet,
    PlanMantencionViewSet,
    OrdenTrabajoViewSet,
    status
)

router = DefaultRouter()
router.register(r"empresas", EmpresaViewSet)
router.register(r"equipos", EquipoViewSet)
router.register(r"tecnicos", TecnicoViewSet)
router.register(r"planes", PlanMantencionViewSet)
router.register(r"ordenes", OrdenTrabajoViewSet)

urlpatterns = [
    path("status/", status),
    path("", include(router.urls)),
]