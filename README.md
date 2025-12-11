# API RESTful de Mantención Industrial – Evaluación 4 (TI3041)

Este proyecto corresponde a la **Evaluación N°4 del ramo Programación BackEnd (TI3041)** de INACAP.  
Consiste en el desarrollo de una **API RESTful** para gestionar información relacionada con los procesos de mantención industrial de empresas de la Región del Biobío.

La API fue desarrollada utilizando **Python**, **Django** y **Django REST Framework**, incorporando autenticación mediante **JWT**, serialización de datos en formato **JSON**, y CRUD completo para todas las entidades solicitadas.

---

## Objetivo del Proyecto

Desarrollar una API RESTful que permita registrar y administrar:

- Empresas clientes  
- Equipos industriales  
- Técnicos asignados  
- Planes de mantención  
- Órdenes de trabajo  

---

## Tecnologías utilizadas

- Python 3.12+
- Django 5
- Django REST Framework
- Django REST Framework SimpleJWT
- SQLite3

---

## Dependencias principales

Estas dependencias deben instalarse mediante:

```
pip install -r requirements.txt
```

Dependencias clave:

```
Django
djangorestframework
djangorestframework-simplejwt
```

---

## Instalación del proyecto

### 1. Crear entorno virtual
```
python -m venv venv
```

### 2. Activar entorno virtual

Windows:
```
venv\Scripts\activate
```

Linux/Mac:
```
source venv/bin/activate
```

### 3. Instalar dependencias
```
pip install -r requirements.txt
```

### 4. Ejecutar migraciones
```
python manage.py migrate
```

### 5. Crear un usuario administrador
```
python manage.py createsuperuser
```

### 6. Iniciar servidor
```
python manage.py runserver
```

Servidor disponible en:  
`http://127.0.0.1:8000/`

---

## Autenticación JWT

### Obtener Token
```
POST /api/token/
```

Body:
```json
{
  "username": "tu_usuario",
  "password": "tu_password"
}
```

Respuesta:
```json
{
  "refresh": "...",
  "access": "..."
}
```

### Refrescar Token
```
POST /api/token/refresh/
```

---

## Endpoints principales

Prefijo general:

```
/api/
```

### Endpoint de Estado
```
GET /api/status/
```

Ejemplo de respuesta:
```json
{
  "status": "OK",
  "message": "API funcionando correctamente",
  "version": "1.0"
}
```

---

## CRUD de Entidades

### Empresas
```
/api/empresas/
```

### Equipos
```
/api/equipos/
```

### Técnicos
```
/api/tecnicos/
```

### Planes de Mantención
```
/api/planes/
```

### Órdenes de Trabajo
```
/api/ordenes/
```

---

## Estructura del Proyecto

```
api_mantenciones/
├── api_mantenciones/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── core/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── manage.py
├── README.md
└── requirements.txt
```

---

## Características Notables

✔ API RESTful completa  
✔ CRUD para 5 entidades  
✔ Autenticación JWT  
✔ Formato JSON  
✔ Permisos IsAuthenticatedOrReadOnly  
✔ Endpoint de estado `/api/status/`  
✔ Buenas prácticas de código  

---

## Autor

Proyecto desarrollado para la asignatura **Programación BackEnd – TI3041**, INACAP.
Estudiante: Cristian Alejandro Junior Muñoz Mora
Carrera: Analista Programador