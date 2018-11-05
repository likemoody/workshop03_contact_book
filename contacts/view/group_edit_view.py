from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic.base import View

from ..forms import GroupForm
from ..models import Group


class GroupEdit(View):
    template_name = 'group_edit.html'

    def get(self, request):
        group = Group.objects.get(pk=request.GET.get('gid'))
        form = GroupForm(initial={'name': group.name})
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = GroupForm(request.POST)

        if form.is_valid():
            group_been_modified = Group.objects.get(pk=request.GET.get('gid'))
            group_been_modified.name = form.cleaned_data['name']
            group_been_modified.save()
            print(':: Group modified ::')
            messages.success(request, 'Group has been modified successfully')
            return redirect('group-list')

        messages.error(request, 'Error occurred')
        return render(request, self.template_name, {'form': form})
