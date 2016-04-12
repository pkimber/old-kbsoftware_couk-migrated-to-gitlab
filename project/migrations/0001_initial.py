# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def remove_references_to_old_tables(apps, schema_editor):
    model = apps.get_model('contenttypes', 'ContentType')
    model.objects.filter(app_label='block').delete()
    model.objects.filter(app_label='booking').delete()
    model.objects.filter(app_label='cms').delete()
    model.objects.filter(app_label='compose').delete()
    model.objects.filter(app_label='enquiry').delete()
    model.objects.filter(app_label='original').delete()
    model.objects.filter(app_label='project').delete()
    model.objects.filter(app_label='web').delete()


class Migration(migrations.Migration):
    """Migrate ``crm`` from ``pkimber_net`` to ``kbsoftware_couk``.

    ``kbsoftware_couk`` does not use ``block`` or ``cms`` so try and remove all
    traces of it.  This will *hopefully* allow a smooth migration to ``block``
    and ``compose`` in future.

    .. warning:: Do **NOT** change the order of the ``drop table`` statements.

    """

    dependencies = [
    ]

    operations = [
        # migrations.RunSQL('drop table booking_booking'),
        # migrations.RunSQL('drop table booking_bookingsettings'),
        # migrations.RunSQL('drop table booking_category'),
        # migrations.RunSQL('drop table booking_location'),
        # migrations.RunSQL('drop table booking_permission'),
        # migrations.RunSQL('drop table enquiry_enquiry'),
        # migrations.RunSQL('drop table project_stripecontent'),
        # migrations.RunSQL('drop table cms_container'),
        # migrations.RunSQL('drop table cms_section'),
        # migrations.RunSQL('drop table block_viewurl'),
        # migrations.RunSQL('drop table cms_headerfooter'),
        # migrations.RunSQL('drop table cms_layout'),
        # migrations.RunSQL('drop table cms_moderatestate'),
        # migrations.RunSQL('drop table cms_page'),
        # migrations.RunSQL('drop table cms_templatesection'),
        # migrations.RunSQL('drop table cms_template'),
        # migrations.RunSQL('drop table compose_article'),
        # migrations.RunSQL('drop table compose_articleblock'),
        # migrations.RunSQL('drop table original_cms_simple'),
        # migrations.RunSQL('drop table original_cms_section'),
        # migrations.RunSQL('drop table web_main'),
        # migrations.RunSQL('drop table web_mainblock'),
        # migrations.RunSQL('drop table block_pagesection'),
        # migrations.RunSQL('drop table block_section'),
        # migrations.RunSQL('drop table block_page'),
        # migrations.RunSQL('drop table block_paginatedsection'),
        # migrations.RunSQL('drop table block_editstate'),
        # migrations.RunSQL('drop table block_moderatestate'),
        # reversion
        # migrations.RunSQL("""
        #     delete from reversion_version
        #         where content_type_id in (
        #             select id from django_content_type where app_label in (
        #                 'block', 'cms', 'compose', 'project', 'web'
        #             )
        #         )
        # """),
        # migrations.RunPython(remove_references_to_old_tables),
    ]
