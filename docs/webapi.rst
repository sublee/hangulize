Web API
~~~~~~~

Hangulize provides a web API for non-python projects. So any project which
could parse a JSON or plist string can use the features of Hangulize.

.. note::

   If your project is written in Python, don't use the web API. `The native
   Hangulize module <http://pypi.python.org/pypi/hangulize>`_ is faster than
   it.

Accept Headers
==============

To use the web API, we should send a HTTP request to `www.hangulize.org
<http://www.hangulize.org>`_. all methods of the web API send different results
in different ``Accept`` or ``Accept-Language`` HTTP headers. So we should send
a them to the web API.

- ``Accept`` decides a type of the result.
- ``Accept-Language`` decides a language label string.

For example, if we want to get the supported language list of Hangulize with
Korean (``ko``) labels, then we should request such as:

.. sourcecode:: console

   $ curl 'http://www.hangulize.org/langs' \
   > -H'Accept: application/json' \
   > -H'Accept-Language: ko'

.. sourcecode:: text

   GET /langs HTTP/1.1
   Host: www.hangulize.org
   Accept: application/json
   Accept-Languages: ko

In this case, the response is:

.. sourcecode:: js

   {
     "length": 38,
     "langs": [
       {
         "code": "aze",
         "name": "Azerbaijani",
         "label": "\uc544\uc81c\ub974\ubc14\uc774\uc794\uc5b4",
         "iso639-1": "az",
         "iso639-2": "aze",
         "iso639-3": "aze"
       },
       ...
       {
         "code": "wlm",
         "iso639-3": "wlm",
         "name": "MiddleWelsh",
         "label": "\uc6e8\uc77c\uc2a4\uc5b4(\uc911\uc138)"
       }
     ],
     "success": true
   }

Look the structure and a ``"label"`` property of an item in ``"langs"``. We
got the result as JSON structure, and there are Korean language labels.

JSONP
=====

To get a `JSONP <http://en.wikipedia.org/wiki/JSON#JSONP>`_ result, just add
a ``jsonp`` parameter into the querystring. Whatever the ``Accept`` header, the
web API will send JSONP data. For example:

.. sourcecode:: html

   <script>
     // define a function for JSONP callback
     function callbackFunction( data ) {
       if ( data.success ) {
         alert( "Hangulize supports " + data.length + " languages." );
       } else {
         throw new Error( data.reason );
       }
     }
   </script>
   <!-- call a method -->
   <script src="http://www.hangulize.org/langs?jsonp=callbackFunction">
   </script>

Methods
=======

.. method:: hangulize(word, lang)

   Transcribes a loanword to Hangul.

   :url: http://www.hangulize.org/
   :method: ``GET``
   :param word: a word to be transcribed
   :param lang: a language code which almost seems to ISO 639-3 code
   :result types: - HTML (:mimetype:`text/html`)
                  - JSON (:mimetype:`application/json`)
                  - Property List (:mimetype:`application/x-plist`,
                    :mimetype:`application/plist+xml`)

   Data structure:

   +-----------+------------------------------------------------------------+
   |``result`` | A transcription result                                     |
   +-----------+------------------------------------------------------------+
   |``word``   | The given word                                             |
   +-----------+------------------------------------------------------------+
   |``lang``   | +------------+-------------------------------------------+ |
   |           | |``code``    | a language code                           | |
   |           | +------------+-------------------------------------------+ |
   |           | |``name``    | a class name in the hangulize module      | |
   |           | +------------+-------------------------------------------+ |
   |           | |``label``   | a humane language name based on requested | |
   |           | |            | language (``Accept-Language`` header)     | |
   |           | +------------+-------------------------------------------+ |
   |           | |``iso639-1``| ISO 639-1 code (it can be not given)      | |
   |           | +------------+-------------------------------------------+ |
   |           | |``iso639-2``| ISO 639-2 code (it can be not given)      | |
   |           | +------------+-------------------------------------------+ |
   |           | |``iso639-3``| ISO 639-3 code (it can be not given)      | |
   |           | +------------+-------------------------------------------+ |
   +-----------+------------------------------------------------------------+
   |``success``| ``true`` or ``false``, when it ``false`` the result        |
   |           | contains a ``reason`` property.                            |
   +-----------+------------------------------------------------------------+
   |``reason`` | An error message when ``success`` is ``false``             |
   +-----------+------------------------------------------------------------+

.. method:: example([lang])

   Sends a random example. If the ``lang`` parameter isn't specified then it
   selects a random language also.

   :url: http://www.hangulize.org/example
   :method: ``GET``
   :param lang: (optional) a specified language code
   :result types: - JSON (:mimetype:`application/json`)
                  - Property List (:mimetype:`application/x-plist`,
                    :mimetype:`application/plist+xml`)

   Data structure:

   +-----------+------------------------------------------------------------+
   |``result`` | A transcription result                                     |
   +-----------+------------------------------------------------------------+
   |``word``   | A selected random word                                     |
   +-----------+------------------------------------------------------------+
   |``lang``   | The given language or selected random language. It's       |
   |           | structure is same as ``lang`` in :meth:`hangulize`.        |
   +-----------+------------------------------------------------------------+
   |``success``| ``true`` or ``false``, when it ``false`` the result        |
   |           | contains a ``reason`` property.                            |
   +-----------+------------------------------------------------------------+
   |``reason`` | An error message when ``success`` is ``false``             |
   +-----------+------------------------------------------------------------+

.. method:: langs

   Sends the language list that Hangulize is supporting.

   :url: http://www.hangulize.org/langs
   :method: ``GET``
   :result types: - JSON (:mimetype:`application/json`)
                  - Property List (:mimetype:`application/x-plist`,
                    :mimetype:`application/plist+xml`)

   Data structure:

   +-----------+------------------------------------------------------------+
   |``length`` | A length of the language list                              |
   +-----------+------------------------------------------------------------+
   |``langs``  | An array of the languages. The language data structure is  |
   |           | same as ``lang`` in :meth:`hangulize`.                     |
   +-----------+------------------------------------------------------------+
   |``success``| ``true`` or ``false``, when it ``false`` the result        |
   |           | contains a ``reason`` property.                            |
   +-----------+------------------------------------------------------------+
   |``reason`` | An error message when ``success`` is ``false``             |
   +-----------+------------------------------------------------------------+
