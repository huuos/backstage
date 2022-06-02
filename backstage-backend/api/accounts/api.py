from accounts.models import Account
from rest_framework import viewsets, permissions
from .serializers import AccountSerializer

# Lead Viewset
class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all();
    permission_classes = [
        permissions.AllowAny
    ]

    serializer_class = AccountSerializer