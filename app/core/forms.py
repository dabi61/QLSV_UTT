from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

UserModel = get_user_model()

class CustomLoginForm(forms.Form):
    identifier = forms.CharField(label="Tên đăng nhập hoặc Email")
    password = forms.CharField(label="Mật khẩu", widget=forms.PasswordInput)
    remember_me = forms.BooleanField(required=False, label="Ghi nhớ đăng nhập")

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)  # Tránh lỗi như bạn gặp
        super().__init__(*args, **kwargs)
        self.user_cache = None

    def clean(self):
        identifier = self.cleaned_data.get('identifier')
        password = self.cleaned_data.get('password')

        try:
            # Tìm theo email hoặc username
            user = UserModel.objects.filter(email=identifier).first() \
                or UserModel.objects.filter(username=identifier).first()
        except UserModel.DoesNotExist:
            user = None

        if user is None:
            raise forms.ValidationError("Tài khoản không tồn tại.")

        self.user_cache = authenticate(username=user.username, password=password)

        if self.user_cache is None:
            raise forms.ValidationError("Mật khẩu không đúng.")
        if not self.user_cache.is_active:
            raise forms.ValidationError("Tài khoản đã bị khóa.")

        return self.cleaned_data

    def get_user(self):
        return self.user_cache
    
    def form_valid(self, form):
        remember = form.cleaned_data.get('remember_me')

        if remember:
            # Ghi nhớ đăng nhập: 30 ngày
            self.request.session.set_expiry(60 * 60 * 24 * 30)  # 30 ngày
        else:
            # Không nhớ: hết phiên khi đóng trình duyệt
            self.request.session.set_expiry(0)

        return super().form_valid(form)