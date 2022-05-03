from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'socketChat/index.html')

def room(request, room_name):
    return render(request, 'socketChat/room.html', {
        'room_name': room_name
    })