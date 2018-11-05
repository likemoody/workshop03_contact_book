from django.shortcuts import render
from django.views.generic.base import View
from ..models import Group


class GroupList(View):
    template_name = 'group_list.html'

    def get(self, request):
        groups = Group.objects.all().order_by('name')
        return render(request, self.template_name, {'groups': groups})

