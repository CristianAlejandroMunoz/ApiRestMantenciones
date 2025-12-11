from django.contrib import admin
from django.urls import path, include

# IMPORTANTE: importar las vistas JWT
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Rutas principales de tu API
    path("api/", include("core.urls")),

    # -----------------------------
    #   RUTAS JWT (Autenticación)
    # -----------------------------
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
