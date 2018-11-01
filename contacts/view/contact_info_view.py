from django.shortcuts import render
from django.views.generic.base import View
from ..models import Person


class ContactInfo(View):
    template_name = 'contact_info.html'

    def get(self, request, cid):
        contact = Person.objects.get(pk=cid)
        group = contact.group.first()
        return render(request, self.template_name, {'contact': contact, 'group': group})

