from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm, CustomUserChangeForm
from .models import UserProfile

@login_required
def profile_view(request):
    # Lấy profile của người dùng hiện tại
    user_profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        # Xử lý form khi người dùng submit
        profile_form = UserProfileForm(request.POST, request.FILES, instance=user_profile)  # Để upload avatar
        user_form = CustomUserChangeForm(request.POST, instance=request.user)  # Để thay đổi thông tin người dùng cơ bản
        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save()
            return redirect('profile')  # Sau khi cập nhật, chuyển hướng lại trang profile
    else:
        # Nếu không phải POST, hiển thị form với dữ liệu hiện tại
        profile_form = UserProfileForm(instance=user_profile)
        user_form = CustomUserChangeForm(instance=request.user)

    return render(request, 'account/profile.html', {
        'profile_form': profile_form,
        'user_form': user_form,
    })
