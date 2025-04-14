from django.urls import path
from django.contrib.auth.models import User
from viewflow.contrib.auth import AuthViewset
from viewflow.urls import Application, Site, ModelViewset
from room.views import CityViewset
from core.views import MyAuthViewset
from core.forms import CustomLoginForm
from django.contrib.auth.views import LoginView


site = Site(title="QLSV UTT", viewsets=[
    Application(
        title='Quản lý người dùng', icon='people', app_name='home', viewsets=[
            ModelViewset(model=User),
        ]
    ),
    Application(
        title='Lớp học', icon='people', app_name='room', viewsets=[
            CityViewset(),
        ]
    ),
])

urlpatterns = [
    # path('accounts/', AuthViewset(with_profile_view=False).urls),
    path('',site.urls),
    path('accounts/', AuthViewset(
        allow_password_change=True,
        with_profile_view=True,
        login_view=LoginView.as_view(authentication_form=CustomLoginForm)
    ).urls),

]
