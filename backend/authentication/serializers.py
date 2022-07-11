from rest_framework import serializers
from authentication.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','image', 'type', 'age', 'levels', 'scores', 'money', 'diamonds', 'is_activ', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        print(validated_data)
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        instance.is_active = True

        if password is not None:
            instance.set_password(password)
        instance.save()

        return instance
