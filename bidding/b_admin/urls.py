"""bidding URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.views.generic import TemplateView
from b_admin import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('b_admin/',TemplateView.as_view(template_name="b_admin template/admin login.html"),name="b_admin"),
    path('admincheck/',views.Admincheck,name="admincheck"),
    path('adminhome/',TemplateView.as_view(template_name="b_admin template/adminhome.html"),name="adminhome"),
    path('pendingreg/',views.Pending_reg,name="pendingreg"),
    path('approved_reg/',views.approved_reg,name="approved_reg"),
    path('decline_reg/',views.decline_reg,name="decline_reg"),
    path('approved/',views.approved,name="approved"),
    path('declined/',views.declined,name="declined"),
    path('logout/',views.logout,name="logout")
]
