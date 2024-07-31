from fastapi import APIRouter, Depends, HTTPException

from src.routers.auth import oauth2_scheme
from src.schemas.validation_schemas import (
    PasswordRequest,
)
from src.services.auth_service import verify_token
from src.services.validation_service import is_valid_password
from src.core.config import CLIENT_ID

router = APIRouter()


@router.post('/validador-senhas')
async def validate(
    passwordRequest: PasswordRequest, token: str = Depends(oauth2_scheme)
):
    if verify_token(token) == CLIENT_ID:
        is_valid = is_valid_password(passwordRequest.password)
        return {'is_valid': is_valid}
    else:
        raise HTTPException(status_code=401)
