from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from .models import Contacts, Laboratory, Production, Company, Advantages, MainPagePhoto, MainPageDescription
from about.forms import ContactForm
from django.http import HttpResponse
from Grite.settings import RECIPIENTS_EMAIL, DEFAULT_FROM_EMAIL


def index(request):

    advantages = Advantages.objects.all()
    descriptions = MainPageDescription.objects.all()
    context = {
        'advantages': advantages,
        'descriptions': descriptions,
    }
    count = MainPagePhoto.objects.all().count()
    if count == 1:
        main_page_photo = MainPagePhoto.objects.all().latest('id')
        context['main_page_photo'] = main_page_photo
    elif count > 1:
        main_page_photos = MainPagePhoto.objects.all()[:len(MainPagePhoto.objects.all())-1]
        main_page_photo_latest = MainPagePhoto.objects.all().latest('id')
        context['main_page_photos'] = main_page_photos
        context['main_page_photo_latest'] = main_page_photo_latest

    return render(request, 'about/index.html', context)


def about(request):
    laboratory = Laboratory.objects.all()
    production = Production.objects.all()
    company = Company.objects.all()

    context = {
        'laboratory': laboratory,
        'production': production,
        'company': company,
    }

    return render(request, 'about/about.html', context)


def contacts(request):
    if request.method == 'GET':
        form = ContactForm()
    elif request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['from_email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']

            try:
                send_mail(f'Сообщение от {name} с адреса {from_email}, телефон для связи {phone}', message,
                          DEFAULT_FROM_EMAIL, RECIPIENTS_EMAIL)
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма')
            return redirect('success')

    else:
        return HttpResponse('Неверный запрос')
    contact_info = Contacts.objects.all().latest('id')
    context = {'contact_info': contact_info, 'form': form}

    return render(request, 'about/contacts.html', context)


def success(request):
    return render(request, 'about/success.html')


