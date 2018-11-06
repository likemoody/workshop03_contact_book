from django.shortcuts import render
from django.views.generic.base import View
from ..models import Person
from ..forms import SearchForm


class ContactSearch(View):
    template_name = 'contact_search.html'

    def get(self, request):
        form = SearchForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        contacts = Person.objects
        searched_data = None
        results = None

        if first_name and last_name:
            results = contacts.filter(first_name__icontains=first_name,
                                      last_name__icontains=last_name)
            searched_data = {'first_name': first_name, 'last_name': last_name}

        if first_name and not last_name:
            results = contacts.filter(first_name__icontains=first_name)
            searched_data = {'first_name': first_name}

        if last_name and not first_name:
            results = contacts.filter(last_name__icontains=last_name)
            searched_data = {'last_name': last_name}

        form = SearchForm(initial=searched_data)
        return render(request, self.template_name, {'form': form, 'results': results})
