from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello!")


#     return render(
#         request,
#         "index.html",
#     )
