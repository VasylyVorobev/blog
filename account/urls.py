from django.urls import path
from django.contrib.auth.views import (LoginView,
                                       LogoutView,
                                       PasswordResetDoneView,
                                       PasswordResetConfirmView,
                                       )
from .views import RegisterView, PasswordChange, PasswordReset

app_name = 'account'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login_url'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout_url'),
    path('register/', RegisterView.as_view(), name='registration'),
    path('password_change/', PasswordChange.as_view(), name='password_change'),
    path('password_reset/', PasswordReset.as_view(), name='password_reset'),
    path('password_reset/done', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetConfirmView.as_view(), name='password_reset_complete'),

]
