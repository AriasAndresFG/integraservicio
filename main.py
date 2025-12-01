from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse

app = FastAPI()

# Montar carpeta static/
app.mount("/static", StaticFiles(directory="static"), name="static")

# Carpeta templates/
templates = Jinja2Templates(directory="templates")


# -----------------------------
#           HOME
# -----------------------------
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


# -----------------------------
#       LOGIN / REGISTER
# -----------------------------
@app.get("/login", response_class=HTMLResponse)
def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.get("/register", response_class=HTMLResponse)
def register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


# -----------------------------
#            LOGOUT
# -----------------------------
@app.get("/logout")
def logout():
    # Redirige siempre al home
    return RedirectResponse("/", status_code=302)


# -----------------------------
#        USER  (CATÁLOGO)
# -----------------------------
@app.get("/user/dashboard", response_class=HTMLResponse)
def user_dashboard(request: Request):
    recursos = [
        {"tipo": "Salón", "nombre": "Salón 101", "capacidad": 40, "descripcion": "Salón equipado multimedia"},
        {"tipo": "Laboratorio", "nombre": "Laboratorio A", "capacidad": 25, "descripcion": "PCs de alto rendimiento"},
        {"tipo": "Auditorio", "nombre": "Auditorio Principal", "capacidad": 120, "descripcion": "Escenario y sonido"},
    ]

    return templates.TemplateResponse(
        "user/dashboard.html",
        {
            "request": request,
            "user": {"nombre": "Juan Pérez"},
            "recursos": recursos,
        }
    )


# -----------------------------
#        USER  (RESERVAS)
# -----------------------------
@app.get("/user/reservas", response_class=HTMLResponse)
def user_reservas(request: Request):
    reservas = [
        {"tipo": "Salón", "recurso": "Salón 101", "estado": "Activa", "fecha": "2025-02-01", "hora": "10:00"},
        {"tipo": "Laboratorio", "recurso": "Lab A", "estado": "Completada", "fecha": "2025-01-29", "hora": "08:00"},
    ]

    return templates.TemplateResponse(
        "user/reservas.html",
        {
            "request": request,
            "user": {"nombre": "Juan Pérez"},
            "reservas": reservas,
        }
    )


# -----------------------------
#        ADMIN  DASHBOARD
# -----------------------------
@app.get("/admin/dashboard", response_class=HTMLResponse)
def admin_dashboard(request: Request):
    return templates.TemplateResponse(
        "admin/dashboard.html",
        {
            "request": request,
            "total_recursos": 8,
            "reservas_activas": 3,
            "reservas_completadas": 12,
            "calificacion_promedio": 4.7,
        }
    )


# -----------------------------
#        ADMIN  RECURSOS
# -----------------------------
@app.get("/admin/recursos", response_class=HTMLResponse)
def admin_recursos(request: Request):

    recursos = [
        {"id": 1, "tipo": "Salón", "nombre": "Salón 101", "capacidad": 40, "descripcion": "Salón multimedia"},
        {"id": 2, "tipo": "Laboratorio", "nombre": "Lab A", "capacidad": 25, "descripcion": "Computadores Intel i7"},
        {"id": 3, "tipo": "Equipo", "nombre": "Proyector Epson", "capacidad": 0, "descripcion": "Full HD"},
    ]

    return templates.TemplateResponse(
        "admin/recursos.html",
        {
            "request": request,
            "recursos": recursos,
        }
    )


# -----------------------------
#        ADMIN  RESERVAS
# -----------------------------
@app.get("/admin/reservas", response_class=HTMLResponse)
def admin_reservas(request: Request):
    reservas = [
        {"usuario": "Carlos Gómez", "recurso": "Salón 101", "estado": "Activa", "fecha": "2025-02-01", "hora": "10:00"},
        {"usuario": "Ana Torres", "recurso": "Lab A", "estado": "Completada", "fecha": "2025-01-30", "hora": "14:00"},
        {"usuario": "Jorge Ruiz", "recurso": "Proyector", "estado": "Pendiente", "fecha": "2025-02-02", "hora": "09:00"},
    ]

    return templates.TemplateResponse(
        "admin/reservas.html",
        {
            "request": request,
            "reservas": reservas,
        }
    )


# -----------------------------
#      ADMIN CALIFICACIONES
# -----------------------------
@app.get("/admin/calificaciones", response_class=HTMLResponse)
def admin_calificaciones(request: Request):
    calificaciones = [
        {"usuario": "Carlos", "recurso": "Salón 101", "puntuacion": 5, "comentario": "Excelente servicio"},
        {"usuario": "Ana", "recurso": "Lab A", "puntuacion": 4, "comentario": "Computadores buenos"},
        {"usuario": "Luis", "recurso": "Proyector", "puntuacion": 3, "comentario": "Regular calidad"},
    ]

    return templates.TemplateResponse(
        "admin/calificaciones.html",
        {
            "request": request,
            "calificaciones": calificaciones,
        }
    )
