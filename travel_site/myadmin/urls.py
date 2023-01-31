from django.urls import path, re_path

from . import views
from myadmin.views import get_user

urlpatterns = [
    re_path(r'^user/(?P<id>[0-9]{2})/$', get_user),
    path('tables/',views.GetTables.as_view()),
    path('add_tickets/',views.AddTickets.as_view()),
]