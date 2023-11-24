from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.contrib.auth.models import Group

from users.forms import UserChangeForm, UserCreationForm


@admin.register(get_user_model())
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm

    list_display = ('id', 'email', 'username', 'is_staff', 'is_active')
    list_filter = ('is_staff',)
    list_display_links = ['id', 'email']
    readonly_fields = ['date_joined']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('date_joined', 'is_active')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2'),
        }),
    )
    search_fields = ('email', 'username')
    ordering = ('email', 'username')


admin.site.unregister(Group)
