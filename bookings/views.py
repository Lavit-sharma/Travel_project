from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import UserRegisterForm, BookingForm
from .models import Booking, TravelOption


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'bookings/register.html', {'form': form})


def travel_options_list(request):
    travel_type = request.GET.get('type')
    source = request.GET.get('source')
    destination = request.GET.get('destination')
    date = request.GET.get('date')

    travel_options = TravelOption.objects.all()

    if travel_type and travel_type != 'All':
        travel_options = travel_options.filter(type=travel_type)
    if source:
        travel_options = travel_options.filter(source__icontains=source)
    if destination:
        travel_options = travel_options.filter(destination__icontains=destination)
    if date:
        travel_options = travel_options.filter(datetime__date=date)

    context = {
        'travel_options': travel_options,
        'travel_type': travel_type or '',
        'source': source or '',
        'destination': destination or '',
        'date': date or '',
    }
    return render(request, 'bookings/travel_options_list.html', context)


@login_required
def book_travel(request, travel_id):
    travel_option = get_object_or_404(TravelOption, pk=travel_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            number_of_seats = form.cleaned_data['number_of_seats']
            if number_of_seats > travel_option.available_seats:
                form.add_error('number_of_seats', 'Not enough seats available.')
            else:
                total_price = number_of_seats * travel_option.price
                booking = Booking.objects.create(
                    user=request.user,
                    travel_option=travel_option,
                    number_of_seats=number_of_seats,
                    total_price=total_price,
                    booking_date=timezone.now(),
                    status='Confirmed'
                )
                travel_option.available_seats -= number_of_seats
                travel_option.save()
                return redirect('user_bookings')
    else:
        form = BookingForm()
    return render(request, 'bookings/book_travel.html', {'form': form, 'travel_option': travel_option})


@login_required
def user_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-booking_date')
    return render(request, 'bookings/user_bookings.html', {'bookings': bookings})


@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id, user=request.user)
    if booking.status == 'Confirmed':
        booking.status = 'Cancelled'
        booking.save()
        travel_option = booking.travel_option
        travel_option.available_seats += booking.number_of_seats
        travel_option.save()
    return HttpResponseRedirect(reverse('user_bookings'))
