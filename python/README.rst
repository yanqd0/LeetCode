leetcode - My Python solutions in leetcode.com
==============================================

Prerequisites
-------------

+---------------------+----------+
| Prerequisite        | Version  |
+---------------------+----------+
| Python              | 3.6      |
+---------------------+----------+
| PyCharm (Community) | 2017.3.3 |
+---------------------+----------+

If without PyCharm, either `pip`_ or `setuptools`_ is necessary.
Besides, a `virtualenv`_ may be useful.

.. _pip: https://pypi.python.org/pypi/pip
.. _setuptools: https://pypi.python.org/pypi/setuptools
.. _virtualenv: https://pypi.python.org/pypi/virtualenv

Setup
-----

If a PyCharm is used, then import this directory as a project.
You need just click, click and click in the UI.

If an code editor are used, you may need to setup the development environment in a terminal.

virtualenv
++++++++++

.. code:: sh

   virtualenv -p python3 venv
   source venv/bin/activate

Use pip
+++++++

.. code:: sh

   pip install -r requirements.txt
   pip install -e .

If something is wrong when developing, try ``pip install -e .`` again.

Use setuptools
++++++++++++++

If you prefer run ``setup.py`` directly, run the command below.

.. code:: sh

   ./setup.py develop

Develop
-------

Add new solutions as modules in ``src/leetcode/``, and their tests in ``tests``.

Don't forget to change package information in ``src/leetcode/_meta.py``.

Test
----

Run tests:

.. code:: sh

   pytest
   # or
   ./setup.py test

Generate coverage reports:

.. code:: sh

   coverage html

Then open ``htmlcov/index.html`` in a browser.

----

Enjoy it! :)
