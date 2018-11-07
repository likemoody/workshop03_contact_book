"""contactbook URL Configuration

The `urlpatterns` list routes URLs to view. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function view
    1. Add an import:  from my_app import view
    2. Add a URL to urlpatterns:  path('', view.home, name='home')
Class-based view
    1. Add an import:  from other_app.view import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from .view import (contact_list_view,
                   contact_add_view,
                   contact_info_view,
                   contact_edit_view,
                   contact_additional_view,
                   contact_delete_view,
                   group_list_view,
                   group_edit_view,
                   group_delete_view,
                   contact_search_view)
from django.urls import path

urlpatterns = [
    # Contacts
    path('', contact_list_view.ContactList.as_view(), name='home'),
    path('new/', contact_add_view.ContactAdd.as_view(), name='contact-new'),
    path('show/<int:cid>', contact_info_view.ContactInfo.as_view(), name='contact-info'),
    path('modify/<int:cid>', contact_edit_view.ContactEdit.as_view(), name='contact-edit'),
    path('modify/<int:cid>/<str:additional_info>', contact_additional_view.ContactEdit.as_view(),
         name='contact-additional'),
    path('delete/<int:cid>', contact_delete_view.contact_delete, name='contact-delete'),
    path('group-search/', contact_search_view.ContactSearch.as_view(), name='contact-search'),

    # Groups
    path('groups/', group_list_view.GroupList.as_view(), name='group-list'),
    path('group-modify/', group_edit_view.GroupEdit.as_view(), name='group-edit'),
    path('group-delete/<int:gid>', group_delete_view.group_delete, name='group-delete'),
]