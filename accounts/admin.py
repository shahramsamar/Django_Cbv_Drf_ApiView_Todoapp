from django.contrib import admin
from django.contrib.auth.models import User
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    model = UserProfile
    fields = ['user', 'profile_picture']
    # readonly_fields = ['user']

admin.site.register(UserProfile, UserProfileAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'profile_picture')

    def profile_picture(self, obj):
        try:
            return obj.userprofile.profile_picture.url
        except UserProfile.DoesNotExist:
            return 'No picture'

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
