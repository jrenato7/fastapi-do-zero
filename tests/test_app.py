def test_root_must_return_200_and_message(client):
    response = client.get('/')

    assert response.status_code == 200
    assert response.json() == {'message': 'Olá Mundo!'}


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'secret',
        },
    )

    assert response.status_code == 201
    assert response.json() == {
        'username': 'alice',
        'email': 'alice@example.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')
    assert response.status_code == 200
    assert response.json() == {
        'users': [
            {
                'username': 'alice',
                'email': 'alice@example.com',
                'id': 1,
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'jose',
            'email': 'jose@example.com',
            'password': 'jose123',
        },
    )

    assert response.status_code == 200
    assert response.json() == {
        'username': 'jose',
        'email': 'jose@example.com',
        'id': 1,
    }


def test_update_user_not_found(client):
    response = client.put(
        '/users/4',
        json={
            'username': 'jose',
            'email': 'jose@example.com',
            'password': 'jose123',
        },
    )

    assert response.status_code == 404
    assert response.json() == {'detail': 'User not found'}


def test_delete_user_success(client):
    response = client.delete('/users/1')

    assert response.status_code == 200
    assert response.json() == {'detail': 'User deleted'}


def test_delete_user_fail(client):
    response = client.delete('/users/3')

    assert response.status_code == 404
    assert response.json() == {'detail': 'User not found'}
