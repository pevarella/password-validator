from http import HTTPStatus

from fastapi.testclient import TestClient
from jose import jwt

from src.app import app
from src.core.config import ALGORITHM, SECRET_KEY

client = TestClient(app)


def test_get_access_token():
    response = client.post(
        '/token',
        data={
            'client_id': 'myclientid',
            'client_secret': 'myclientsecret',
            'grant_type': 'client_credentials',
        },
    )
    assert response.status_code == HTTPStatus.OK
    token_data = response.json()
    assert 'access_token' in token_data
    assert token_data['token_type'] == 'bearer'

    # Verifique se o token pode ser decodificado corretamente
    access_token = token_data['access_token']
    payload = jwt.decode(access_token, SECRET_KEY, algorithms=[ALGORITHM])
    assert payload['sub'] == 'myclientid'


def test_invalid_client_credentials():
    response = client.post(
        '/token',
        data={
            'client_id': 'invalidclientid',
            'client_secret': 'invalidclientsecret',
            'grant_type': 'client_credentials',
        },
    )
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json() == {'detail': 'Invalid client credentials'}
