from django.urls import path
from .import views
from.views import loginview,RegisterView,ForgotPasswordView,editprofileview, logoutview,homeview,UserProfileView,ChangePasswordView
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('', loginview.as_view(), name='login'),
    path('forgotpassword/', ForgotPasswordView.as_view(), name='forgotpassword'),
    path('logout/', logoutview.as_view(), name='logout'),
    path('men/', views.men_view, name='men'),  
    path('home/', homeview.as_view(), name='home'),
    path('editprofile/', editprofileview.as_view(), name='editprofile'), 
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),   
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('category/<str:category_name>/', views.category_page, name='category_page'),
    path('women/', views.women_view, name='women'),   
    path('kids/', views.kids_view, name='kids'),  
]
