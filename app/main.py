from fastapi import FastAPI
from app.schemas import LoginBase, DataInsertBase

app = FastAPI(
    title="Text Anonymitation API",
    version="1.0.0"
)

@app.get("/")
def test ():
    return {"message": "api funcionando correctamente"}

@app.post("/login")
def login(data: LoginBase):
    return {
        "message": "mensaje recibido",
        "user": data.user_name
    }


