from django.shortcuts import render
from django.views.generic.base import View
from ..models import Person


class ContactInfo(View):
    template_name = 'contact_info.html'

    def get(self, request, cid):
        contact = Person.objects.get(pk=cid)
        groups = contact.group.all()
        addresses = contact.address.all()
        emails = contact.person_id_email.all()
        telephones = contact.person_id_tel.all()
        return render(request, self.template_name, {'contact': contact,
                                                    'groups': groups,
                                                    'addresses': addresses,
                                                    'emails': emails,
                                                    'telephones': telephones})

