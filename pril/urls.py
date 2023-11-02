from django.urls import include, path
from rest_framework.routers import DefaultRouter

from pril.views import import_data, PassViewSet, ItemViewSet

router = DefaultRouter()
router.register("pass", PassViewSet),
router.register("item", ItemViewSet)

urlpatterns = [
    path("products-import-data/", import_data),
    path("", include(router.urls)),
]
