from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def main_route_page(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "main_route_page.html",
    )


def about(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "about_page.html",
    )
