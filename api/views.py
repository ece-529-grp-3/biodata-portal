from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import StudentBiodata
from rest_framework import permissions
from .serializers import BiodataSerializer

class BiodataViewSet(viewsets.ModelViewSet):
    queryset = StudentBiodata.objects.all()
    serializer_class = BiodataSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend]

# Create your views here.
