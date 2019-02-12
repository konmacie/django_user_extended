from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db import transaction
from user_extended.forms import ProfileForm, UserForm


@login_required
@transaction.atomic
def user_change(request):
    if request.method == "POST":
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }

    return render(request, 'user_change_form.html', context=context)
