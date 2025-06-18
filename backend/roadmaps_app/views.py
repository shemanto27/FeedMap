from django.shortcuts import render
from .models import RoadmapCategory, RoadmapItem
from .serializers import RoadmapCategorySerializer, RoadmapItemSerializer
from rest_framework import viewsets


class RoadmapItemViewSet(viewsets.ModelViewSet):
    queryset = RoadmapItem.objects.all()
    serializer_class = RoadmapItemSerializer
