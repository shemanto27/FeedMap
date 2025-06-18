from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import RoadmapItemViewSet

router = DefaultRouter()
router.register(r'roadmap-items', RoadmapItemViewSet, basename='roadmapitem')

urlpatterns = [
    path('', include(router.urls)),
]
