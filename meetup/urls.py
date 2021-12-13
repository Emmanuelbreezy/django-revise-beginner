from django.urls import path

from . import views

urlpatterns = [
    path('meetup/', views.index, name='all-meetups'),
    path('meetup/success', views.confirm_registration, name='confirm-register'),
    path('meetup/<slug:meetup_slug>', views.meetup_details, name='meetup-detail')
]