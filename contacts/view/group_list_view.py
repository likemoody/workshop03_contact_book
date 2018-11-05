from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic.base import View
from ..forms import GroupForm
from ..models import Group


class GroupList(View):
    template_name = 'group_list.html'

    def get(self, request):
        form = GroupForm()
        groups = Group.objects.all().order_by('name')
        return render(request, self.template_name, {'groups': groups, 'form': form})

    def post(self, request):
        form = GroupForm(request.POST)
        if form.is_valid():
            Group.objects.create(name=form.cleaned_data['name'])
            print(':: Group added to database ::')
            messages.success(request, 'Saved successfully')
            return redirect('group-list')

        messages.error(request, 'Error occurred')
        return redirect('group-list')
