from django.views.generic import ListView

from .aggregator import aggregator
from .models import VisitHandler


class AllInfoViews(ListView):
    model = VisitHandler
    template_name = "middlewares/sessions_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "All session info"

        session_handler = VisitHandler.objects.all()

        context["object_list"] = session_handler
        context.update(aggregator(session_handler))
        return context


class SessionInfoViews(ListView):
    model = VisitHandler
    template_name = "middlewares/sessions_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Session info"

        session_handler = VisitHandler.objects.filter(session_key=self.kwargs["session_key"])

        context["object_list"] = session_handler
        context.update(aggregator(session_handler))
        return context


class UserInfoViews(ListView):
    model = VisitHandler
    template_name = "middlewares/sessions_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "User actions info"

        session_handler = VisitHandler.objects.filter(user=self.kwargs["pk"])

        context["object_list"] = session_handler
        context.update(aggregator(session_handler))
        return context


# import datetime
#
# from django.http import HttpRequest, HttpResponse
# from django.shortcuts import render
#
# KEY__COUNT_OF_VISITS = "count_of_visits"
#
#
# def session_example_view(request: HttpRequest) -> HttpResponse:
#     session = request.session
#     count_of_visits = session.get(KEY__COUNT_OF_VISITS, 0)
#     time_of_visit = session.get("time_of_visit", datetime.datetime.now())
#
#     count_of_visits += 1
#
#     session[KEY__COUNT_OF_VISITS] = count_of_visits
#
#     return render(
#         request,
#         "sessions.html",
#         {
#             "session_id": session.session_key,
#             "count_of_visits": count_of_visits,
#             "time_of_visit": time_of_visit,
#             "title": "Sessions",
#         },
#     )
