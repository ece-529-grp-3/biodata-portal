from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from .models import StudentBiodata
from rest_framework import permissions
from .serializers import BiodataSerializer

class BiodataViewSet(viewsets.ModelViewSet):
    queryset = StudentBiodata.objects.all()
    serializer_class = BiodataSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend]

    def get_queryset(self):
        return StudentBiodata.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, reg_number=self.kwargs["pk"])
        return obj

# Create your views here.
