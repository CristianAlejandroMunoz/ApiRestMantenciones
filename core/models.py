from django.db import models
from django.contrib.auth.models import User


class Empresa(models.Model):
    """
    Representa a una empresa cliente que solicita servicios de mantención.
    """
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=250)
    rut = models.CharField(max_length=12, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Equipo(models.Model):
    """
    Equipo perteneciente a una empresa. 
    Ejemplo: compresores, bombas, generadores, etc.
    """
    company = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="equipments")
    name = models.CharField(max_length=200)
    serial_number = models.CharField(max_length=100, unique=True)
    critical = models.BooleanField(default=False)
    installed_at = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.serial_number}"


class Tecnico(models.Model):
    """
    Técnico responsable de realizar las mantenciones. 
    Asociado a un usuario del sistema.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="technician_profile")
    full_name = models.CharField(max_length=200)
    specialty = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.full_name


class PlanMantencion(models.Model):
    """
    Plan de mantención definido para un equipo.
    Ejemplo: plan semanal, mensual, cada X días, etc.
    """
    equipment = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name="maintenance_plans")
    name = models.CharField(max_length=200)
    frequency_days = models.PositiveIntegerField()  # cada cuántos días se ejecuta
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.equipment.name}"


class OrdenTrabajo(models.Model):
    """
    Orden de trabajo generada a partir de un plan de mantención.
    Se asigna un técnico encargado.
    """
    STATUS_CHOICES = [
        ("pendiente", "Pendiente"),
        ("en_proceso", "En proceso"),
        ("completada", "Completada"),
        ("cancelada", "Cancelada"),
    ]

    plan = models.ForeignKey(PlanMantencion, on_delete=models.SET_NULL, null=True, related_name="work_orders")
    equipment = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name="work_orders")
    technician = models.ForeignKey(Tecnico, on_delete=models.SET_NULL, null=True, related_name="assigned_orders")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pendiente")
    scheduled_date = models.DateField()
    completed_at = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"OT #{self.id} - {self.equipment.name} ({self.status})"
