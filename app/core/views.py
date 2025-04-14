from viewflow.contrib.auth import AuthViewset
from .forms import CustomLoginForm

class MyAuthViewset(AuthViewset):
    def get_login_view_kwargs(self, **kwargs):
        return {
            'authentication_form': CustomLoginForm,
            **super().get_login_view_kwargs(**kwargs),
        }
