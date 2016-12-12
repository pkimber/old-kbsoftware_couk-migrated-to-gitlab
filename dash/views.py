# -*- encoding: utf-8 -*-
from braces.views import LoginRequiredMixin, StaffuserRequiredMixin
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import DetailView, ListView, TemplateView

from base.view_utils import BaseMixin
from crm.models import Note, Ticket
from crm.service import get_contact_model
from crm.views import CrmContactDetailMixin
from invoice.models import TimeRecord
from report.views import ReportMixin


class ContactDetailView(
        LoginRequiredMixin, StaffuserRequiredMixin,
        CrmContactDetailMixin, BaseMixin, DetailView):

    template_name = 'crm/contact_detail.html'


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
