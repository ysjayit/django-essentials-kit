from django.shortcuts import redirect
from django.contrib import messages


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        else:
            return view_func(request, *args, **kwargs)
        
    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            user_groups = request.user.groups.values_list('name', flat=True)
            
            if not any(group in allowed_roles for group in user_groups):
                messages.error(request, 'You don\'t have the required permissions to access this page.')
                return redirect('index')

            return view_func(request, *args, **kwargs)
        return wrapper_func
    return decorator