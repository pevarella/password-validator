# app/routers/auth.py
from datetime import timedelta

from fastapi import APIRouter, Form, HTTPException
from fastapi.security import OAuth2PasswordBearer

from src.core.config import (
    ACCESS_TOKEN_EXPIRE_MINUTES,
    CLIENT_ID,
    CLIENT_SECRET,
)
from src.schemas.auth_schemas import Token
from src.services.auth_service import create_access_token

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


@router.post('/token', response_model=Token)
async def login(
    client_id: str = Form(...),
    client_secret: str = Form(...),
    grant_type: str = Form(...),
):
    if (
        client_id == CLIENT_ID
        and client_secret == CLIENT_SECRET
        and grant_type == 'client_credentials'
    ):
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={'sub': client_id}, expires_delta=access_token_expires
        )
        return {'access_token': access_token, 'token_type': 'bearer'}
    else:
        raise HTTPException(
            status_code=400, detail='Invalid client credentials'
        )
