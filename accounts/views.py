from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.core.mail import send_mail

# Create your views here.
def login(request):
    if request.method == 'POST':
        username= request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        # print(user)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are logged in")
            return redirect('latest-posts')
        else:
            messages.error(request, "Invalid login credentials")
            return redirect('login')
    else:
        return render(request,'accounts/login.html')

def signup(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'username already exists')
            return redirect('sign-up')
        else:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
                return redirect('sign-up')
            else:
                user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username, email=email, password=password)
                user.save()
                messages.success(request, 'Account created successfully')
                message_body_email = f"""Hi, {firstname}
                                            Welcome to Divine Ayurveda

                                        Your account has been successfully created.
                                        Now you can sign in with your email and password."""
                # email = User.objects.get(email)
                print(email)
                send_mail(
                    "Divine Ayurveda Account Created",
                    message_body_email,
                    'pateljay.india@gmail.com',
                    [email],
                    fail_silently = False,
                )
                return redirect('login')
    else:
        return render(request, 'accounts/signup.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are successfully logout')
    return redirect('latest-posts')