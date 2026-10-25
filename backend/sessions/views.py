from datetime import datetime

from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

from sessions.models import Session
from sessions.serializers import SessionSerializer, RevokeSessionSerializer


class SessionViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = SessionSerializer

    def get_queryset(self):
        return Session.objects.filter(user=14).order_by('-created_at')

    def get_serializer_class(self):
        if self.action == 'revoke':
            return RevokeSessionSerializer
        return SessionSerializer

    @action(detail=False, methods=['post'])
    def revoke(self, request):
        serializer = RevokeSessionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        revoked_sessions = self.get_queryset().filter(pk__in=serializer.validated_data['session_ids'],
                                                      revoked_at__isnull=True).update(revoked_at=datetime.now())
        return Response({'revoked_sessions': revoked_sessions})

    @action(detail=False, methods=['post'])
    def logout(self, request):
        ...
