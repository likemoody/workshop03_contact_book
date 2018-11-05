from django.contrib import messages
from django.shortcuts import redirect
from ..models import Group


def group_delete(request, gid):
    try:
        group_to_delete = Group.objects.get(pk=gid)
        group_to_delete.delete()
        messages.success(request, 'Group has been removed successfully')
        return redirect('group-list')
    except Exception as e:
        print(e)
        messages.error(request, 'Error occurred')
        return redirect('group-list')
