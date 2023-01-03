from django.shortcuts import render
from .forms import BasicInfo, DateForm, TimeForm
from django.http import HttpResponse, HttpResponseRedirect
from .models import BookingSection
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def basic_information(request):
    if request.method == 'POST':
        form = BasicInfo()
    else:
        form = BasicInfo()
    context = {'form': form}

    return render(request, 'reservation/basicinfo.html', context)


def select_date(request):
    if request.method == 'POST':
        form = DateForm()
        basic_info_form = BasicInfo(request.POST)
        print(request.POST)
    else:
        form = DateForm()
        basic_info_form = BasicInfo()

    context = {
        'form': form,
        'basic_info_form': basic_info_form,
    }
    return render(request, 'reservation/pickdate.html', context)


def select_time(request):
    if request.method == 'POST':
        TIME_CHOICES = [
            ["9:00", "9:00"],
            ["10:00", "10:00"],
            ["11:00", "11:00"],
            ["13:00", "13:00"],
            ["14:00", "14:00"],
            ["15:00", "15:00"],
            ["16:00", "16:00"],
            ["17:00", "17:00"],
        ]
        form = TimeForm()
        form.fields['time'].choices = TIME_CHOICES
        basic_info_form = BasicInfo(request.POST)
        date = DateForm(request.POST)
        required_date = date['date'].value()

        reserved_set = BookingSection.objects.all()

        booked_date_time = []
        for sets in reserved_set:
            days = sets.date
            reserved_days = str(days)
            reserved_time = sets.time
            booked_date_time.append(reserved_days)
            booked_date_time.append(reserved_time)

        list_of_all_reservation = list()
        chunk_size = 2
        for i in range(0, len(booked_date_time), chunk_size):
            list_of_all_reservation.append(booked_date_time[i:i+chunk_size])

        for one_reservation in list_of_all_reservation:
            if one_reservation[0] not in required_date:
                form.fields['time'].choices = TIME_CHOICES
            else:
                available_times = []
                for one_choice in TIME_CHOICES:
                    if one_reservation[1] in one_choice:
                        pass
                    else:
                        available_times.append(one_choice)
                form.fields['time'].choices = available_times
    else:
        basic_info_form = BasicInfo()
        date = DateForm()
        form = TimeForm()

    context = {
        'form': form,
        'date_form': date,
        'basic_info_form' : basic_info_form,
    }
    return render(request, 'reservation/picktime.html', context)


def save(request):
    if request.method == 'POST':
        basic_info = BasicInfo(request.POST)
        date_form = DateForm(request.POST)
        time_form = TimeForm(request.POST)

        if basic_info.is_valid() and date_form.is_valid() and time_form.is_valid():
            reserved_subject = basic_info.cleaned_data['subject']
            reserved_name = basic_info.cleaned_data['user_name']
            reserved_email = basic_info.cleaned_data['user_email']
            reserved_mobile = basic_info.cleaned_data['user_mobile']

            reserved_subject = basic_info['subject'].value()
            reserved_name = basic_info['user_name'].value()
            reserved_email = basic_info['user_email'].value()
            reserved_mobile = basic_info['user_mobile'].value()
            reserved_date = date_form['date'].value()
            reserved_time = time_form['time'].value()

            reservation = BookingSection(subject=reserved_subject, user_name=reserved_name, user_email=reserved_email, user_mobile=reserved_mobile, date=reserved_date, time=reserved_time)
            reservation.save()

            return HttpResponse("Rezervace byla úspěšně provedena.")

    else:
        basic_info = BasicInfo()
        date_form = DateForm()
        time_form = TimeForm()

    context = {
        'basic_info': basic_info,
        'date_form': date_form,
        'time_form': time_form,
    }
    return render(request, 'reservation/save.html', context)

@login_required(login_url='/beauty-salon/login/')
def all_reservations(request):
    list_of_all_reservations = BookingSection.objects.all()
    context = {'list_of_all_reservations':list_of_all_reservations}

    return render(request, 'reservation/reservations_list.html', context)

def delete_reservation(request, id):
    BookingSection.objects.filter(id=id).delete()
    
    return HttpResponseRedirect(reverse('reservationslist'))
