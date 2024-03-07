from django.contrib import admin

from .models import StudentBiodata

class BiodataAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'date_of_birth',
        'reg_number',
        'gender'
    )

admin.site.register(StudentBiodata, BiodataAdmin)

# Register your models here.
