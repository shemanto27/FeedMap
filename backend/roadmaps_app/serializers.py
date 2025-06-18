from rest_framework import serializers
from .models import RoadmapCategory, RoadmapItem

class RoadmapCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RoadmapCategory
        fields = '__all__'


class RoadmapItemSerializer(serializers.ModelSerializer):
    category = RoadmapCategorySerializer(read_only=True)

    class Meta:
        model = RoadmapItem
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')