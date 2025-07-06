from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserRegistrationForm, UserUpdateForm
from .models import TravelOption, Booking
from .forms import BookingForm
from django.db.models import Q
from django.utils import timezone
from django.db import transaction  
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # redirects to Django’s built-in login page
    else:
        form = CustomUserRegistrationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)
    
    return render(request, 'profile.html', {'form': form})

def travel_list(request):
    travel_type = request.GET.get('type')
    source = request.GET.get('source')
    destination = request.GET.get('destination')
    date = request.GET.get('date')

    travels = TravelOption.objects.filter(date_time__gte=timezone.now()).order_by('date_time')

    if travel_type:
        travels = travels.filter(type=travel_type)
    if source:
        travels = travels.filter(source__icontains=source)
    if destination:
        travels = travels.filter(destination__icontains=destination)

    if date:
        try:
            travels = travels.filter(date_time__date=date)
        except ValueError:
            pass  # silently ignore invalid date


    paginator = Paginator(travels, 5)  # Show 5 travels per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'travels': page_obj,
    }
    return render(request, 'travel_list.html', context)




@login_required
def book_travel(request, travel_id):
    if request.method == 'POST':
        with transaction.atomic():
            travel = TravelOption.objects.select_for_update().get(pk=travel_id)

            if travel.date_time < timezone.now():
                messages.error(request, "❌ You cannot book a travel that has already passed.")
                return redirect('travel_list')

            form = BookingForm(request.POST)
            if form.is_valid():
                seats_requested = form.cleaned_data['seats']

                travel.refresh_from_db()
                if seats_requested > travel.available_seats:
                    form.add_error('seats', 'Not enough seats available.')
                else:
                    booking = form.save(commit=False)
                    booking.user = request.user
                    booking.travel = travel
                    booking.total_price = seats_requested * travel.price

                    travel.available_seats -= seats_requested
                    travel.save()
                    booking.save()

                    messages.success(request, 'Booking successful!')
                    return redirect('travel_list')
    else:
        travel = get_object_or_404(TravelOption, pk=travel_id)  # 🔁 No select_for_update on GET
        form = BookingForm()

    return render(request, 'book_travel.html', {'form': form, 'travel': travel})



@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).select_related('travel')
    return render(request, 'my_bookings.html', {'bookings': bookings, 'now': timezone.now()})



@require_POST  # 👈 ensures only POST allowed
@login_required
def cancel_booking(request, booking_id):
    booking = Booking.objects.get(pk=booking_id, user=request.user)

    if booking.status == 'Confirmed' and booking.travel.date_time > timezone.now():
        booking.status = 'Cancelled'
        booking.travel.available_seats += booking.seats
        booking.travel.save()
        booking.save()
        messages.success(request, 'Booking cancelled successfully.')
    else:
        messages.error(request, 'Booking cannot be cancelled.')

    return redirect('my_bookings')


def contact(request):
    if request.method == "POST":
        messages.success(request, "Thanks for reaching out! We'll get back to you soon.")
        return redirect('home')  # or 'contact' if separate page
    return redirect('home')  # fallback

def about(request):
    return render(request, 'about.html')
