from django.shortcuts import render, redirect
from .models import Meetup,Participant

from .forms import RegistrationForm

# Create your views here.

def index(request):
    meetups = Meetup.objects.all()
    return render(request, 'meetup/index.html',{
        'meetups': meetups
    })

def meetup_details(request,meetup_slug):
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        if request.method == 'GET':
            registrationForm = RegistrationForm()
        else:
            registrationForm = RegistrationForm(request.POST)
            if registrationForm.is_valid():
                user_email = registrationForm.cleaned_data['email']
                participant, _ = Participant.objects.get_or_create(email=user_email)
                selected_meetup.participant.add(participant)
                return redirect('confirm-register')

        return render(request, 'meetup/meetup-detail.html',{
                'meetup_found': True,
                'meetup': selected_meetup,
                'form': registrationForm
            })
    except Exception as exc:
        return render(request, 'meetup/meetup-detail.html',{
            'meetup_found': False
        })

def confirm_registration(request):
    return render(request, 'meetup/registration-success.html')