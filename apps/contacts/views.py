from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .forms import ContactsForm
from .models import Contacts


def get_contacts(request: HttpRequest) -> HttpResponse:
    contacts = Contacts.objects.all()

    return render(
        request,
        "contacts.html",
        {
            "contacts": contacts,
            "title": "Contacts",
        },
    )


def edit_contact(request: HttpRequest, pk: int) -> HttpResponse:
    contact = Contacts.objects.get(pk=pk)
    form = ContactsForm(instance=contact)

    return render(
        request,
        "contacts.html",
        {
            "form": form,
            "title": "Contacts",
        },
    )
