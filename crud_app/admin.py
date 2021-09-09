from django.contrib import admin
from .models import UserDetails

class UserDetalsAdmin(admin.ModelAdmin):
    list_display = ['id','capture_name', 'address', 'owner_info', 'employee_size', 'user_id']
admin.site.register(UserDetails, UserDetalsAdmin)