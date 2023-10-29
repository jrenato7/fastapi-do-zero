from jose import jwt

from fast_zero.security import create_access_token, verify_password
from fast_zero.settings import Settings

settings = Settings()


def test_jwt():
    data = {'test': 'test1'}
    token = create_access_token(data)

    decoded = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])

    assert decoded['test'] == data['test']
    assert decoded['exp']


def test_verify_password():
    password = 'the_pass'
    hashed_pass = (
        '$2b$12$WCvjGEKKSCNo2XUMYoTJVuf36/mROJSfBZBZt.9YNVAqRUnLANY5.'
    )
    assert verify_password(password, hashed_pass)
