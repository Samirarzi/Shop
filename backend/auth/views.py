from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from auth.serializers import LoginSerializer
from auth.services.tokens import sign_jwt_tokens


class LoginAPIView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        access_token, refresh_token = sign_jwt_tokens(user.id)

        return Response({"success": True, "tokens": {"access": access_token, "refresh": refresh_token}},
                        status=status.HTTP_200_OK)
