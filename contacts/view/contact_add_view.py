from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic.base import View

from ..models import Group
from ..forms import PersonAddForm


class ContactAdd(View):
    template_name = 'contact_add.html'

    def get(self, request):
        groups = [group.name for group in Group.objects.all()]  # TODO issue no 1
        form = PersonAddForm(initial={'group': groups})

        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = PersonAddForm(request.POST, request.FILES)
        if form.is_valid():
            print(':: Contact added to database ::')
            form.save()
            messages.success(request, 'Saved successfully')
            return redirect('home')

        messages.error(request, 'Error occurred')
        return redirect('home')
