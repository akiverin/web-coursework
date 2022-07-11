from rest_framework.viewsets import ModelViewSet
from enemies.serializers import EnemySerializer
from enemies.models import Enemy

class EnemyViewSet(ModelViewSet):
    queryset = Enemy.objects.all()
    serializer_class = EnemySerializer
