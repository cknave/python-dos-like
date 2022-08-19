Differences from the C API
==========================

The screen buffer
-----------------

The screen buffer is a CFFI :class:`.buffer` object.  It can be accessed with item syntax:

.. code-block:: python

  # (C API)
  # char *screen = screenbuffer();
  screen = screenbuffer()

  # (C API)
  # screen[0] = 0x40;
  # screen[1] = 0x41;
  # screen[2] = 0x42;
  # screen[3] = 0x43;
  screen[0] = b'\x40';
  screen[1:4] = bytearray([0x41, 0x42, 0x43])

  # (C API)
  # print("%x\n", screen[2]);  // 42
  print(screen[2].hex())  # 42


Basic types
-----------

Functions with text arguments will accept CP437_ encoded :class:`bytes`, or strings as long
as they can be encoded in CP437:

.. code-block:: python

  # (C API)
  # cputs("\xb0\xb1\xb2)");
  cputs(b'\xb0\xb1\xb2')

  # (C API)
  # cputs("hello \x02");
  cputs('hello ☻')


.. _CP437: https://en.wikipedia.org/wiki/Code_page_437

:class:`bool` is used for true/false arguments and return values:

.. code-block:: python

  # (C API)
  # setdoublebuffer(1)
  setdoublebuffer(True)

  # (C API)
  # int x = shuttingdown()
  x: bool = shuttingdown()

  # (C API)
  # settextstyle(DEFAULT_FONT_8X8, 0, 1, 0)
  settextstyle(DEFAULT_FONT_8X8, bold=False, italic=True, underline=False)


Exceptions
----------

In cases where a function can return ``NULL`` on error, the Python version will raise an exception
(typically a :class:`ValueError`).

.. code-block:: python

  # (C API)
  # struct music_t *music = loadmid("does not exist.mid");
  # if(!music) {
  #   printf("Could not load music\n");
  # }
  try:
    music = loadmid('does not exist.mid')
  except ValueError:
    print('Could not load music')


Palette
-------

The palette functions accept and return a named 3-tuple, :class:`.RGB`, that has ``r``, ``g``,
and ``b`` properties for the red, green, and blue channels respectively:

.. code-block:: python

  # (C API)
  # int r, g, b;
  # getpal(0, &r, &g, &b);
  # print("%d, %d, %d\n", r, g, b);
  color = getpal(0)
  print(f'{color.r}, {color.g}, {color.b}')

  # (C API)
  # setpal(0, 1, 3, 5);
  setpal(0, 1, 3, 5)  # color index and red, green, and blue channels

  # (C API)
  # setpal(1, 2, 4, 6);
  setpal(1, (2, 4, 6))  # color index and 3-tuple of ints

  # (C API)
  # setpal(3, 3, 5, 7);
  setpal(2, RGB(3, 5, 7))  # color index and RGB namedtuple


GIF images
----------
GIF images are returned in a :class:`.GIF` data class.

.. code-block:: python

  # (C API)
  # int width, height, palcount;
  # char palette[768];
  # char *pixels = loadgif("test.gif", &width, &height, &palcount, palette);
  gif = loadgif('test.gif')

  # (C API)
  # printf("test.gif: %dx%d, %d colors\n", width, height, palcount);
  print(f'{gif.filename}: {gif.width}x{gif.height}, {len(gif.palette)} colors')

  # (C API)
  # char top_left = pixels[0];  // 1
  top_left_byte = gif.pixels[0]  # b'\x01'
  top_left_index = top_left_byte[0]  # 1

  # (C API)
  # char *color = &palette[top_left];
  # printf("top left red: %d, green: %d, blue %d\n",
  #        *color, *(color + 1), *(color + 2);
  color = gif.palette[top_left_index]
  print(f'top left red: {color.r}, green: {color.g}, blue: {color.b}')


Polygons
--------
Point lists for polygons may be a list of tuples ``[(𝑥1, 𝑦1), (𝑥2, 𝑦2)]``, a flattened list
of points ``[𝑥1, 𝑦1, 𝑥2, 𝑦2]```, or a buffer of a flattened list of points as ints.

.. code-block:: python

  # (C API)
  # int points[] = {5, 0, 10, 10, 0, 10, 5, 0};
  # drawpoly(points, 8);
  drawpoly([(5, 0), (10, 10), (0, 10), (5, 0)])
  # or flattened:
  drawpoly([5, 0, 10, 10, 0, 10, 5, 0])
  # or from a buffer:
  data = struct.pack('8i', 5, 0, 10, 10, 0, 10, 5, 0)
  drawpoly(data)


Font and sound bank handles
---------------------------
:func:`.installuserfont` and :func:`.installusersoundbank` return :class:`int` subclasses
:class:`.FontHandle` and :class:`.SoundBankHandle` respectively.  This is purely to help your
type checker (e.g. prevent you from passing a sound bank to a function expecting a font).


Keys and characters
-------------------
:func:`.readkeys` returns a :class:`list` of :class:`.KeyCode` enums.  The length of the list
should be used instead of searching for a zero value:

.. code-block:: python

  # (C api)
  # enum keycode_t *keys = readkeys();
  # int length = 0;
  # for(enum keycode_t key = *keys; *keys++; key) {
  #   if(key == KEY_A) printf("A was pressed\n");
  #   length++;
  # }
  # printf("There were %d keys in the buffer.\n", length);
  keys = readkeys()
  for key in keys:
      if key == KEY_A:
          print('A was pressed')
  print(f'There were {len(keys)} keys in the buffer.')


Similarly, :func:`.readchars` returns a :class:`str` of characters.  The length of the string
should be used instead of searching for a NUL character:

.. code-block:: python

  # (C api)
  # char *chars = readchars();
  # int length = 0;
  # for(char c = *chars; *chars++; c) {
  #   if(c == 'a') printf("A was pressed\n");
  #   length++;
  # }
  # printf("There were %d characters in the buffer.\n", length);
  chars = readchars()
  for char in chars:
      if char == 'a':
          print('A was pressed')
  print(f'There were {len(chars)} characters in the buffer.')
