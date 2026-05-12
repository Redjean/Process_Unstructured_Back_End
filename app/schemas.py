from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field


# =========================
# 1. LOGIN
# =========================
class LoginBase(BaseModel):
    user: str
    password: str


class LoginResponse(BaseModel):
    status: str


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
    options: Optional[NormalizationOptions] = Field(
        default_factory=NormalizationOptions
    )


class NormalizationResponse(BaseModel):
    normalized_text: str
    detected_language: Optional[str] = None
    segments: Optional[List[str]] = None
    quality_score: Optional[float] = None
    statistics: Optional[Dict[str, Any]] = None


# =========================
# 3. ANONYMIZATION
# =========================
class AnonymizationRequest(BaseModel):
    text: str
    ner_model: str = "electra"
    anonymization_technique: str = "masking"


class AnonymizationMetadata(BaseModel):
    entities_found: int
    execution_time_ms: float
    model_used: str
    technique_used: str


class AnonymizationResponse(BaseModel):
    anonymized_text: str
    metadata: AnonymizationMetadata


# =========================
# 4. LOGS
# =========================
class LogSchema(BaseModel):
    id: int
    process_type: str
    input_length: int
    output_length: int
    execution_time_ms: float
    status: str
    timestamp: str
    details: Optional[Dict[str, Any]] = None