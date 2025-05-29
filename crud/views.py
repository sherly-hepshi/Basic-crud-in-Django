from django.shortcuts import render, redirect
from bson.objectid import ObjectId
from . import dbcon

def read_bookings(request):
    bookings = list(dbcon.col.find())
    for booking in bookings:
        booking['id'] = str(booking['_id'])
    return render(request, 'read.html', {'bookings': bookings})

def create_booking(request):
    if request.method == 'POST':
        dbcon.col.insert_one({
            'passenger_name': request.POST.get('passenger_name',''),
            'train_name': request.POST.get('train_name',''),
            'source': request.POST.get('source',''),
            'destination': request.POST.get('destination',''),
            'travel_date': request.POST.get('travel_date','')
        })
        return redirect('read_bookings')
    return render(request, 'create.html')

def update_booking(request, booking_id):
    booking = dbcon.col.find_one({'_id': ObjectId(booking_id)})
    if request.method == 'POST':
        dbcon.col.update_one(
            {'_id': ObjectId(booking_id)},
            {'$set': {
                'passenger_name': request.POST['passenger_name'],
                'train_name': request.POST['train_name'],
                'source': request.POST['source'],
                'destination': request.POST['destination'],
                'travel_date': request.POST['travel_date']
            }}
        )
        return redirect('read_bookings')
    booking['id'] = str(booking['_id'])
    return render(request, 'update.html', {'booking': booking})

def delete_booking(request, booking_id):
    if request.method == 'POST':
        dbcon.col.delete_one({'_id': ObjectId(booking_id)})
    return redirect('read_bookings')
