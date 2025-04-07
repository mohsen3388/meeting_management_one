import sys
from django.shortcuts import redirect, render, get_object_or_404
from .form import MeetingForm
from .models import Meeting, Room
#from django.contrib.admin.views.decorators import \

def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, 'meetings/detail.html', {"meeting": meeting})

def rooms_list(request):
    return render(request, 'meetings/rooms_list.html', {"rooms": Room.objects.all()})

def form(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        requesteddate = request.POST.get('date')
        #requestedhour = request.POST.get('hour')
        submitedroom = (Meeting.objects.filter(room=request.POST.get('room')))
      #  allsubmitedhour = (Meeting.objects.filter(hour=submitedroom).values_list('hour', flat=True))[0]
       # allsubmiteddate = (Meeting.objects.filter(date=submitedroom).values_list('date', flat=True))[0]
        print (submitedroom)

        sys.stdout.write ("ffffffffffffffffffffffffffffffffffffffffff")
        #if (not (submiteddate)): # Means the Query is empty and not used before
         #   sys.stdout.write ("repeated hour")
        print = ("dffffffffffffffffffffffffff")
      #  print (requestedhour)
       # print (requesteddate)

        if form.is_valid():
            form.save()
            return redirect('welcome')

    else:
        form = MeetingForm()

    return render(request, 'meetings/form.html', {"form": form})

def sendsms (request):
    return render (request, 'meetings/AddDevice_html.html')