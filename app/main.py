from fastapi import FastAPI
from datetime import datetime
import time
import re
from app.schemas import (
    LoginBase,
    LoginResponse,
    NormalizationRequest,
    NormalizationResponse,
    AnonymizationRequest,
    AnonymizationResponse,
    AnonymizationMetadata,
    LogSchema,
)

app = FastAPI(
    title="Text Processing API",
    version="1.0.0",
    description="API para normalización, anonimización, logs y autenticación."
)

# Base de datos en memoria para ejemplo
logs_db = []


# ==========================================================
# Función para guardar logs (persistencia simulada)
# ==========================================================
def guardar(log: LogSchema):
    logs_db.append(log)


# ==========================================================
# Endpoint raíz
# ==========================================================
@app.get("/")
def root():
    return {
        "message": "Bienvenido a la API de Procesamiento de Datos No Estructurados",
        "docs": "/docs",
        "redoc": "/redoc"
    }


# ==========================================================
# 1. LOGIN
# ==========================================================
@app.post("/login", response_model=LoginResponse)
def login(data: LoginBase):
    return {"message": "funcionalidad de login en desarrollo"}


# ==========================================================
# 2. NORMALIZATION
# ==========================================================
@app.post("/Normalization", response_model=NormalizationResponse)
def normalize(data: NormalizationRequest):
    return {"message": "funcionalidad de normalización en desarrollo"}



# ==========================================================
# 3. ANONYMIZATION
# ==========================================================
@app.post("/Anonimization", response_model=AnonymizationResponse)
def anonymize(data: AnonymizationRequest):
    return {
        "message": "Funcionalidad de anonimización en desarrollo"
    }


# ==========================================================
# 4. LOGS
# ==========================================================
@app.get("/logs", response_model=list[LogSchema])
def get_logs():
    return {
        "message": "Funcionalidad de logs en desarrollo"
    }

@app.post("/register", response_model=RegisterUserResponse)
def register_user(data: RegisterUserRequest):
    return {
        "message": "Endpoint en desarrollo"
    }