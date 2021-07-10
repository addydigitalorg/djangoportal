"""djangoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from djangoproject import views

admin.site.site_header = 'djangoproject Operation Admin'     # default: "Django Administration"
admin.site.index_title = 'djangoproject Operation'           # default: "Site administration"
admin.site.site_title = 'Welcome to djangoproject Operation' # default: "Django site admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('signup', views.userSignUp, name='signup'),
    path('login', views.userlogin, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('djangoproject-view', views.crud_view, name='crud-view'),
    path('balance_sheet', views.balance_sheet, name='balance_sheet'),
    
]
