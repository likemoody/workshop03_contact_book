import os
from django.contrib import messages
from django.shortcuts import redirect
from ..models import Person
from django.conf import settings


def contact_delete(request, cid):
    try:
        contact_to_delete = Person.objects.get(pk=cid)
        os.remove(f"{settings.BASE_DIR}{contact_to_delete.profile_img.url}")
        contact_to_delete.delete()
        messages.success(request, 'Contact has been removed')
        return redirect('home')
    except Exception as e:
        print(e)
        messages.error(request, 'Error occurred')
        return redirect('home')
