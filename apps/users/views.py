from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from webargs import fields
from webargs.djangoparser import use_args

from apps.users.services.data_generator import organize_info


@use_args({"amount": fields.Int(missing=10)}, location="query")
def users_info(request: HttpRequest, args) -> HttpResponse:
    amount = args["amount"]
    return render(
        request,
        "users.html",
        {
            "userinfo": organize_info(amount=amount),
        },
    )
