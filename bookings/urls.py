from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='bookings/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('', views.travel_options_list, name='travel_options_list'),
    path('book/<int:travel_id>/', views.book_travel, name='book_travel'),
    path('mybookings/', views.user_bookings, name='user_bookings'),
    path('cancel/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),



]
