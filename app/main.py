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
    if data.user == "admin" and data.password == "1234":
        return {"status": "ok"}

    return {"status": "combinación incorrecta"}


# ==========================================================
# 2. NORMALIZATION
# ==========================================================
@app.post("/Normalization", response_model=NormalizationResponse)
def normalize(data: NormalizationRequest):
    text = data.text

    # Clean spaces
    if data.options.clean_spaces:
        text = re.sub(r"\s+", " ", text).strip()

    # Remove HTML
    if data.options.remove_html:
        text = re.sub(r"<[^>]+>", "", text)

    # Normalize Unicode (simulado)
    if data.options.normalize_unicode:
        text = text.encode("utf-8", errors="ignore").decode("utf-8")

    # Control chars
    if data.options.control_chars:
        text = re.sub(r"[\x00-\x1F\x7F]", "", text)

    # Delete format (simulado)
    if data.options.delete_format:
        text = text.replace("\t", " ")

    # Detect language (simulado)
    detected_language = "es"

    # Segmentation
    segments = []
    if data.options.segmentation:
        segments = [s.strip() for s in text.split(".") if s.strip()]

    # Quality assessment (simulado)
    quality_score = 0.98

    # Statistical profiling
    statistics = {}
    if data.options.statistical_profiling:
        statistics = {
            "characters": len(text),
            "words": len(text.split()),
            "segments": len(segments),
        }

    return {
        "normalized_text": text,
        "detected_language": detected_language,
        "segments": segments,
        "quality_score": quality_score,
        "statistics": statistics,
    }


# ==========================================================
# 3. ANONYMIZATION
# ==========================================================
@app.post("/Anonimization", response_model=AnonymizationResponse)
def anonymize(data: AnonymizationRequest):
    start = time.time()

    text = data.text

    # Ejemplo simple: reemplazar correos electrónicos
    anonymized_text = re.sub(
        r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",
        "[EMAIL]",
        text,
    )

    # Contar entidades encontradas (simulado)
    entities_found = text.count("@")

    execution_time_ms = round((time.time() - start) * 1000, 2)

    metadata = AnonymizationMetadata(
        entities_found=entities_found,
        execution_time_ms=execution_time_ms,
        model_used=data.ner_model,
        technique_used=data.anonymization_technique,
    )

    # Guardar log
    log = LogSchema(
        id=len(logs_db) + 1,
        process_type="anonymization",
        input_length=len(data.text),
        output_length=len(anonymized_text),
        execution_time_ms=execution_time_ms,
        status="success",
        timestamp=datetime.now().isoformat(),
        details={
            "model": data.ner_model,
            "technique": data.anonymization_technique,
            "entities_found": entities_found,
        },
    )
    guardar(log)

    return {
        "anonymized_text": anonymized_text,
        "metadata": metadata,
    }


# ==========================================================
# 4. LOGS
# ==========================================================
@app.get("/logs", response_model=list[LogSchema])
def get_logs():
    return logs_db