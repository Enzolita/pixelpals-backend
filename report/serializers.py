# Customized to cater for report management functionality.
# This module defines the serializer for the Report model. 
# The serializer converts the Report model instances to 
# JSON format and validates the data.

from rest_framework import serializers
from .models import Report

class ReportSerializer(serializers.ModelSerializer):
    """
    Serializer for the Report model. 
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    profile_id = serializers.ReadOnlyField(source="owner.profile.id")
    profile_image = serializers.ReadOnlyField(source="owner.profile.image.url")
    class Meta:
        """
        Meta class to define the model and fields to be serialized.
        """
        model = Report
        fields = [
            'id', 
            'owner',
            'reason',
            'content',
            "profile_id",
            "profile_image",
            'created_at',
            'updated_at',
        ]