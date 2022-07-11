from rest_framework.viewsets import ModelViewSet
from levels.serializers import LevelSerializer
from levels.models import Level

class LevelViewSet(ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer
