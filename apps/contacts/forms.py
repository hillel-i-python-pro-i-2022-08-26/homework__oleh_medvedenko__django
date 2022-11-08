from datetime import datetime

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.urls import reverse_lazy

from apps.contacts.models import Contacts


class ContactsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy("contacts_app:show_contacts")
        self.helper.form_method = "POST"
        self.helper.add_input(Submit("submit", "Submit"))

    class Meta:
        model = Contacts
        fields = (
            "name",
            "phone_number",
            "birthday",
        )

        widgets = {
            "name": forms.TextInput(attrs={"style": "width:220px"}),
            "phone_number": forms.TextInput(attrs={"style": "width:220px"}),
            "birthday": forms.DateInput(attrs={"type": "date", "max": datetime.now().date(), "style": "width:220px"}),
        }
