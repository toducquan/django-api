from rest_framework import serializers

from .models import Hero as HeroModel

class HeroSerializer(serializers.ModelSerializer):
    def validate_name(self, value):
        try:
            HeroModel.objects.get(name = value)
        except HeroModel.DoesNotExist:
            return value
        raise serializers.ValidationError(f"{value} has already exists")

    class Meta:
        model = HeroModel
        fields = '__all__'