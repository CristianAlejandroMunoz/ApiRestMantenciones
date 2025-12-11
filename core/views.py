from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
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


# ----------------------------
#  Endpoint de prueba (Pauta)
# ----------------------------
@api_view(["GET"])
def status(request):
    return Response({"status": "API funcionando correctamente"})


# ----------------------------
#       VIEWSETS CRUD
# ----------------------------

class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer


class EquipoViewSet(viewsets.ModelViewSet):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer


class TecnicoViewSet(viewsets.ModelViewSet):
    queryset = Tecnico.objects.all()
    serializer_class = TecnicoSerializer


class PlanMantencionViewSet(viewsets.ModelViewSet):
    queryset = PlanMantencion.objects.all()
    serializer_class = PlanMantencionSerializer


class OrdenTrabajoViewSet(viewsets.ModelViewSet):
    queryset = OrdenTrabajo.objects.all()
    serializer_class = OrdenTrabajoSerializer
