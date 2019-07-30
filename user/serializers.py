from rest_framework.serializers import ModelSerializer
from user.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        fields = ('first_name', 'last_name', 'username', 'password', 'groups', 'email')
        model = User
        extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data):
            user = User.objects.create(**validated_data)
            user.set_password(validated_data['password'])
            user.is_staff = True
            user.save()

            return user
