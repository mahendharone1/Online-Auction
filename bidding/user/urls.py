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

from user import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Buyer_Seller/',TemplateView.as_view(template_name="user templates/login_registration.html"),name="Buyer_Seller"),
    path('Registration/',TemplateView.as_view(template_name="user templates/registration.html"),name="reg"),
    path('save_reg/',views.Savereg,name="save_reg"),
    path('login_data/',views.login_data,name="login_data"),
    path('user_home/',TemplateView.as_view(template_name="user templates/user_home.html"),name="user_home"),
    path('user_logout/',views.user_logout,name="user_logout"),
    path('user_seller/',views.user_seller,name="user_seller"),
    path('save_product/',views.save_product,name="save_product"),
    path('view_product/',views.view_product,name="view_product"),
    path('Bid_product/',views.Bid_product,name="Bid_product"),
    path('bid_details/',views.bid_details,name="bid_details"),
    path('bid_show/',views.bid_show,name="bid_show"),
    path('viewbid_show/',views.viewbid_show,name="viewbid_show")
]
