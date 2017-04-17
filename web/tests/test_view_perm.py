# -*- encoding: utf-8 -*-
import pytest

from django.core.urlresolvers import reverse

from block.tests.factories import PageFactory, TemplateFactory
from login.tests.fixture import perm_check


@pytest.mark.django_db
def test_dash(perm_check):
    perm_check.staff(reverse('project.dash'))


@pytest.mark.django_db
def test_home(perm_check):
    PageFactory(
        slug='home',
        slug_menu='',
        is_home=True,
        template=TemplateFactory(template_name='web/page_article.html'),
    )
    perm_check.anon(reverse('project.home'))


@pytest.mark.django_db
def test_login(perm_check):
    perm_check.anon(reverse('login'))
