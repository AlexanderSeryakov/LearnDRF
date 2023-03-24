from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

from .models import Women


class WomenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Women
        fields = '__all__'

    # def create(self, validated_data):
    #     return Women.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.content = validated_data.get('content', instance.content)
    #     instance.time_update = validated_data.get('time_update', instance.time_update)
    #     instance.is_published = validated_data.get('is_published', instance.is_published)
    #     instance.cat_id = validated_data.get('cat_id', instance.cat_id)
    #     instance.save()
    #
    #     return instance
