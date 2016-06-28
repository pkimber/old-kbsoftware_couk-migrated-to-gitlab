kbsoftware.co.uk
****************

WIP
===

For notes on removing the ``Contact`` model from ``crm`` and using the
``contact`` app instead, see https://www.kbsoftware.co.uk/crm/ticket/717/

.. tip:: For historial information on moving the CRM data from ``pkimber_net``
         to ``kbsoftware_couk``, see ``project/migrations/0001_initial.py``.

Development
===========

Virtual Environment
-------------------

::

  virtualenv --python=python3 venv-kbsoftware_couk
  source venv-kbsoftware_couk/bin/activate
  pip install --upgrade pip

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

https://pkimber.net/open/
