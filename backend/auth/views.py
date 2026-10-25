from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView

from auth.serializers import LoginSerializer
from auth.services.login import create_login_session
from auth.services.refresh import refresh_session_token


class LoginAPIView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        access_token, refresh_token = create_login_session(user, request.headers.get('USER-AGENT'))
        response = Response({"success": True, "tokens": {"access": access_token}},
                            status=status.HTTP_200_OK)
        response.set_cookie(key="refresh", value=refresh_token, httponly=True)
        return response


class RefreshAPIView(APIView):
    def get(self, request):
        refresh_token = request.COOKIES.get('refresh')
        if not refresh_token:
            return AuthenticationFailed("There is no refresh token.")

        access_token, refresh_token = refresh_session_token(refresh_token)
        response = Response({"success": True, "tokens": {"access": access_token}},
                            status=status.HTTP_200_OK)
        response.set_cookie("refresh", refresh_token, httponly=True)
        return response
