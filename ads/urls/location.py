from rest_framework import routers

from ads.views.location import LocationViewSet

router = routers.SimpleRouter()
router.register('', LocationViewSet)

urlpatterns = router.urls
