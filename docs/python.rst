Python Module
=============

Installing
~~~~~~~~~~

The stable version is available in PyPI:

.. sourcecode:: console

   $ pip install hangulize

.. sourcecode:: console

   $ easy_install hangulize

We can also get a development version from `the GitHub repository
<http://github.com/sublee/hangulize>`_.

.. sourcecode:: console

   $ pip install git+git://github.com/sublee/hangulize.git#egg=hangulize

.. sourcecode:: console

   $ git clone git://github.com/sublee/hangulize.git
   $ cd hangulize
   $ python setup.py install

API
~~~

.. autofunction:: hangulize.hangulize

.. autofunction:: hangulize.supported

.. autofunction:: hangulize.get_lang

.. autofunction:: hangulize.langs.get_list
