========
IndexNow
========

:Info: An IndexNow URL submitter for Python.
:Author: Ajit Jasrotia (http://github.com/ajitjasrotia, http://twitter.com/ajitjasroti)

IndexNow is an easy way for websites owners to instantly inform search engines about latest content changes on their website.

Installation
============

You can get IndexNow by using pip::

    $ pip install indexnow

You can get IndexNow by using poetry::

    $ poetry shell
    $ poetry add indexnow

If you want to install it from source, grab the git repository from GitHub and run setup.py::

    $ git clone git@github.com:ajitjasrotia/indexnow.git
    $ cd indexnow
    $ python setup.py install


Documentation
=============

The key features are:

* Support for Django
* Support for FastAPI

More information on Getting-Started


Guide
=====

.. code-block:: python

    from indexnow import IndexNow

    index_now = IndexNow(key="57e85df435cd43bb", host="example.com")

    status = index_now.index(["https://www.example.com"])

    print(f"IndexNow Response: {status}")

    IndexNow Response: 200

Getting Involved
================

Open Source projects can always use more help. Fixing a problem, documenting a feature, adding
translation in your language. If you have some time to spare and like to help us, here are the places to do so:

- GitHub: https://github.com/ajitjasrotia/indexnow
- Mailing list: https://groups.google.com/group/indexnow


Support
=======

IndexNow is free and always will be. It is developed and maintained by developers in an Open Source manner.
Any support is welcome. You could help by writing documentation, pull-requests, report issues and/or translations.

Please remember that nobody is paid directly to develop or maintain IndexNow so we do have to divide our time
between putting food on the table, family, this project and the rest of life :-)
