from rest_framework import serializers
from accounts.models import Account

#Lead Serializer
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'