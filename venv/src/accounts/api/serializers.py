from rest_framework import serializers
from accounts.models import User

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_fields = []
        depth = 1
class Postlistserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'