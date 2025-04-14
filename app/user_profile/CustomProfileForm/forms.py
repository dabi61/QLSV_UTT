from django import forms
from .models import UserProfile
from django.contrib.auth import get_user_model

User = get_user_model()

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'avatar', 'birthday']  # Các trường bạn muốn cho phép người dùng cập nhật

class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']  # Các trường cơ bản của user
