Python bindings for dos-like
============================
python-dos-like is a set of Python bindings for the dos-like_ programming library by Mattias
Gustavsson.

.. image:: https://github.com/cknave/python-dos-like/actions/workflows/testing.yml/badge.svg
  :target: https://github.com/cknave/python-dos-like/actions/workflows/testing.yml
  :alt: Tests status 

.. image:: https://readthedocs.org/projects/python-dos-like/badge/?version=latest
  :target: https://python-dos-like.readthedocs.io/en/latest/?badge=latest
  :alt: Documentation Status

.. _dos-like: https://mattiasgustavsson.itch.io/dos-like

----

**Documentation:** https://python-dos-like.readthedocs.io/en/latest/

**Source Code:** https://github.com/cknave/python-dos-like


Usage
-----

.. code-block:: bash

  pip install python-dos-like

python-dos-like can be used in the same way as dos-like by calling ``dos_like.start`` on your
main function:

.. code-block:: python

  from random import randrange

  import dos_like
  from dos_like.dos import *


  def main():
      setvideomode(videomode_320x200)

      while not shuttingdown():
          waitvbl()
          for _ in range(50):
              setcolor(randrange(256))
              line(randrange(320), randrange(200), randrange(320), randrange(200))
              setcolor(randrange(256))
              fillcircle(randrange(320), randrange(200), randrange(30))
              setcolor(randrange(256))
              circle(randrange(320), randrange(200), randrange(30))

  dos_like.start(main)

You can also use python-dos-like in the Python REPL by calling ``dos_like.run_in_background``:

.. code-block:: python

  >>> import dos_like
  >>> from dos_like.dos import *
  >>> dos_like.run_in_background(['-w'])
  >>> cputs('hello world!')

.. note::

  Why the ``['-w']``?  This passes the ``-w`` flag through to dos-like, which tells it to
  run in windowed mode.  Without it, dos-like starts in full screen and you have to press
  F11 to enter windowed mode.


Building
--------

Building python-dos-like requires C development tools to be installed.

On Linux and macOS, the SDL2_ and GLEW_ libraries are required.

If building from a git repository, you must update submodules to get the dos-like source.

.. code-block:: bash

  git submodule update --init --recursive

.. code-block:: bash

  $ python -mvenv .venv
  $ . .venv/bin/activate
  (.venv) $ pip install -e '.[dev]'
  (.venv) $ coverage run -m unittest && coverage report

Several environment variables may be set to control compile-time options:

+----------------------+---------+---------------------------------------------------------------+
| Environment variable | Default | Description                                                   |
+======================+=========+===============================================================+
| ``ALWAYS_UPDATE``    | 1       | Update the screen in the background.  Set this to ``0`` to    |
|                      |         | restore dos-like's default behavior of pausing updates when   |
|                      |         | the window loses focus.                                       |
+----------------------+---------+---------------------------------------------------------------+
| ``CFLAGS``           |         | Extra compiler flags.  Of note, ``-DNULL_PLATFORM`` is useful |
|                      |         | to build a library for headless build servers.                |
+----------------------+---------+---------------------------------------------------------------+


.. _SDL2: https://www.libsdl.org/download-2.0.php
.. _GLEW: http://glew.sourceforge.net/


Limitations
-----------

Memory management
~~~~~~~~~~~~~~~~~

Memory allocated by dos-like will be freed when its corresponding bython buffer object is
garbage collected.  The current draw target and music will be retained even if no other python
code has a reference, but any playing sounds will not be.  Deleting or releasing the last
reference to a playing sound may cause issues.

Platforms
~~~~~~~~~

This library has been tested on Linux, Windows, and macOS.

macOS does not support GUI operations in a background thread, so it cannot be used from the
Python REPL by calling ``run_in_background()``.

python-dos-like can be compiled as a WebAssembly Pyodide_ module, but will fail to import due to
a missing symbol from WAjic_.  Even if this symbol (``J``, an object containing JS functions to
be called from C) is added to the imports when loaded by Pyodide, it does not appear to be
compatible.

It is not clear to me what the best way forward is for WebAssembly support: getting a Pyodide
module to import WAjic functions, building a Pyodide module in WAjic, or removing Pyodide or
WAjic from the project entirely.

.. _Pyodide: https://pyodide.org/en/stable/index.html
.. _WAjic: https://wajic.github.io/
