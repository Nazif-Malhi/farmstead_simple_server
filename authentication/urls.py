from django.urls import path, include
from authentication.views import UserRegistrationView, UserLoginView, UserProfileView, UserChangePasswordView, SentPasswordResetView, ResetPasswordView, get, UpdateProfileView, UserVerifiedView,  UserVerfiedUpdateView
urlpatterns = [

    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('change_password/', UserChangePasswordView.as_view(),
         name='change_password'),
    path('reset-email/', SentPasswordResetView.as_view(), name='reset-email'),
    path('reset-password/<uid>/<token>/',
         ResetPasswordView.as_view(), name="reset_password"),
    path('farmers/', get, name="index"),
    path('users/update-profile/<id>/', UpdateProfileView.as_view(), name="update_profile"),
    path('verify-account/', UserVerifiedView.as_view(), name="verify-mail"),
    path('verify-account-request/<uid>/<token>/',
         UserVerfiedUpdateView.as_view(), name="verify-account")
]