from rest_framework.serializers import ModelSerializer

from users.models import User, Payment


class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class UserSerializer(ModelSerializer):
    payments = PaymentSerializer(many=True)
    class Meta:
        model = User
        fields = '__all__'

class UserCreateSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'password')
