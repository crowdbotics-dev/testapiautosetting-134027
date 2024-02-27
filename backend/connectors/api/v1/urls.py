from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors134027ViewSet

router = DefaultRouter()
router.register(
    "testconnectors134027", Testconnectors134027ViewSet, basename="testconnectors134027"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
