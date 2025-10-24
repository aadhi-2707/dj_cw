from django.shortcuts import render
from .forms import LoginForm

def login_view(request):
    message = ""
    email = ""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            message = "Thank you for logging in..."
            return render(request, 'thankyou.html', {'email': email, 'message': message})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

