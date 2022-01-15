from django.shortcuts import redirect

def admin_only(view_func):
    def wrapper_function(request):
        group=None
        if request.user.groups.exists():
            group=request.user.groups.all()[0].name

        if group == 'student':
            return redirect('student')

        if group == 'teacher':
            return redirect('teacher')

        if group == 'admin' :
            return view_func(request)  
    return wrapper_function          

