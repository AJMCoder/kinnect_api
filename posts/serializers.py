from rest_framework import serializers
from posts.models import Post
from likes.models import Like
from django.utils.timezone import localtime


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()

    # Add formatted created and updated date fields
    formatted_created_at = serializers.SerializerMethodField()
    formatted_updated_at = serializers.SerializerMethodField()

    def validate_images(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image file too large ( > 2MB )')
        
        if value.image.width > 4096 or value.image.height > 4096:
            raise serializers.ValidationError('Image width or height is greater than 4096px')
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    
    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(owner=user, post=obj).first()
            return like.id if like else None
        return None

    # Format created_at
    def get_formatted_created_at(self, obj):
        return localtime(obj.created_at).strftime('%d %B %Y')

    # Format updated_at
    def get_formatted_updated_at(self, obj):
        return localtime(obj.updated_at).strftime('%d %B %Y')

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'formatted_created_at', 'formatted_updated_at',
            'title', 'content', 'image', 'image_filter',
            'like_id', 'likes_count', 'comments_count'
        ]