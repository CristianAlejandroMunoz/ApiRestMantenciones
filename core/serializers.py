from rest_framework import serializers
from .models import Empresa, Equipo, Tecnico, PlanMantencion, OrdenTrabajo
from django.contrib.auth.models import User


class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = "__all__"


class EquipoSerializer(serializers.ModelSerializer):
    company = serializers.StringRelatedField(read_only=True)
    company_id = serializers.PrimaryKeyRelatedField(
        queryset=Empresa.objects.all(), source="company", write_only=True
    )

    class Meta:
        model = Equipo
        fields = ["id", "company", "company_id", "name", "serial_number", "critical", "installed_at"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]


class TecnicoSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source="user", write_only=True
    )

    class Meta:
        model = Tecnico
        fields = ["id", "user", "user_id", "full_name", "specialty", "phone"]


class PlanMantencionSerializer(serializers.ModelSerializer):
    equipment = serializers.StringRelatedField(read_only=True)
    equipment_id = serializers.PrimaryKeyRelatedField(
        queryset=Equipo.objects.all(), source="equipment", write_only=True
    )

    class Meta:
        model = PlanMantencion
        fields = ["id", "equipment", "equipment_id", "name", "frequency_days", "active"]


class OrdenTrabajoSerializer(serializers.ModelSerializer):
    plan = serializers.StringRelatedField(read_only=True)
    plan_id = serializers.PrimaryKeyRelatedField(
        queryset=PlanMantencion.objects.all(), source="plan", write_only=True
    )

    equipment = serializers.StringRelatedField(read_only=True)
    equipment_id = serializers.PrimaryKeyRelatedField(
        queryset=Equipo.objects.all(), source="equipment", write_only=True
    )

    technician = serializers.StringRelatedField(read_only=True)
    technician_id = serializers.PrimaryKeyRelatedField(
        queryset=Tecnico.objects.all(), source="technician", write_only=True
    )

    class Meta:
        model = OrdenTrabajo
        fields = [
            "id",
            "plan", "plan_id",
            "equipment", "equipment_id",
            "technician", "technician_id",
            "status",
            "scheduled_date",
            "completed_at",
            "notes"
        ]