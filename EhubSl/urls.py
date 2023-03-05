from django.urls import path
from . import views
from EhubSl.admin import admin_site


urlpatterns = [
    path('',views.HomeView,name='home'),
    path('Register/',views.RegisterView,name='register'),
    path('login/',views.LoginView,name='login' ),
    path('Dashboard/',views.dashboard,name='dashboard'),
    path('logout/', views.logoutView,name='logout'),
    path('error/', views.unsucces,name='unsucces'),
    path('loginError/', views.login_err ,name='login_error'),
    path('user-panel/', views.userpanel,name='users'),
    path('message-panel/', views.messagepanel,name='messages'),
    path('Ehub-admin/',admin_site.urls),

]