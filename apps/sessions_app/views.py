import datetime

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

KEY__COUNT_OF_VISITS = "count_of_visits"


def session_example_view(request: HttpRequest) -> HttpResponse:
    session = request.session
    count_of_visits = session.get(KEY__COUNT_OF_VISITS, 0)
    time_of_visit = session.get("time_of_visit", datetime.datetime.now())

    count_of_visits += 1

    session[KEY__COUNT_OF_VISITS] = count_of_visits

    return render(
        request,
        "sessions.html",
        {
            "session_id": session.session_key,
            "count_of_visits": count_of_visits,
            "time_of_visit": time_of_visit,
            "title": "Sessions",
        },
    )
