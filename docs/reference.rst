Reference
=========

Running dos-like
----------------
.. automodule:: dos_like
  :members: start, run_in_background, stop


dos-like API
------------
.. automodule:: dos_like.dos

Screen functions
~~~~~~~~~~~~~~~~
.. autofunction:: getpal
.. autofunction:: screenbuffer
.. autofunction:: screenheight
.. autofunction:: screenwidth
.. autofunction:: setdoublebuffer
.. autofunction:: setpal
.. autofunction:: setvideomode
.. autofunction:: shuttingdown
.. autofunction:: swapbuffers
.. autofunction:: waitvbl

Text mode functions
~~~~~~~~~~~~~~~~~~~
.. autofunction:: clrscr
.. autofunction:: cputs
.. autofunction:: cursoff
.. autofunction:: curson
.. autofunction:: gotoxy
.. autofunction:: textbackground
.. autofunction:: textcolor
.. autofunction:: wherex
.. autofunction:: wherey


Graphics mode functions
~~~~~~~~~~~~~~~~~~~~~~~
.. autofunction:: blit
.. autofunction:: maskblit
.. autofunction:: loadgif
TODO: clearscreen

Utilities
---------
.. autofunction:: dos_like.dos.new_buffer


Types
-----
.. autoclass:: dos_like.dos.buffer
.. autoclass:: dos_like.dos.GIF
  :members: filename, width, height, palette, pixels
.. autoclass:: dos_like.dos.Music
  :members: filename
.. autoclass:: dos_like.dos.RGB
  :members: r, g, b
.. autoclass:: dos_like.dos.Sound
  :members: filename



Video Modes
-----------
.. autoclass:: dos_like.dos.VideoMode
.. autodata:: dos_like.dos.videomode_40x25_8x8
.. autodata:: dos_like.dos.videomode_40x25_9x16
.. autodata:: dos_like.dos.videomode_80x25_8x16
.. autodata:: dos_like.dos.videomode_80x25_8x8
.. autodata:: dos_like.dos.videomode_80x25_9x16
.. autodata:: dos_like.dos.videomode_80x43_8x8
.. autodata:: dos_like.dos.videomode_80x50_8x8
.. autodata:: dos_like.dos.videomode_320x200
.. autodata:: dos_like.dos.videomode_320x240
.. autodata:: dos_like.dos.videomode_320x400
.. autodata:: dos_like.dos.videomode_640x200
.. autodata:: dos_like.dos.videomode_640x350
.. autodata:: dos_like.dos.videomode_640x400
.. autodata:: dos_like.dos.videomode_640x480


Fonts
-----
.. autoclass:: dos_like.dos.FontHandle
.. autodata:: dos_like.dos.DEFAULT_FONT_8X8
.. autodata:: dos_like.dos.DEFAULT_FONT_8X16
.. autodata:: dos_like.dos.DEFAULT_FONT_9X16


Sound Banks
-----------
.. autoclass:: dos_like.dos.SoundBankHandle
.. autodata:: dos_like.dos.DEFAULT_SOUNDBANK_AWE32
.. autodata:: dos_like.dos.DEFAULT_SOUNDBANK_SB16


