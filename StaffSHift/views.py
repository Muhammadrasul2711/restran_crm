from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_requierd
from Crmapp.models import StaffSHift
from django.http import HttpResponse



def StaffSHiftCreate(request):
    if request.method == 'POST':
        staff=staff.objects.create_staff(

        )

