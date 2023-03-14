from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('/listing', views.listing, name='listing'),
    path('/unit/<int:pk>', views.unit, name='unit'),
    path('/about', views.about, name='about'),
    
    path('/post-ad', views.post_ad, name='post_ad'),
    path('/update-ad/<int:pk>', views.update_ad, name='update_ad'),
    path('/delete-ad/<int:pk>', views.delete_ad, name='delete_ad'),
    
    path('/login', views.loginPage, name='login'),
    path('/logout', views.logoutUser, name='logout'),
    path('/select-account-type', views.selectAccountType, name='select_account_type'),
    path('/create-user-account', views.registerUserAccount, name='create_user_account'),
    path('/create-realtor-account', views.registerRealtorAccount, name='create_realtor_account'),
    
    # path('/register', views.registerUser, name='register'),
    
    path('/threads', views.threadPage, name='thread_page'),
    path('/messagePage/<str:username>', views.messagePage, name='message_page'),
    
    path('/profile/<int:pk>', views.accountProfile, name='profile_page'),
    path('/profile-update', views.updateProfile, name='profile_update'),

]