Sound Modes
-----------
.. autoclass:: dos_like.dos.SoundMode
.. autodata:: dos_like.dos.soundmode_8bit_mono_5000
.. autodata:: dos_like.dos.soundmode_8bit_mono_8000
.. autodata:: dos_like.dos.soundmode_8bit_mono_11025
.. autodata:: dos_like.dos.soundmode_8bit_mono_16000
.. autodata:: dos_like.dos.soundmode_8bit_mono_22050
.. autodata:: dos_like.dos.soundmode_8bit_mono_32000
.. autodata:: dos_like.dos.soundmode_8bit_mono_44100
.. autodata:: dos_like.dos.soundmode_16bit_mono_5000
.. autodata:: dos_like.dos.soundmode_16bit_mono_8000
.. autodata:: dos_like.dos.soundmode_16bit_mono_11025
.. autodata:: dos_like.dos.soundmode_16bit_mono_16000
.. autodata:: dos_like.dos.soundmode_16bit_mono_22050
.. autodata:: dos_like.dos.soundmode_16bit_mono_32000
.. autodata:: dos_like.dos.soundmode_16bit_mono_44100
.. autodata:: dos_like.dos.soundmode_8bit_stereo_5000
.. autodata:: dos_like.dos.soundmode_8bit_stereo_8000
.. autodata:: dos_like.dos.soundmode_8bit_stereo_11025
.. autodata:: dos_like.dos.soundmode_8bit_stereo_16000
.. autodata:: dos_like.dos.soundmode_8bit_stereo_22050
.. autodata:: dos_like.dos.soundmode_8bit_stereo_32000
.. autodata:: dos_like.dos.soundmode_8bit_stereo_44100
.. autodata:: dos_like.dos.soundmode_16bit_stereo_5000
.. autodata:: dos_like.dos.soundmode_16bit_stereo_8000
.. autodata:: dos_like.dos.soundmode_16bit_stereo_11025
.. autodata:: dos_like.dos.soundmode_16bit_stereo_16000
.. autodata:: dos_like.dos.soundmode_16bit_stereo_22050
.. autodata:: dos_like.dos.soundmode_16bit_stereo_32000
.. autodata:: dos_like.dos.soundmode_16bit_stereo_44100


