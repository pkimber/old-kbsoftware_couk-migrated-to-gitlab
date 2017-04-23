kbsoftware.co.uk
****************

WIP
===

To remove all traces of ``block`` tables (before re-instating them)::

  django-admin.py migrate block zero
  django-admin.py migrate block zero --fake

.. note:: If you get an error with the first command, then try the second!

For notes on removing the ``Contact`` model from ``crm`` and using the
``contact`` app instead, see https://www.kbsoftware.co.uk/crm/ticket/717/

.. tip:: For historial information on moving the CRM data from ``pkimber_net``
         to ``kbsoftware_couk``, see ``project/migrations/0001_initial.py``.

Chargeable Time Report
----------------------

https://www.kbsoftware.co.uk/crm/ticket/2161/::

  from invoice.tasks import time_summary_by_user
  time_summary_by_user()

Browse to: http://localhost:8000/dash/

Development
===========

Virtual Environment
-------------------

::

  virtualenv --python=python3 venv-kbsoftware_couk
  source venv-kbsoftware_couk/bin/activate

  pip install -r requirements/local.txt

Testing
-------

::

  find . -name '*.pyc' -delete
  py.test -x

Usage
-----

::

  ./init_dev.sh

Browse to http://localhost:8000/::

  user          staff
  password      letmein

Release and Deploy
==================

https://www.kbsoftware.co.uk/docs/
