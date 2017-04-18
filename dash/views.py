# -*- encoding: utf-8 -*-
import csv

from braces.views import LoginRequiredMixin, StaffuserRequiredMixin
from datetime import date
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import DetailView, ListView, TemplateView

from base.view_utils import BaseMixin
from crm.models import Note, Ticket
from crm.service import get_contact_model
from crm.views import CrmContactDetailMixin
from invoice.models import TimeRecord
from invoice.report import time_summary_by_user_for_chartist
from report.models import ReportSpecification


class ContactDetailView(
        LoginRequiredMixin, StaffuserRequiredMixin,
        CrmContactDetailMixin, BaseMixin, DetailView):

    template_name = 'contact/contact_detail.html'


class DashView(
        LoginRequiredMixin, StaffuserRequiredMixin,
        BaseMixin, TemplateView):
    """Dashboard includes the report mixin."""

    template_name = 'dash/dash.html'

    def _summary(self):
        result = {}
        try:
            report = ReportSpecification.objects.get(
                slug='time_summary_by_user'
            )
            latest = report.latest()
            if latest:
                reader = csv.reader(open(latest.full_path), 'excel')
                csv_data = []
                for row in reader:
                    csv_data.append(row)
                result = time_summary_by_user_for_chartist(csv_data)
        except ReportSpecification.DoesNotExist:
            pass
        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(dict(
            notes=Note.objects.order_by('-pk')[:10],
            tickets=Ticket.objects.order_by('-pk')[:10],
            time_records=TimeRecord.objects.order_by('-pk')[:10],
            summary=self._summary(),
        ))
        return context


class SettingsView(
        LoginRequiredMixin, StaffuserRequiredMixin,
        BaseMixin, TemplateView):

    template_name = 'dash/settings.html'
