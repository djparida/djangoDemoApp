from django.http import JsonResponse
from django.shortcuts import render
from .models import Order
from django.core import serializers
from .forms import OrderForm, UserRegistrationForm
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.template import loader
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, reverse




def dashboard_with_pivot(request):
    return render(request, 'dashboard_with_pivot.html', {})

def pivot_data(request):
    dataset = Order.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)

def addOrder(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("added successfully!!!")
    return render(request, 'addOrder.html', {'form': OrderForm()})


def sendEmail(request):
    print("preparing to send mail")
    name="Sambit Kumar Sahoo"
    domain="http://weown.properties"
    body="http://weown.properties"
    body = loader.render_to_string('email.html', {'name':name,'domain':domain,'body':body})
    send_mail(
        subject = 'Weown Properties',
        message='',
        html_message = body,
        from_email = settings.EMAIL_HOST_USER,
        recipient_list = ['dj@yopmail.com','paridadibyajyoti4@gmail.com','sambitsahoo.sks@gmail.com'],
        fail_silently = False,
    )
    return HttpResponse("hii, Mail sent!!")

def index(request):
    return render(request, 'home.html')


def userRegistration(request):
    if request.method=='POST':
        user = User(
            username = request.POST.get('username'),
            first_name = request.POST.get('first_name'),
            last_name = request.POST.get('last_name'),
            email = request.POST.get('email')
        )
        user.set_password(request.POST.get('password'))
        user.is_active = True
        user.save()
        return redirect(index)
    return render(request, 'registration.html')

def userLogin(request):
    if request.method == 'POST':
        try:
            user = User.objects.get(username=request.POST.get('username'))
            if user.check_password(request.POST.get('password')):
                if (user.is_active):
                    request.session['logged_User']=[user.username, user.first_name, user.last_name, user.email]
                    return redirect(dashboard)
                return HttpResponse("User is inactive!!")
            return HttpResponse("Please Enter the correct Password")
        except Exception as e:
            return  HttpResponse("Exception: {}".format(e))
    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def logout(request):
    request.session.clear()
    return redirect(index)

