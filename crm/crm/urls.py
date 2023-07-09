from django.contrib import admin
from django.urls import path, include
# for log-in page import view
from django.contrib.auth import views

# import view
from core.views import index, about
from userprofile.views import signup

urlpatterns = [
    path('dashboard/lead/', include('lead.urls')),#path for add leads
    path('dashboard/', include('dashboard.urls')),#path for dashboard
    path('dashboard/clients/', include('clients.urls')),#path for clients list
    path('admin/', admin.site.urls),#path for admin manager
    path('', index, name='index'),#path for index page(start page)
    path('about/', about, name='about'), #path for about info
    path('sign_up/', signup, name='signup'), #path for signup
    path('log_in/', views.LoginView.as_view(template_name='userprofile/login.html'), name='login'),#path for login with django class
    path('log_out/', views.LogoutView.as_view(), name='logout'),#path for logot
]
