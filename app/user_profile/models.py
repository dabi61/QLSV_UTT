from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Liên kết với User
    bio = models.TextField(blank=True, null=True)  # Thêm trường bio
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)  # Avatar người dùng
    birthday = models.DateField(null=True, blank=True)  # Ngày sinh

    def __str__(self):
        return self.user.username
