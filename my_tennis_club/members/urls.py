from django.urls import path
from .import views
from.views import loginview,RegisterView,ForgotPasswordView,editprofileview, logoutview,homeview
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('', loginview.as_view(), name='login'),
    path('forgotpassword/', ForgotPasswordView.as_view(), name='forgotpassword'),
    path('logout/', logoutview.as_view(), name='logout'),
    path('men/', views.men_view, name='men'),  
    path('home/', homeview.as_view(), name='home'),
    path('edit_profile/', editprofileview.as_view(), name='edit_profile'), 
    path('change_password_ajax/', views.change_password, name='change_password_ajax'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('category/<str:category_name>/', views.category_page, name='category_page'),
    path('women/', views.women_view, name='women'),
    
]
