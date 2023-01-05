from django.shortcuts import render
from .forms import UserCreateForm
from django.shortcuts import redirect

# Create your views here.
def SignUp(request):
    if request.method == 'POST':
        user_form = UserCreateForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save(commit=True)
            # user.set_password(user.password)
            # user.save()
            print("user created")
            return redirect('accounts:login')
        else:
            print(user_form.errors)
    else:
        user_form = UserCreateForm()
    return render(request, 'accounts/signup.html', {'form':user_form})