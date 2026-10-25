import jwt
from datetime import datetime, timedelta

from shop import settings


def sign_jwt_tokens(sub: str) -> tuple[str, str]:
    access_token_payload = {
        'sub': sub,
        'exp': datetime.now() + timedelta(minutes=10),
        'iat': datetime.now(),
    }
    refresh_token_payload = {
        'sub': sub,
        'exp': datetime.now() + timedelta(days=1),
        'iat': datetime.now(),
    }
    access_token = jwt.encode(access_token_payload, settings.ACCESS_SECRET_KEY, algorithm='HS256')
    refresh_token = jwt.encode(refresh_token_payload, settings.REFRESH_SECRET_KEY, algorithm='HS256')
    return access_token, refresh_token


def decode_jwt_token(token: str, secret_key: str) -> dict:
    try:
        return jwt.decode(token, secret_key, algorithms=['HS256'],
                          options={"require": ["sub", "exp", "iat"]})
    except jwt.ExpiredSignatureError:
        raise Exception('Token expired')
    except jwt.InvalidTokenError:
        raise Exception('Invalid token')


def decode_access_token(token: str) -> dict:
    return decode_jwt_token(token, settings.ACCESS_SECRET_KEY)


def decode_refresh_token(token: str) -> dict:
    return decode_jwt_token(token, settings.REFRESH_SECRET_KEY)
