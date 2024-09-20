from functools import wraps
from django.shortcuts import redirect
from django.contrib import messages


def adminOnly(view_func):
    @wraps(view_func)
    def wrapperFunction(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_superuser:
            return view_func(request, *args, **kwargs)
        else:
            messages.error(request, 'Unauthoreised. login as admin')
            return redirect('/admin/');
    return wrapperFunction