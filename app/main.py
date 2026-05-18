# ==========================================================
# main.py
# Arquitectura RESTful preliminar (todos los endpoints
# retornan únicamente {"message": "Endpoint en desarrollo"})
# ==========================================================

from fastapi import FastAPI

from app.schemas import (
    MessageResponse,
    DocumentCreateRequest,
    DocumentNormalizationRequest,
    DocumentAnonymizationRequest,
    AccessRequestCreateRequest,
    AuditLogQueryRequest,
    LoginRequest,
    RegisterRequest,
    UserRoleUpdateRequest,
)

app = FastAPI(
    title="Text Processing API",
    version="3.0.0",
    description="API RESTful para procesamiento de datos no estructurados y cumplimiento de la LOPDP."
)


# ==========================================================
# Endpoint raíz
# ==========================================================
@app.get("/")
def root():
    return {
        "message": "Bienvenido a la API RESTful de Procesamiento de Datos No Estructurados",
        "docs": "/docs",
        "redoc": "/redoc"
    }


# ==========================================================
# AUTHENTICATION
# ==========================================================
@app.post("/api/v1/auth/login", response_model=MessageResponse)
def login(data: LoginRequest):
    return {"message": "Endpoint en desarrollo"}


@app.post("/api/v1/auth/register", response_model=MessageResponse)
def register(data: RegisterRequest):
    return {"message": "Endpoint en desarrollo"}


# ==========================================================
# DOCUMENTS
# Data Owner crea un documento con consentimiento
# ==========================================================
@app.post("/api/v1/documents", response_model=MessageResponse)
def create_document(data: DocumentCreateRequest):
    return {"message": "Endpoint en desarrollo"}


# ==========================================================
# NORMALIZATIONS
# Data Controller procesa un documento existente
# ==========================================================
@app.post(
    "/api/v1/documents/{document_id}/normalizations",
    response_model=MessageResponse
)
def normalize_document(document_id: int, data: DocumentNormalizationRequest):
    return {"message": "Endpoint en desarrollo"}


# ==========================================================
# ANONYMIZATIONS
# Data Processor anonimiza un documento existente
# ==========================================================
@app.post(
    "/api/v1/documents/{document_id}/anonymizations",
    response_model=MessageResponse
)
def anonymize_document(document_id: int, data: DocumentAnonymizationRequest):
    return {"message": "Endpoint en desarrollo"}


# ==========================================================
# ACCESS REQUESTS
# External Party solicita acceso a datos
# ==========================================================
@app.post("/api/v1/access-requests", response_model=MessageResponse)
def create_access_request(data: AccessRequestCreateRequest):
    return {"message": "Endpoint en desarrollo"}


# ==========================================================
# AUDIT LOGS
# Control Authority consulta registros
# ==========================================================
@app.get("/api/v1/audit-logs", response_model=MessageResponse)
def get_audit_logs():
    return {"message": "Endpoint en desarrollo"}


# ==========================================================
# USERS / ROLES
# Admin modifica roles de usuario
# ==========================================================
@app.patch(
    "/api/v1/users/{user_id}/roles",
    response_model=MessageResponse
)
def update_user_role(user_id: int, data: UserRoleUpdateRequest):
    return {"message": "Endpoint en desarrollo"}