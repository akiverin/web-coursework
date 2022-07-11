from rest_framework.routers import DefaultRouter
from authentication.views import UserViewSet
from enemies.views import EnemyViewSet
from levels.views import LevelViewSet
from products.views import ProductViewSet
from artifacts.views import ArtifactViewSet

router = DefaultRouter()

router.register('users', UserViewSet)
router.register('enemies', EnemyViewSet)
router.register('levels', LevelViewSet)
router.register('products', ProductViewSet)
router.register('artifacts', ArtifactViewSet)