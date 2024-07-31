from pydantic import BaseModel


class PasswordRequest(BaseModel):
    password: str


class ResponsePassword(BaseModel):
    is_valid: str
