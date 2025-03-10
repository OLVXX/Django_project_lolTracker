from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views
from accounts import views as account_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('analysis/', include('analysis.urls')),
    path('', RedirectView.as_view(url='analysis/', permanent=True)),
    path('login/', auth_views.LoginView.as_view(template_name='analysis/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', account_views.register_view, name='register'),
]
