from django.contrib import admin
from authentication.models import MyUser
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserAdmin(BaseUserAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name', 'user_name', 'phone', 'city', 'province', 'address', 'country',
                    'package', 'no_of_acres', 'last_login', 'is_active', 'is_verified', 'is_admin', 'package_renew', 'created_at', 'updated_at')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('id', 'email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'user_name', 'phone', 'city', 'province', 'address', 'country',
         'package', 'no_of_acres', 'last_login', 'is_active', 'is_verified', 'package_renew', 'created_at', 'updated_at',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'email', 'first_name', 'last_name', 'user_name', 'phone', 'city', 'province', 'address', 'country', 'package', 'no_of_acres', 'last_login', 'is_active', 'is_verified', 'is_admin', 'package_renew', 'password'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(MyUser, UserAdmin)