from django.contrib.auth import get_user_model
from rest_framework import serializers


User = get_user_model()


class CreateUserSerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        if not attrs.get('phone_number') and not attrs.get('email'):
            raise serializers.ValidationError('At least one of "phone_number" and "email" is required.')
        return attrs

    class Meta:
        model = User
        fields = ('email', 'phone_number', 'username', 'firstname', 'lastname')
