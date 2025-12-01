🏰 Lazarus - Plataforma de Reserva de Recursos

Plataforma de gestión institucional diseñada para automatizar y optimizar la reserva de recursos físicos como salones, laboratorios, canchas, auditorios y equipos de manera fácil, rápida y segura.

📦 Módulos Principales

El sistema está dividido en las siguientes áreas funcionales:

    - Autenticación: Registro y acceso diferenciado para administradores - y usuarios finales (estudiantes/personal).
    - Inventario (Admin): Creación, edición y eliminación del catálogo de recursos (salones, equipos, etc.), incluyendo detalles de capacidad y tipo.
    - Catálogo (Usuario): Exploración y visualización de recursos disponibles con filtros y detalles de capacidad.
    - Reservas: Módulo central para solicitar, aprobar y gestionar la asignación de recursos en fechas y horarios específicos.
    - Historial: Seguimiento del estado de las reservas activas, pasadas y canceladas por el usuario o administrador.
    - Feedback/Calificaciones (Admin): Revisión de opiniones y puntuaciones de los usuarios sobre el estado y la calidad de los recursos utilizados.

🛠️ Instalación y Configuración
Sigue estos pasos para poner en marcha el proyecto Lazarus en tu entorno local:

Bash

# 1. Clonar el repositorio
git clone [URL-del-repo-de-Lazarus]

# 2. Navegar al directorio del proyecto
cd lazarus

# 3. Crear entorno virtual (Recomendado)
python -m venv venv

# 4. Activar entorno virtual
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 5. Instalar las dependencias necesarias
pip install -r requirements.txt

# 6. Ejecutar el servidor (Ajusta 'main:app' si tu archivo principal tiene otro nombre, ej. 'app:server')
uvicorn main:app --reload

Una vez ejecutado, el servidor estará disponible en http://127.0.0.1:8000 (o el puerto configurado por Uvicorn).