from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic.base import View

from ..models import Person
from ..forms import ContactAddress, ContactEmail, ContactTelephone


class ContactEdit(View):
    template_name = 'contact_additional.html'

    def get(self, request, cid, additional_info=None):
        if additional_info == 'add-address':
            form = ContactAddress()
            return render(request, self.template_name, {'form': form})
        if additional_info == 'add-email':
            form = ContactEmail()
            return render(request, self.template_name, {'form': form})
        if additional_info == 'add-tel-no':
            form = ContactTelephone()
            return render(request, self.template_name, {'form': form})

        return redirect('home')

    def post(self, request, cid, additional_info=None):
        contact = Person.objects.get(pk=cid)
        form = None
        if additional_info == 'add-address':
            form = ContactAddress(request.POST)
        if additional_info == 'add-email':
            form = ContactEmail(request.POST)
        if additional_info == 'add-tel-no':
            form = ContactTelephone(request.POST)

        if form.is_valid():
            if additional_info == 'add-address':
                contact.address.create(city=request.POST['city'],
                                       street=request.POST['street'],
                                       building_no=request.POST['building_no'],
                                       apt_no=request.POST['apt_no'],
                                       label=request.POST['label'])

            if additional_info == 'add-email':
                contact.person_id_email.create(email=request.POST['email'],
                                               label=request.POST['label'])

            if additional_info == 'add-tel-no':
                contact.person_id_tel.create(tel_no=request.POST['tel_no'],
                                             label=request.POST['label'])

            print(':: Data added ::')
            messages.success(request, 'Saved successfully')
            return redirect('home')

        messages.error(request, 'Error occurred')
        return redirect('home')
