from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Room, Booking, Customer
from .forms import EditRoomForm, EditBookingForm, EditCustomerForm
from django.http import JsonResponse

def home(request):
    context = {
        
        }
    return render(request, 'accommodationHome.html',context)
# View to list all rooms
def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'rooms/room_list.html', {'rooms': rooms})

# View to add a new room
def add_room(request):
    if request.method == 'POST':
        form = EditRoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accommodation:room_list')
    else:
        form = EditRoomForm()
    return render(request, 'rooms/add_room.html', {'form': form})

# View to edit an existing room
def edit_room(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    if request.method == 'POST':
        form = EditRoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('room_list')
    else:
        form = EditRoomForm(instance=room)
    return render(request, 'rooms/edit_room.html', {'form': form, 'room': room})

def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'booking/booking_list.html', {'bookings': bookings})

# View to add a new booking
def add_booking(request):
    if request.method == 'POST':
        form = EditBookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking/booking_list')
    else:
        form = EditBookingForm()
    return render(request, 'booking/add_booking.html', {'form': form})

# View to edit an existing booking
def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    if request.method == 'POST':
        form = EditBookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('booking/booking_list')
    else:
        form = EditBookingForm(instance=booking)
    return render(request, 'booking/edit_booking.html', {'form': form, 'booking': booking})



# View to list all customers
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customers/customer_list.html', {'customers': customers})

# View to add a new customer
def add_customer(request):
    if request.method == 'POST':
        form = EditCustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customers/customer_list')
    else:
        form = EditCustomerForm()
    return render(request, 'customers/add_customer.html', {'form': form})

# View to edit an existing customer
def edit_customer(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    if request.method == 'POST':
        form = EditCustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customers/customer_list')
    else:
        form = EditCustomerForm(instance=customer)
    return render(request, 'customers/edit_customer.html', {'form': form, 'customer': customer})

def delete_room(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    if request.method == 'POST':
        room.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

# Similarly, modify the delete views for bookings and customers

# View to delete a booking
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    if request.method == 'POST':
        booking.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

# View to delete a customer
def delete_customer(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    if request.method == 'POST':
        customer.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})
