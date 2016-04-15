# -*- encoding: utf-8 -*-
"""
This command is designed to be run multiple times.  It will clear out data, and
then re-insert e.g. for setting up the main menu navigation.
"""
from decimal import Decimal
from django.core.management.base import BaseCommand
from stock.models import Product, ProductCategory, ProductType


class Command(BaseCommand):

    help = "Set-up project (e.g. main navigation)"

    def handle(self, *args, **options):
        product_type = ProductType.objects.init_product_type('crm', 'CRM')
        product_category = ProductCategory.objects.init_product_category('time', 'Time', product_type)
        Product.objects.init_product('time', 'Time', 'Time Recording', Decimal('30'), product_category)
        print("Project initialised...")
