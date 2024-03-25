from rest_framework import serializers

from .models import StudentBiodata

class BiodataSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentBiodata
        fields = (
        'first_name',
        'last_name',
        'date_of_birth',
        'reg_number',
        'gender',
        'profile_picture'
    )