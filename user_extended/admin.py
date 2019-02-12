from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BasicUserAdmin
from django.contrib.auth.models import User
from user_extended.models import Profile


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = "Profile"


class UserAdmin(BasicUserAdmin):
    inlines = (ProfileInline, )


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