Key Codes
---------
.. autoclass:: dos_like.dos.KeyCode
.. autodata:: dos_like.dos.KEY_MODIFIER_RELEASED
.. autodata:: dos_like.dos.KEY_INVALID
.. autodata:: dos_like.dos.KEY_LBUTTON
.. autodata:: dos_like.dos.KEY_RBUTTON
.. autodata:: dos_like.dos.KEY_CANCEL
.. autodata:: dos_like.dos.KEY_MBUTTON
.. autodata:: dos_like.dos.KEY_XBUTTON1
.. autodata:: dos_like.dos.KEY_XBUTTON2
.. autodata:: dos_like.dos.KEY_BACK
.. autodata:: dos_like.dos.KEY_TAB
.. autodata:: dos_like.dos.KEY_CLEAR
.. autodata:: dos_like.dos.KEY_RETURN
.. autodata:: dos_like.dos.KEY_SHIFT
.. autodata:: dos_like.dos.KEY_CONTROL
.. autodata:: dos_like.dos.KEY_MENU
.. autodata:: dos_like.dos.KEY_PAUSE
.. autodata:: dos_like.dos.KEY_CAPITAL
.. autodata:: dos_like.dos.KEY_KANA
.. autodata:: dos_like.dos.KEY_HANGUL
.. autodata:: dos_like.dos.KEY_JUNJA
.. autodata:: dos_like.dos.KEY_FINAL
.. autodata:: dos_like.dos.KEY_HANJA
.. autodata:: dos_like.dos.KEY_KANJI
.. autodata:: dos_like.dos.KEY_ESCAPE
.. autodata:: dos_like.dos.KEY_CONVERT
.. autodata:: dos_like.dos.KEY_NONCONVERT
.. autodata:: dos_like.dos.KEY_ACCEPT
.. autodata:: dos_like.dos.KEY_MODECHANGE
.. autodata:: dos_like.dos.KEY_SPACE
.. autodata:: dos_like.dos.KEY_PRIOR
.. autodata:: dos_like.dos.KEY_NEXT
.. autodata:: dos_like.dos.KEY_END
.. autodata:: dos_like.dos.KEY_HOME
.. autodata:: dos_like.dos.KEY_LEFT
.. autodata:: dos_like.dos.KEY_UP
.. autodata:: dos_like.dos.KEY_RIGHT
.. autodata:: dos_like.dos.KEY_DOWN
.. autodata:: dos_like.dos.KEY_SELECT
.. autodata:: dos_like.dos.KEY_PRINT
.. autodata:: dos_like.dos.KEY_EXEC
.. autodata:: dos_like.dos.KEY_SNAPSHOT
.. autodata:: dos_like.dos.KEY_INSERT
.. autodata:: dos_like.dos.KEY_DELETE
.. autodata:: dos_like.dos.KEY_HELP
.. autodata:: dos_like.dos.KEY_0
.. autodata:: dos_like.dos.KEY_1
.. autodata:: dos_like.dos.KEY_2
.. autodata:: dos_like.dos.KEY_3
.. autodata:: dos_like.dos.KEY_4
.. autodata:: dos_like.dos.KEY_5
.. autodata:: dos_like.dos.KEY_6
.. autodata:: dos_like.dos.KEY_7
.. autodata:: dos_like.dos.KEY_8
.. autodata:: dos_like.dos.KEY_9
.. autodata:: dos_like.dos.KEY_A
.. autodata:: dos_like.dos.KEY_B
.. autodata:: dos_like.dos.KEY_C
.. autodata:: dos_like.dos.KEY_D
.. autodata:: dos_like.dos.KEY_E
.. autodata:: dos_like.dos.KEY_F
.. autodata:: dos_like.dos.KEY_G
.. autodata:: dos_like.dos.KEY_H
.. autodata:: dos_like.dos.KEY_I
.. autodata:: dos_like.dos.KEY_J
.. autodata:: dos_like.dos.KEY_K
.. autodata:: dos_like.dos.KEY_L
.. autodata:: dos_like.dos.KEY_M
.. autodata:: dos_like.dos.KEY_N
.. autodata:: dos_like.dos.KEY_O
.. autodata:: dos_like.dos.KEY_P
.. autodata:: dos_like.dos.KEY_Q
.. autodata:: dos_like.dos.KEY_R
.. autodata:: dos_like.dos.KEY_S
.. autodata:: dos_like.dos.KEY_T
.. autodata:: dos_like.dos.KEY_U
.. autodata:: dos_like.dos.KEY_V
.. autodata:: dos_like.dos.KEY_W
.. autodata:: dos_like.dos.KEY_X
.. autodata:: dos_like.dos.KEY_Y
.. autodata:: dos_like.dos.KEY_Z
.. autodata:: dos_like.dos.KEY_LWIN
.. autodata:: dos_like.dos.KEY_RWIN
.. autodata:: dos_like.dos.KEY_APPS
.. autodata:: dos_like.dos.KEY_SLEEP
.. autodata:: dos_like.dos.KEY_NUMPAD0
.. autodata:: dos_like.dos.KEY_NUMPAD1
.. autodata:: dos_like.dos.KEY_NUMPAD2
.. autodata:: dos_like.dos.KEY_NUMPAD3
.. autodata:: dos_like.dos.KEY_NUMPAD4
.. autodata:: dos_like.dos.KEY_NUMPAD5
.. autodata:: dos_like.dos.KEY_NUMPAD6
.. autodata:: dos_like.dos.KEY_NUMPAD7
.. autodata:: dos_like.dos.KEY_NUMPAD8
.. autodata:: dos_like.dos.KEY_NUMPAD9
.. autodata:: dos_like.dos.KEY_MULTIPLY
.. autodata:: dos_like.dos.KEY_ADD
.. autodata:: dos_like.dos.KEY_SEPARATOR
.. autodata:: dos_like.dos.KEY_SUBTRACT
.. autodata:: dos_like.dos.KEY_DECIMAL
.. autodata:: dos_like.dos.KEY_DIVIDE
.. autodata:: dos_like.dos.KEY_F1
.. autodata:: dos_like.dos.KEY_F2
.. autodata:: dos_like.dos.KEY_F3
.. autodata:: dos_like.dos.KEY_F4
.. autodata:: dos_like.dos.KEY_F5
.. autodata:: dos_like.dos.KEY_F6
.. autodata:: dos_like.dos.KEY_F7
.. autodata:: dos_like.dos.KEY_F8
.. autodata:: dos_like.dos.KEY_F9
.. autodata:: dos_like.dos.KEY_F10
.. autodata:: dos_like.dos.KEY_F11
.. autodata:: dos_like.dos.KEY_F12
.. autodata:: dos_like.dos.KEY_F13
.. autodata:: dos_like.dos.KEY_F14
.. autodata:: dos_like.dos.KEY_F15
.. autodata:: dos_like.dos.KEY_F16
.. autodata:: dos_like.dos.KEY_F17
.. autodata:: dos_like.dos.KEY_F18
.. autodata:: dos_like.dos.KEY_F19
.. autodata:: dos_like.dos.KEY_F20
.. autodata:: dos_like.dos.KEY_F21
.. autodata:: dos_like.dos.KEY_F22
.. autodata:: dos_like.dos.KEY_F23
.. autodata:: dos_like.dos.KEY_F24
.. autodata:: dos_like.dos.KEY_NUMLOCK
.. autodata:: dos_like.dos.KEY_SCROLL
.. autodata:: dos_like.dos.KEY_LSHIFT
.. autodata:: dos_like.dos.KEY_RSHIFT
.. autodata:: dos_like.dos.KEY_LCONTROL
.. autodata:: dos_like.dos.KEY_RCONTROL
.. autodata:: dos_like.dos.KEY_LMENU
.. autodata:: dos_like.dos.KEY_RMENU
.. autodata:: dos_like.dos.KEY_BROWSER_BACK
.. autodata:: dos_like.dos.KEY_BROWSER_FORWARD
.. autodata:: dos_like.dos.KEY_BROWSER_REFRESH
.. autodata:: dos_like.dos.KEY_BROWSER_STOP
.. autodata:: dos_like.dos.KEY_BROWSER_SEARCH
.. autodata:: dos_like.dos.KEY_BROWSER_FAVORITES
.. autodata:: dos_like.dos.KEY_BROWSER_HOME
.. autodata:: dos_like.dos.KEY_VOLUME_MUTE
.. autodata:: dos_like.dos.KEY_VOLUME_DOWN
.. autodata:: dos_like.dos.KEY_VOLUME_UP
.. autodata:: dos_like.dos.KEY_MEDIA_NEXT_TRACK
.. autodata:: dos_like.dos.KEY_MEDIA_PREV_TRACK
.. autodata:: dos_like.dos.KEY_MEDIA_STOP
.. autodata:: dos_like.dos.KEY_MEDIA_PLAY_PAUSE
.. autodata:: dos_like.dos.KEY_LAUNCH_MAIL
.. autodata:: dos_like.dos.KEY_LAUNCH_MEDIA_SELECT
.. autodata:: dos_like.dos.KEY_LAUNCH_APP1
.. autodata:: dos_like.dos.KEY_LAUNCH_APP2
.. autodata:: dos_like.dos.KEY_OEM_1
.. autodata:: dos_like.dos.KEY_OEM_PLUS
.. autodata:: dos_like.dos.KEY_OEM_COMMA
.. autodata:: dos_like.dos.KEY_OEM_MINUS
.. autodata:: dos_like.dos.KEY_OEM_PERIOD
.. autodata:: dos_like.dos.KEY_OEM_2
.. autodata:: dos_like.dos.KEY_OEM_3
.. autodata:: dos_like.dos.KEY_OEM_4
.. autodata:: dos_like.dos.KEY_OEM_5
.. autodata:: dos_like.dos.KEY_OEM_6
.. autodata:: dos_like.dos.KEY_OEM_7
.. autodata:: dos_like.dos.KEY_OEM_8
.. autodata:: dos_like.dos.KEY_OEM_102
.. autodata:: dos_like.dos.KEY_PROCESSKEY
.. autodata:: dos_like.dos.KEY_ATTN
.. autodata:: dos_like.dos.KEY_CRSEL
.. autodata:: dos_like.dos.KEY_EXSEL
.. autodata:: dos_like.dos.KEY_EREOF
.. autodata:: dos_like.dos.KEY_PLAY
.. autodata:: dos_like.dos.KEY_ZOOM
.. autodata:: dos_like.dos.KEY_NONAME
.. autodata:: dos_like.dos.KEY_PA1
.. autodata:: dos_like.dos.KEY_OEM_CLEAR
.. autodata:: dos_like.dos.KEYCOUNT
.. autodata:: dos_like.dos.KEYPADDING
