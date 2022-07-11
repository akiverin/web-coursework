from rest_framework import serializers
from achievements.models import Achievement
from levels.models import Level

class LevelSerializerForEnemy(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ['name','difficulty']

class AchievementSerializer(serializers.ModelSerializer):
    levels_data = LevelSerializerForEnemy(source='level', many=True)
    class Meta:
        model = Achievement
        exclude = ['level']
