import os  # <-- Asegúrate de que esta línea esté aquí arriba
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Esto calcula la ruta de la carpeta templates subiendo un nivel desde la carpeta 'api'
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
templates = Jinja2Templates(directory=os.path.join(base_dir, "templates"))
# 1. Ruta de inicio (GET): Muestra el formulario
@app.get("/", response_class=HTMLResponse)
async def mostrar_formulario(request: Request, error: str = None):
    # Corrección aquí también para usar 'context' de forma segura
    return templates.TemplateResponse(
        request=request, 
        name="login.html", 
        context={"error": error}
    )

# 2. Ruta captura de información (POST): Procesa los datos del formulario
@app.post("/login")
async def procesar_login(
    request: Request, 
    username: str = Form(...), 
    password: str = Form(...)
):
    # Validación solicitada: si la contraseña es "1234"
    if password == "1234":
        # ¡Corregido! Pasamos request, el nombre de la plantilla y el context con tus variables
        return templates.TemplateResponse(
            request=request, 
            name="bienvenido.html", 
            context={"nombre_usuario": username}
        )
    else:
        # Redirige a la ruta raíz si la contraseña es incorrecta
        return RedirectResponse(url="/?error=Contrasena+incorrecta", status_code=303)