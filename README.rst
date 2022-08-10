Python bindings for dos-like
============================
python-dos-like is a set of Python bindings for the dos-like_ programming library by Mattias
Gustavsson.

.. _dos-like: https://mattiasgustavsson.itch.io/dos-like


Usage
-----
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

.. warning::

  The current version of dos-like does not update the screen while its window is out of focus.
  Since this is inconvenient for experimentation, you can build your own version of dos-like
  where you modify the `app_has_focus function`_ to always return true.

.. _app_has_focus function: https://github.com/mattiasgustavsson/dos-like/blob/e0e279f2d8b117e128fe9c20b19edb3fbc6f8375/source/dos.h#L3652-L3654


Building
--------

Building python-dos-like requires C development tools, SDL2_, and GLEW_ to be installed.

If building from a git repository, you must update submodules to get the dos-like source.

.. code-block:: bash

  $ git submodule update --init --recursive

.. code-block:: bash

  $ python -mvenv .venv
  $ . .venv/bin/activate
  (.venv) $ pip install -e '.[dev]'
  (.venv) $ coverage run -m unittest && coverage report

.. _SDL2: https://www.libsdl.org/download-2.0.php
.. _GLEW: http://glew.sourceforge.net/


Limitations
-----------

Only building on Linux has been tested.  Building on macOS should work fine.  Windows will
likely be more difficult.  And WebAssembly should be a real challenge.

The lifecycle of graphics, music, and sound loaded from dos-like is not managed, and is
likely leaking memory.
