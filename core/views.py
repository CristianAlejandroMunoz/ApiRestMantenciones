from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Empresa, Equipo, Tecnico, PlanMantencion, OrdenTrabajo
from .serializers import (
    EmpresaSerializer,
    EquipoSerializer,
    TecnicoSerializer,
    PlanMantencionSerializer,
    OrdenTrabajoSerializer
)


# -------------------------------------------------------------
# ENDPOINT DE PRUEBA EXIGIDO POR LA PAUTA (3.1.3 - Endpoint de estado)
# -------------------------------------------------------------
@api_view(["GET"])
def status(request):
    """
    Endpoint simple para verificar que la API está funcionando correctamente.
    Retorna un JSON con información básica del sistema.
    """
    return Response({
        "status": "OK",
        "message": "API funcionando correctamente",
        "version": "1.0"
    })


# -------------------------------------------------------------
# VIEWSETS CRUD PARA TODAS LAS ENTIDADES
# -------------------------------------------------------------

class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class EquipoViewSet(viewsets.ModelViewSet):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class TecnicoViewSet(viewsets.ModelViewSet):
    queryset = Tecnico.objects.all()
    serializer_class = TecnicoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class PlanMantencionViewSet(viewsets.ModelViewSet):
    queryset = PlanMantencion.objects.all()
    serializer_class = PlanMantencionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class OrdenTrabajoViewSet(viewsets.ModelViewSet):
    queryset = OrdenTrabajo.objects.all()
    serializer_class = OrdenTrabajoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]