from django.urls import path
from .views import profile_view
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('profile/', profile_view, name='profile'),  # Thêm URL cho trang profile
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
