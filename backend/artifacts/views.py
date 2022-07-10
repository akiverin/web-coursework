from rest_framework.viewsets import ModelViewSet
from artifacts.serializers import ArtifactSerializer
from artifacts.models import Artifact

class ArtifactViewSet(ModelViewSet):
    queryset = Artifact.objects.all()
    serializer_class = ArtifactSerializer
