from datetime import datetime

from django import forms

from apps.contacts.models import Contacts


class ContactsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Contacts
        fields = (
            "name",
            "phone_number",
            "birthday",
            "image",
        )

        widgets = {
            "birthday": forms.DateInput(attrs={"type": "date", "max": datetime.now().date()}),
        }
