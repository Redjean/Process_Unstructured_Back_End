from typing import Optional, Literal
from pydantic import BaseModel, EmailStr


# ==========================================================
# RESPUESTA GENÉRICA
# ==========================================================
class MessageResponse(BaseModel):
    message: str


# ==========================================================
# 1. INSERT DATA (Data Owner)
# Endpoint: /insert_data
# ==========================================================
class InsertDataRequest(BaseModel):
    text: str
    consent_accepted: bool


InsertDataResponse = MessageResponse


# ==========================================================
# 2. NORMALIZE DATA (Data Controller)
# Endpoint: /normalize_data
# ==========================================================
class NormalizationOptions(BaseModel):
    clean_spaces: bool = True
    remove_html: bool = True
    detect_language: bool = True
    segmentation: bool = True
    quality_assessment: bool = True
    normalize_unicode: bool = True
    control_chars: bool = True
    delete_format: bool = True
    statistical_profiling: bool = True


class NormalizeDataRequest(BaseModel):
    text: str
    options: Optional[NormalizationOptions] = None


NormalizeDataResponse = MessageResponse


# ==========================================================
# 3. ANONYMIZE DATA (Data Processor)
# Endpoint: /anonimize_data
# ==========================================================
class AnonymizeDataRequest(BaseModel):
    text: str
    anonymization_technique: Literal[
        "masking",
        "redaction",
        "pseudonymization",
        "tokenization"
    ] = "masking"


AnonymizeDataResponse = MessageResponse


# ==========================================================
# 4. REQUEST DATA (External Party / Receiver)
# Endpoint: /request_data
# ==========================================================
class RequestDataRequest(BaseModel):
    requester_name: str
    organization: str
    purpose: str
    legal_basis: str
    requested_data_description: str


RequestDataResponse = MessageResponse


# ==========================================================
# 5. CHECKING LOGS (Control Authority)
# Endpoint: /checking_logs
# ==========================================================
class CheckingLogsRequest(BaseModel):
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    process_type: Optional[str] = None


CheckingLogsResponse = MessageResponse


# ==========================================================
# 6. LOGIN
# Endpoint: /login
# ==========================================================
class LoginRequest(BaseModel):
    user: str
    password: str


LoginResponse = MessageResponse


# ==========================================================
# 7. SIGN IN / REGISTER USER
# Endpoint: /sign_in
# Rol por defecto: data_owner
# ==========================================================
class SignInRequest(BaseModel):
    username: str
    email: EmailStr
    password: str
    full_name: Optional[str] = None


SignInResponse = MessageResponse


# ==========================================================
# 8. MODIFY ATTRIBUTES (Admin)
# Endpoint: /modify_attributes
# ==========================================================
class ModifyAttributesRequest(BaseModel):
    username: str
    new_role: Literal[
        "admin",
        "data_owner",
        "data_controller",
        "data_processor",
        "external_party",
        "control_authority"
    ]


ModifyAttributesResponse = MessageResponse