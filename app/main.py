from fastapi import FastAPI

from app.schemas import (
    InsertDataRequest,
    InsertDataResponse,
    NormalizeDataRequest,
    NormalizeDataResponse,
    AnonymizeDataRequest,
    AnonymizeDataResponse,
    RequestDataRequest,
    RequestDataResponse,
    CheckingLogsRequest,
    CheckingLogsResponse,
    LoginRequest,
    LoginResponse,
    SignInRequest,
    SignInResponse,
    ModifyAttributesRequest,
    ModifyAttributesResponse,
)

app = FastAPI(
    title="Text Processing API",
    version="2.0.0",
    description="API para ingesta, normalización, anonimización, solicitud de datos, auditoría y gestión de usuarios."
)


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
# 1. INSERT DATA (Data Owner)
# ==========================================================
@app.post("/insert_data", response_model=InsertDataResponse)
def insert_data(data: InsertDataRequest):
    return {
        "message": "Endpoint en desarrollo"
    }


# ==========================================================
# 2. NORMALIZE DATA (Data Controller)
# ==========================================================
@app.post("/normalize_data", response_model=NormalizeDataResponse)
def normalize_data(data: NormalizeDataRequest):
    return {
        "message": "Endpoint en desarrollo"
    }


# ==========================================================
# 3. ANONYMIZE DATA (Data Processor)
# ==========================================================
@app.post("/anonimize_data", response_model=AnonymizeDataResponse)
def anonimize_data(data: AnonymizeDataRequest):
    return {
        "message": "Endpoint en desarrollo"
    }


# ==========================================================
# 4. REQUEST DATA (External Party / Receiver)
# ==========================================================
@app.post("/request_data", response_model=RequestDataResponse)
def request_data(data: RequestDataRequest):
    return {
        "message": "Endpoint en desarrollo"
    }


# ==========================================================
# 5. CHECKING LOGS (Control Authority)
# ==========================================================
@app.post("/checking_logs", response_model=CheckingLogsResponse)
def checking_logs(data: CheckingLogsRequest):
    return {
        "message": "Endpoint en desarrollo"
    }


# ==========================================================
# 6. LOGIN
# ==========================================================
@app.post("/login", response_model=LoginResponse)
def login(data: LoginRequest):
    return {
        "message": "Endpoint en desarrollo"
    }


# ==========================================================
# 7. SIGN IN / REGISTER USER
# ==========================================================
@app.post("/sign_in", response_model=SignInResponse)
def sign_in(data: SignInRequest):
    return {
        "message": "Endpoint en desarrollo"
    }


# ==========================================================
# 8. MODIFY ATTRIBUTES (Admin)
# ==========================================================
@app.post("/modify_attributes", response_model=ModifyAttributesResponse)
def modify_attributes(data: ModifyAttributesRequest):
    return {
        "message": "Endpoint en desarrollo"
    }