from pydantic import BaseModel

class DataInsertBase(BaseModel):
    id_user: int
    user_name: str
    text_unstructured: str

class LoginBase(BaseModel):
    user_name: str
    password: str