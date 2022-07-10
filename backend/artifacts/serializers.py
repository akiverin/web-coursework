from rest_framework import serializers
from artifacts.models import Artifact
from levels.models import Level

class LevelSerializerForEnemy(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ['name','difficulty']

class ArtifactSerializer(serializers.ModelSerializer):
    levels_data = LevelSerializerForEnemy(source='level', many=True)
    class Meta:
        model = Artifact
        exclude = ['level']
