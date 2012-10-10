Python Module
=============

Installing
~~~~~~~~~~

The stable version is available in `PyPI
<http://pypi.python.org/pypi/hangulize>`_:

.. sourcecode:: console

   $ easy_install hangulize

We can also get a development version from `the GitHub repository
<http://github.com/sublee/hangulize>`_:

.. sourcecode:: console

   $ pip install git+git://github.com/sublee/hangulize.git#egg=hangulize

.. sourcecode:: console

   $ git clone git://github.com/sublee/hangulize.git
   $ cd hangulize
   $ python setup.py install

API
~~~

Front-end
---------

.. autofunction:: hangulize.hangulize

.. autofunction:: hangulize.supports

.. autofunction:: hangulize.get_lang

.. autofunction:: hangulize.langs.list_langs

Utility
-------

.. autofunction:: hangulize.normalization.normalize_roman

.. autofunction:: hangulize.processing.complete_syllable

.. autofunction:: hangulize.processing.complete_syllables

.. autofunction:: hangulize.processing.split_phonemes

.. autofunction:: hangulize.processing.join_phonemes
