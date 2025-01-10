from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('analyze/', views.analyze_matches, name='analyze_matches'),
    path('recommendations/', views.get_champion_recommendations, name='get_recommendations'),
    path('login/', views.CustomLoginView.as_view(), name='login'), 
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'), 
    
    # Password Reset URLs
    path('password_reset/', 
        auth_views.PasswordResetView.as_view(template_name='analysis/password_reset.html'),
        name='password_reset'),
    path('password_reset/done/', 
        auth_views.PasswordResetDoneView.as_view(template_name='analysis/password_reset_done.html'),
        name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='analysis/password_reset_confirm.html'),
        name='password_reset_confirm'),
    path('reset/done/',
        auth_views.PasswordResetCompleteView.as_view(template_name='analysis/password_reset_complete.html'),
        name='password_reset_complete'),
]