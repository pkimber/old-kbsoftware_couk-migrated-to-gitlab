kbsoftware.co.uk
****************

WIP
===

Add cms branch
--------------

Please note: The site previously used the block app, this was partially removed.
To correct we need to fake remove the migrations see below

Pull the latest source from the repository, then refresh the VE ::

  rm -r venv-*     # Make sure there is not space between the - and the *
  create-venv kbs
  cd .

Restore a copy of the existing site and migrate::

  django-admin migrate block zero --fake

  django-admin migrate

Load the block and compose data::

  django-admin loaddata project/tests/data/block_compose.json

Extract the demo media files::

  tar -xvzf project/tests/data/media-files.tar.gz

Run the project 

  django-admin runserver 0.0.0.0:8000

You can view the site on mobile by finding your ip address::

  ip addr

Then on the mobile device enter::

  <ip address>:8000


Contact App
-----------
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
