from django.urls import path
from . import views
from core.views import travel_list

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('travels/', travel_list, name='travel_list'),
    path('book/<int:travel_id>/', views.book_travel, name='book_travel'), 
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('cancel/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),

]
