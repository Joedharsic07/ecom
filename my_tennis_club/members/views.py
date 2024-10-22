from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth import  logout
from django.contrib import messages
from .models import Product 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.hashers import check_password
from .models import CustomUser
from django.contrib.auth import login
import random
import re
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import CustomUser
from django.http import JsonResponse
from django.views import View
from django.views.generic import DetailView


def send_otp_to_email(email):
    otp_code = str(random.randint(100000, 999999))  
    subject = 'Your OTP Code'
    message = f'Your OTP is {otp_code}'
    email_from = 'joedharsic07@gmail.com'
    send_mail(subject, message, email_from, [email])
    CustomUser.objects.update_or_create(email=email, defaults={'otp': otp_code})
def is_valid_password(password):
    if (len(password) < 8 or 
        not re.search(r'\d', password) or not re.search(r'[A-Z]', password) or not re.search(r'[\W_]', password)): 
        return False
    return True

class RegisterView(View):
    def get(self, request):
        context = {
            'errors': {},            
            'otp_sent': False,        
            'otp_verified': False,    
            'username': '',           
            'email': '',
            'password1': '',
            'password2': ''
        }
        return render(request, 'registration.html', context)

    def post(self, request):
        email = request.POST.get('email', '')
        username = request.POST.get('username', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')
        otp_sent = False
        otp_verified = request.POST.get('otp_verified') == 'True' 
        errors = {}

        if 'send_otp' in request.POST:
            if not email:
                errors['email'] = 'Email is required.'
            elif CustomUser.objects.filter(email=email, otp_verified=True).exists():
                errors['email'] = 'Email already exists. Please use a different email.'
            else:
                send_otp_to_email(email)
                otp_sent = True
                print(f"OTP sent to {email}")

        elif 'verify_otp' in request.POST:
            entered_otp = request.POST.get('otp')
            try:
                otp_user = CustomUser.objects.get(email=email)
                if otp_user.otp == entered_otp:
                    otp_user.otp_verified = True
                    otp_user.save()
                    otp_verified = True
                    otp_sent = True
                    print(f"OTP {entered_otp} verified for {email}")
                else:
                    errors['otp'] = 'Invalid OTP.'
                    otp_sent = True
            except CustomUser.DoesNotExist:
                errors['otp'] = 'OTP not found for this email.'

        elif 'register' in request.POST and otp_verified:
            if not is_valid_password(password1):
                errors['password1'] = 'Password must contain at least 8 characters, 1 number, 1 uppercase letter, and 1 special character.'
            elif password1 != password2:
                errors['password2'] = 'Passwords do not match.'
            else:
                try:
                    user = CustomUser.objects.get(email=email)
                    if user.otp_verified:
                        user.set_password(password1)
                        user.username = username
                        user.save()

                        authenticated_user = authenticate(email=email, password=password1)
                        if authenticated_user:
                            login(request, authenticated_user)
                            return redirect('home')  
                        else:
                            errors['form'] = 'Authentication failed.'
                    else:
                        errors['otp'] = 'OTP not verified.'
                except CustomUser.DoesNotExist:
                    errors['form'] = 'User with this email does not exist.'
        context = {
            'errors': errors,
            'otp_sent': otp_sent,
            'otp_verified': otp_verified,
            'username': username,
            'email': email,
            'password1': password1,
            'password2': password2
        }
        return render(request, 'registration.html', context)

class loginview(View):
    def post(self,request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email and password:
            user = authenticate(request, username=email, password=password)  
            if user is not None:
                login(request, user)  
                return redirect('home')
            messages.error(request, "Invalid email or password.")
        return render(request, 'login.html')
    def get(self,request):
        return render(request, 'login.html')  

class logoutview(View):
    def get (self,request):
        logout(request)
        return redirect('login')
    
class ForgotPasswordView(View):
    def get(self, request):
        context = {
            'errors': {},
            'otp_sent': False,
            'otp_verified': False,
            'email': '',
            'new_password': '',
            'confirm_password': ''
        }
        return render(request, 'forgotpassword.html', context)

    def post(self, request):
        email = request.POST.get('email', '')
        new_password = request.POST.get('new_password', '')
        confirm_password = request.POST.get('confirm_password', '')
        otp_verified = request.POST.get('otp_verified') == 'True'
        otp_sent = False
        errors = {}
        
        email_exists = CustomUser.objects.filter(email=email).exists()
        if 'send_otp' in request.POST:
            if not email:
                errors['email'] = 'Email is required.'
            elif not email_exists:
                errors['email'] = 'Email not found. Please register first.'
            else:
                send_otp_to_email(email)
                otp_sent = True
                print(f"OTP sent to {email}")

        elif 'verify_otp' in request.POST:
            entered_otp = request.POST.get('otp')
            if email:
                try:
                    otp_user = CustomUser.objects.get(email=email)
                    if otp_user.otp == entered_otp:
                        otp_verified = True
                        otp_sent = True
                        print(f"OTP {entered_otp} verified for {email}")
                    else:
                        errors['otp'] = 'Invalid OTP.'
                        otp_sent = True
                        print(f"Invalid OTP: {entered_otp} for {email}")
                except CustomUser.DoesNotExist:
                    errors['otp'] = 'OTP not found for this email.'
                    otp_sent = True
                    print(f"OTP not found for {email}")
            else:
                errors['otp'] = 'Email is required for OTP verification.'
        elif 'reset_password' in request.POST and otp_verified:
            if (len(new_password) < 8 or 
                not re.search(r'\d', new_password) or 
                not re.search(r'[A-Z]', new_password) or 
                not re.search(r'[!@#$%^&*()_+]', new_password)):
                errors['new_password'] = 'Password must contain at least 8 characters, 1 number, 1 uppercase letter, and 1 special character.'
            elif new_password != confirm_password:
                errors['confirm_password'] = 'Passwords do not match.'
            else:
                try:
                    user = CustomUser.objects.get(email=email)
                    user.set_password(new_password)
                    user.save()
                    messages.success(request, 'Your password has been successfully reset.')
                    return redirect('login')
                except CustomUser.DoesNotExist:
                    errors['email'] = 'Email not found.'
        context = {
            'errors': errors,
            'otp_sent': otp_sent,
            'otp_verified': otp_verified,
            'email': email,
            'new_password': new_password,
            'confirm_password': confirm_password,
        }
        return render(request, 'forgotpassword.html', context)

def men_view(request):
    men_products = Product.objects.filter(category='men')  
    return render(request, 'men.html', {'products': men_products})

def women_view(request):
    women_products = Product.objects.filter(category='women')  
    return render(request, 'women.html', {'products': women_products})

def product_detail(request, pk):
    product = get_object_or_404(Product, id=pk)
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)[:4]
    context = {
        'product': product,
        'related_products': related_products,
    }
    return render(request, 'viewproduct.html', context)

def category_page(request, category_name):
    products = Product.objects.filter(category=category_name.lower())
    return render(request, 'categorypage.html', {'products': products, 'category_name': category_name})


class homeview(LoginRequiredMixin,View):
    def get(self, request):
        return render(request, 'home.html')

class editprofileview(LoginRequiredMixin,View):
    def get(self, request):
        user = request.user
        return render(request, 'edit-profile.html', {'user': user})
    def post(self,request):
        user = request.user
        user.username = request.POST.get('username')
        user.first_name=request.POST.get('first_name')
        user.last_name=request.POST.get('last_name')
        user.email = request.POST.get('email')
        if request.FILES.get('profile_picture'):
            user.profile_picture = request.FILES['profile_picture']
        user.save()  
        return redirect('home') 
        
@login_required
def change_password(request):
    if request.method == 'POST' :
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password1')
        confirm_password = request.POST.get('new_password2')

        user = request.user
        errors = {}

        try:
            if not check_password(old_password, user.password):
                errors['old_password'] = 'Old password is incorrect.'
            if new_password != confirm_password:
                errors['new_password'] = 'New password and Confirm password do not match.'
            if len(new_password) < 8:
                errors['new_password_length'] = 'New password must be at least 8 characters long.'
            if errors:
                return JsonResponse({'success': False, 'errors': errors})
            user.set_password(new_password)
            user.save()

            update_session_auth_hash(request, user)

            return JsonResponse({'success': True, 'message': 'Password has been changed successfully!'})

        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=500)

    return JsonResponse({'success': False, 'message': 'Invalid request method.'}, status=400)

class UserProfileView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'profile.html'
    context_object_name = 'user_profile'

    def get_object(self):
        return get_object_or_404(CustomUser, email=self.request.user.email)