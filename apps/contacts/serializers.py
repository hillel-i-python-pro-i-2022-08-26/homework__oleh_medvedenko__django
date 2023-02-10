from rest_framework import serializers

from .models import Contacts


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = [
            "id",
            "name",
            "phone_number",
            "birthday",
            "image",
            "is_auto_generated",
            "creation_date",
            "edition_date",
        ]

        read_only_fields = [
            "id",
            "is_auto_generated",
            "creation_date",
            "edition_date",
        ]


class ContactsHyperlinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contacts
        fields = [
            # "url", Could not resolve URL for hyperlinked relationship using view name "contacts-detail".
            "id",
            "name",
            "phone_number",
            "birthday",
            "image",
            "is_auto_generated",
            "creation_date",
            "edition_date",
        ]

        read_only_fields = [
            "id",
            "is_auto_generated",
            "creation_date",
            "edition_date",
        ]
