from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field


from typing import Optional
from pydantic import BaseModel, EmailStr


# =========================
# Response genérico
# =========================
class MessageResponse(BaseModel):
    message: str


# =========================
# 1. LOGIN
# =========================
class LoginBase(BaseModel):
    user: str
    password: str


# Alias para response_model del endpoint /login
LoginResponse = MessageResponse


# =========================
# 2. NORMALIZATION
# =========================
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


class NormalizationRequest(BaseModel):
    text: str
    options: Optional[NormalizationOptions] = None


# Alias para response_model del endpoint /Normalization
NormalizationResponse = MessageResponse


# =========================
# 3. ANONYMIZATION
# =========================
class AnonymizationRequest(BaseModel):
    text: str
    anonymization_technique: str = "masking"


# Alias para response_model del endpoint /Anonimization
AnonymizationResponse = MessageResponse


# =========================
# 4. LOGS
# =========================
# Si el endpoint /logs devuelve:
# {"message": "Funcionalidad de logs en desarrollo"}
# entonces también debe usar MessageResponse.
LogSchema = MessageResponse


# =========================
# 5. REGISTER USER
# =========================
class RegisterUserRequest(BaseModel):
    username: str
    email: EmailStr
    password: str
    full_name: Optional[str] = None


# Alias para response_model del endpoint /register
RegisterUserResponse = MessageResponse