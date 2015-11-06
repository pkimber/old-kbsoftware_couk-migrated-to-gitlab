# -*- encoding: utf-8 -*-
from django.views.generic import TemplateView

from braces.views import (
    LoginRequiredMixin,
    StaffuserRequiredMixin,
)

from base.view_utils import BaseMixin
from invoice.views import DashMixin


class DashView(
        LoginRequiredMixin, StaffuserRequiredMixin,
        DashMixin, BaseMixin, TemplateView):

    template_name = 'dash/home.html'
