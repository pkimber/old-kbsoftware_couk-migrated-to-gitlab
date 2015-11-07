# -*- encoding: utf-8 -*-
from django.views.generic import TemplateView

from braces.views import (
    LoginRequiredMixin,
    StaffuserRequiredMixin,
)

from base.view_utils import BaseMixin
from report.views import ReportMixin


class DashView(
        LoginRequiredMixin, StaffuserRequiredMixin,
        ReportMixin, BaseMixin, TemplateView):

    template_name = 'dash/dash.html'
