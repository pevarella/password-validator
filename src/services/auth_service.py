from datetime import datetime, timedelta

from fastapi import HTTPException
from jose import JWTError, jwt

from src.core.config import (
    ALGORITHM,
    SECRET_KEY,
)


def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        client_id: str = payload.get('sub')
        if client_id is None:
            raise HTTPException(status_code=401, detail='Invalid token')
        return client_id
    except JWTError:
        raise HTTPException(status_code=401, detail='Invalid token')
