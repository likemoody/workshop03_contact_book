from django.shortcuts import render
from django.views.generic.base import View
from ..models import Person


class ContactList(View):
    template_name = 'contact_list.html'

    def get(self, request):
        contacts = Person.objects.all().order_by('first_name')  # TODO case sensitive
        return render(request, self.template_name, {'contacts': contacts})

