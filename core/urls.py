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

# Rutas automáticas CRUD mediante ViewSets
router = DefaultRouter()
router.register(r'empresas', EmpresaViewSet)
router.register(r'equipos', EquipoViewSet)
router.register(r'tecnicos', TecnicoViewSet)
router.register(r'planes', PlanMantencionViewSet)
router.register(r'ordenes', OrdenTrabajoViewSet)

urlpatterns = [
    # Endpoint de prueba
    path("status/", status),

    # Endpoints CRUD
    path("", include(router.urls)),
]