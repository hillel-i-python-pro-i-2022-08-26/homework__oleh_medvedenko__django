from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView

from .forms import ContactsForm
from .models import Contacts


# def get_contacts(request: HttpRequest) -> HttpResponse:
#     contacts = Contacts.objects.order_by("-creation_date")
#     return render(
#         request,
#         "contacts/contacts_list.html",
#         {
#             "contacts": contacts,
#             "title": "Contacts",
#         },
#     )


class ArticleListView(ListView):
    model = Contacts

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Contacts"
        return context


def create_contact(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ContactsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("contacts_app:show_contacts")
    else:
        form = ContactsForm()
    return render(request, "contacts/edit_contact.html", {"title": "Create a contact", "form": form})


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
            "contacts/edit_contact.html",
            {
                "form": form,
                "title": "Edit contacts",
            },
        )


class ContactDeleteView(DeleteView):
    model = Contacts
    success_url = reverse_lazy("contacts_app:show_contacts")
