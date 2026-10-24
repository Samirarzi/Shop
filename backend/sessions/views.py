from rest_framework import viewsets

from sessions.models import Session
from sessions.serializers import SessionSerializer


class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
