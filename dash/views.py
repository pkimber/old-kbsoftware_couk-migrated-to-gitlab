# -*- encoding: utf-8 -*-
from django.views.generic import TemplateView

from braces.views import (
    LoginRequiredMixin,
    StaffuserRequiredMixin,
)

from base.view_utils import BaseMixin
from crm.models import (
    Note,
    Ticket,
)
from invoice.models import TimeRecord
from report.views import ReportMixin


class DashView(
        LoginRequiredMixin, StaffuserRequiredMixin,
        ReportMixin, BaseMixin, TemplateView):
    """Dashboard includes the report mixin."""

    template_name = 'dash/dash.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(dict(
            notes=Note.objects.order_by('-pk')[:10],
            tickets=Ticket.objects.order_by('-pk')[:10],
            time_records=TimeRecord.objects.order_by('-pk')[:10],
        ))
        return context


class SettingsView(
        LoginRequiredMixin, StaffuserRequiredMixin,
        ReportMixin, BaseMixin, TemplateView):

    template_name = 'dash/settings.html'
