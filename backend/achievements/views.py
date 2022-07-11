from rest_framework.viewsets import ModelViewSet
from achievements.serializers import AchievementSerializer
from achievements.models import Achievement

class AchievementViewSet(ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
