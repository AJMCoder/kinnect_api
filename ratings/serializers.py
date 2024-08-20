from django.db import IntegrityError
from rest_framework import serializers
from .models import Rating

class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = ["id", "owner", "profile", "rating", "created_at"]
    
    def create(self, validated_data):
        profile_id = self.context["profile_id"]
        owner_id = self.context["owner_id"]
        try:
            rating = Rating.objects.create(profile_id=profile_id, owner_id=owner_id, **validated_data)
        except IntegrityError:
            raise serializers.ValidationError("You have already rated this profile.")
        return rating