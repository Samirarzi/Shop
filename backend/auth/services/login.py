from auth.constants import  REFRESH_TOKEN_EXPIRE_TIME
from auth.services.tokens import sign_jwt_tokens
from sessions.services.session import create_session


def create_login_session(user, user_agent):
    session = create_session(user, user_agent, REFRESH_TOKEN_EXPIRE_TIME)
    access_token, refresh_token = sign_jwt_tokens(user.pk, session.pk)
    return access_token, refresh_token
