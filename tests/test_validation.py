from http import HTTPStatus

from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def get_access_token():
    response = client.post(
        '/token',
        data={
            'client_id': 'myclientid',
            'client_secret': 'myclientsecret',
            'grant_type': 'client_credentials',
        },
        headers={'Content-Type': 'application/x-www-form-urlencoded'},
    )
    assert response.status_code == HTTPStatus.OK
    return response.json()['access_token']


def test_validation():
    token = get_access_token()
    response = client.post(
        '/validador-senhas',
        json={'password': ''},
        headers={'Authorization': f'Bearer {token}'},
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'is_valid': False}


def test_validation_valid_password():
    token = get_access_token()
    response = client.post(
        '/validador-senhas',
        json={'password': 'AbTp9!fok'},
        headers={'Authorization': f'Bearer {token}'},
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'is_valid': True}
