from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DeleteView, UpdateView, CreateView
from rest_framework import generics, permissions, viewsets

from .forms import ContactsForm
from .models import Contacts
from .serializers import ContactsSerializer, ContactsHyperlinkSerializer


class ContactList(ListView):
    model = Contacts


@method_decorator(login_required, name="get")
class ContactCreate(CreateView):
    form_class = ContactsForm
    template_name = "contacts/contacts_form.html"
    success_url = reverse_lazy("contacts_app:show_contacts")


@method_decorator(login_required, name="get")
class ContactUpdate(UpdateView):
    model = Contacts
    form_class = ContactsForm
    success_url = reverse_lazy("contacts_app:show_contacts")


@method_decorator(login_required, name="post")
class ContactDelete(DeleteView):
    model = Contacts
    success_url = reverse_lazy("contacts_app:show_contacts")


# Generics
class ContactAPIList(generics.ListCreateAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
    permission_classes = [permissions.IsAuthenticated]


class ContactAPIEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
    permission_classes = [permissions.IsAuthenticated]


# ViewSet
class ContactsViewSet(viewsets.ModelViewSet):
    queryset = Contacts.objects.all()
    serializer_class = ContactsHyperlinkSerializer
    permission_classes = [permissions.IsAuthenticated]
