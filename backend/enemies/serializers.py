from rest_framework import serializers
from enemies.models import Enemy
from levels.models import Level

class LevelSerializerForEnemy(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ['id','name','difficulty']

class EnemySerializer(serializers.ModelSerializer):
    levels_data = LevelSerializerForEnemy(source='level', many=True)
    class Meta:
        model = Enemy
        exclude = ['level']
