# ==========================================================
# schemas.py
# ==========================================================

from typing import Optional, Literal
from pydantic import BaseModel, EmailStr


# ==========================================================
# RESPUESTA GENÉRICA
# ==========================================================
class MessageResponse(BaseModel):
    message: str


# ==========================================================
# AUTHENTICATION
# ==========================================================
class LoginRequest(BaseModel):
    user: str
    password: str


class RegisterRequest(BaseModel):
    username: str
    email: EmailStr
    password: str
    full_name: Optional[str] = None


# ==========================================================
# DOCUMENTS
# ==========================================================
class ComplianceInfo(BaseModel):
    lodpd_consent_granted: bool
    consent_version: str = "v1.0"


class DocumentCreateRequest(BaseModel):
    raw_text: str
    compliance: ComplianceInfo


# ==========================================================
# NORMALIZATIONS
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


class DocumentNormalizationRequest(BaseModel):
    options: Optional[NormalizationOptions] = None


# ==========================================================
# ANONYMIZATIONS
# ==========================================================
class DocumentAnonymizationRequest(BaseModel):
    anonymization_technique: Literal[
        "masking",
        "redaction",
        "pseudonymization",
        "tokenization"
    ] = "masking"


# ==========================================================
# ACCESS REQUESTS
# ==========================================================
class AccessRequestCreateRequest(BaseModel):
    requester_name: str
    organization: str
    purpose: str
    legal_basis: str
    requested_data_description: str


# ==========================================================
# AUDIT LOGS
# (GET sin body, por ahora no requiere schema)
# ==========================================================
class AuditLogQueryRequest(BaseModel):
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    process_type: Optional[str] = None


# ==========================================================
# USER ROLE UPDATE
# ==========================================================
class UserRoleUpdateRequest(BaseModel):
    new_role: Literal[
        "admin",
        "data_owner",
        "data_controller",
        "data_processor",
        "external_party",
        "control_authority"
    ]