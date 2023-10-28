from fastapi.testclient import TestClient
from fast_zero.app import app


def test_root_must_return_200_and_message():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == 200
    assert response.json() == {'message': 'Olá Mundo!'}