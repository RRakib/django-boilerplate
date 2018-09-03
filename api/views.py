from rest_framework import viewsets
from .models import DemoPurpose
from .serializers import DemoSerializer


class DemoViewSet(viewsets.ModelViewSet):
    queryset = DemoPurpose.objects.all()
    serializer_class = DemoSerializer