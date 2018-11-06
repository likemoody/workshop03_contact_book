from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic.base import View

from ..models import Person
from ..forms import PersonAddForm


class ContactEdit(View):
    template_name = 'contact_edit.html'

    def get(self, request, cid):
        contact = Person.objects.get(pk=cid)
        first_name = contact.first_name
        last_name = contact.last_name
        description = contact.description
        profile_img = contact.profile_img
        group = contact.group.first()
        form = PersonAddForm(initial={'first_name': first_name,
                                      'last_name': last_name,
                                      'description': description,  # TODO server the image
                                      'group': group})

        return render(request, self.template_name, {'form': form, 'profile_image': profile_img})

    def post(self, request, cid):
        contact_been_modified = Person.objects.get(pk=cid)
        form = PersonAddForm(request.POST, request.FILES, instance=contact_been_modified)
        if form.is_valid():
            print(':: Contact data modified ::')
            form.save()
            messages.success(request, 'Saved successfully')
            return redirect('home')

        messages.error(request, 'Error occurred')
        return redirect('home')
