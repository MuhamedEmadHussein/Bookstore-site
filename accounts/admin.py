from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .forms import CustomUserCreationForm,CustomUserChangeForm

CsutomUser = get_user_model()
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CsutomUser
    list_display = [
        'email',
        'username',
        'is_superuser',
    ] 

admin.site.register(CsutomUser,CustomUserAdmin)