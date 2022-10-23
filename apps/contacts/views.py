from django.contrib import messages
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from .forms import ContactsForm
from .models import Contacts


def get_contacts(request: HttpRequest) -> HttpResponse:
    contacts = Contacts.objects.order_by("-creation_date")
    return render(
        request,
        "contacts_dir/show_contacts.html",
        {
            "contacts": contacts,
            "title": "Contacts",
        },
    )


def create_contact(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ContactsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("contacts_app:show_contacts")
    else:
        form = ContactsForm()
    return render(request, "contacts_dir/edit_contact.html", {"title": "Create a contact", "form": form})


def update_contact(request: HttpRequest, pk) -> HttpResponse | HttpResponseRedirect:
    contact = Contacts.objects.get(pk=pk)

    if request.method == "POST":
        form = ContactsForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect("contacts_app:show_contacts")
        else:
            form = ContactsForm(instance=contact)
        return render(
            request,
            "contacts_dir/edit_contact.html",
            {
                "form": form,
                "title": "Edit contacts",
            },
        )


def delete_contact(request: HttpRequest, pk):
    contacts = Contacts.objects.get(pk=pk)
    contacts.delete()
    messages.success(request, f"User {contacts.name} deleted.")
    return redirect("contacts_app:show_contacts")
