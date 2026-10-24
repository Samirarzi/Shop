from rest_framework import serializers

from sessions.models import Session


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ['id', 'revoked_at', 'created_at', 'expires_at', 'user_agent']
        read_only_fields = ['revoked_at', 'created_at', 'expires_at', 'user_agent']