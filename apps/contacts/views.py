from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, UpdateView, CreateView

from .forms import ContactsForm
from .models import Contacts


class ContactList(ListView):
    model = Contacts


class ContactCreate(CreateView):
    form_class = ContactsForm
    template_name = "contacts/contacts_form.html"
    success_url = reverse_lazy("contacts_app:show_contacts")


class ContactUpdate(UpdateView):
    model = Contacts
    form_class = ContactsForm
    success_url = reverse_lazy("contacts_app:show_contacts")


class ContactDelete(DeleteView):
    model = Contacts
    success_url = reverse_lazy("contacts_app:show_contacts")
