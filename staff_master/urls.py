"""staff_master URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from authentication import views as views_auth
from check_in_out import views as views_check_in_out

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views_auth.login_view), 
    path('logout/',views_auth.logout_view),
    path('register/',views_auth.register), 
    path('faq/',views_check_in_out.faq), 
    path('contact/',views_check_in_out.contact_form), 
    path('check_in/',views_check_in_out.check_in), 
    path('check_out/',views_check_in_out.check_out),
    path('profile/',views_check_in_out.profile)
    
]
