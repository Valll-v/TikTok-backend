from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


User = get_user_model()


class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'phone_number', 'email', 'first_name', 'last_name', 'last_seen', 'is_blocked')
    list_filter = ()
    ordering = ()
    readonly_fields = ('last_seen', )
    search_fields = ('phone_number', 'username', 'email', )

    def has_add_permission(self, request):
        return False


admin.site.register(User, CustomUserAdmin)
