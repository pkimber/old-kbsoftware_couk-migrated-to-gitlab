kbsoftware.co.uk
****************

Development
===========

Virtual Environment
-------------------

::

  pyvenv-3.4 --without-pip venv-kbsoftware_couk
  source venv-kbsoftware_couk/bin/activate
  wget https://raw.githubusercontent.com/pypa/pip/master/contrib/get-pip.py
  python get-pip.py

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
