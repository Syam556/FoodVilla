from . import views
from django.urls import path, include


urlpatterns = [
    path('',views.myAccount),
    path('registerUser/', views.registerUser, name="registerUser"),
    path('registerVendor/', views.registerVendor, name="registerVendor"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('myAccount', views.myAccount, name="myAccount"),
    path('custDashboard', views.custDashboard, name="custDashboard"),  # dashboard  customer
    path('vendorDashboard', views.vendorDashboard, name="vendorDashboard"),  # dashboard  vendor
    path('activate/<uidb64>/<token>', views.activate, name="activate"),

    path('vendor/', include('vendor.urls')),
    path('customer/', include('customers.urls')),

]