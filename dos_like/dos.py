from __future__ import annotations

import collections
import dataclasses
import enum
import os
import pathlib
import typing
from typing import Sized, Union

try:
    from typing import TypeAlias  # type: ignore
except ImportError:
    from typing_extensions import TypeAlias  # type: ignore

from . import _dos, cp437, int_with_flags

__all__ = [
    'DEFAULT_FONT_8X16',
    'DEFAULT_FONT_8X8',
    'DEFAULT_FONT_9X16',
    'DEFAULT_SOUNDBANK_AWE32',
    'DEFAULT_SOUNDBANK_SB16',
    'FontHandle',
    'GIF',
    'KEYCOUNT',
    'KEYPADDING',
    'KEY_0',
    'KEY_1',
    'KEY_2',
    'KEY_3',
    'KEY_4',
    'KEY_5',
    'KEY_6',
    'KEY_7',
    'KEY_8',
    'KEY_9',
    'KEY_A',
    'KEY_ACCEPT',
    'KEY_ADD',
    'KEY_APPS',
    'KEY_ATTN',
    'KEY_B',
    'KEY_BACK',
    'KEY_BROWSER_BACK',
    'KEY_BROWSER_FAVORITES',
    'KEY_BROWSER_FORWARD',
    'KEY_BROWSER_HOME',
    'KEY_BROWSER_REFRESH',
    'KEY_BROWSER_SEARCH',
    'KEY_BROWSER_STOP',
    'KEY_C',
    'KEY_CANCEL',
    'KEY_CAPITAL',
    'KEY_CLEAR',
    'KEY_CONTROL',
    'KEY_CONVERT',
    'KEY_CRSEL',
    'KEY_D',
    'KEY_DECIMAL',
    'KEY_DELETE',
    'KEY_DIVIDE',
    'KEY_DOWN',
    'KEY_E',
    'KEY_END',
    'KEY_EREOF',
    'KEY_ESCAPE',
    'KEY_EXEC',
    'KEY_EXSEL',
    'KEY_F',
    'KEY_F1',
    'KEY_F10',
    'KEY_F11',
    'KEY_F12',
    'KEY_F13',
    'KEY_F14',
    'KEY_F15',
    'KEY_F16',
    'KEY_F17',
    'KEY_F18',
    'KEY_F19',
    'KEY_F2',
    'KEY_F20',
    'KEY_F21',
    'KEY_F22',
    'KEY_F23',
    'KEY_F24',
    'KEY_F3',
    'KEY_F4',
    'KEY_F5',
    'KEY_F6',
    'KEY_F7',
    'KEY_F8',
    'KEY_F9',
    'KEY_FINAL',
    'KEY_G',
    'KEY_H',
    'KEY_HANGUL',
    'KEY_HANJA',
    'KEY_HELP',
    'KEY_HOME',
    'KEY_I',
    'KEY_INSERT',
    'KEY_INVALID',
    'KEY_J',
    'KEY_JUNJA',
    'KEY_K',
    'KEY_KANA',
    'KEY_KANJI',
    'KEY_L',
    'KEY_LAUNCH_APP1',
    'KEY_LAUNCH_APP2',
    'KEY_LAUNCH_MAIL',
    'KEY_LAUNCH_MEDIA_SELECT',
    'KEY_LBUTTON',
    'KEY_LCONTROL',
    'KEY_LEFT',
    'KEY_LMENU',
    'KEY_LSHIFT',
    'KEY_LWIN',
    'KEY_M',
    'KEY_MBUTTON',
    'KEY_MEDIA_NEXT_TRACK',
    'KEY_MEDIA_PLAY_PAUSE',
    'KEY_MEDIA_PREV_TRACK',
    'KEY_MEDIA_STOP',
    'KEY_MENU',
    'KEY_MODECHANGE',
    'KEY_MODIFIER_RELEASED',
    'KEY_MULTIPLY',
    'KEY_N',
    'KEY_NEXT',
    'KEY_NONAME',
    'KEY_NONCONVERT',
    'KEY_NUMLOCK',
    'KEY_NUMPAD0',
    'KEY_NUMPAD1',
    'KEY_NUMPAD2',
    'KEY_NUMPAD3',
    'KEY_NUMPAD4',
    'KEY_NUMPAD5',
    'KEY_NUMPAD6',
    'KEY_NUMPAD7',
    'KEY_NUMPAD8',
    'KEY_NUMPAD9',
    'KEY_O',
    'KEY_OEM_1',
    'KEY_OEM_102',
    'KEY_OEM_2',
    'KEY_OEM_3',
    'KEY_OEM_4',
    'KEY_OEM_5',
    'KEY_OEM_6',
    'KEY_OEM_7',
    'KEY_OEM_8',
    'KEY_OEM_CLEAR',
    'KEY_OEM_COMMA',
    'KEY_OEM_MINUS',
    'KEY_OEM_PERIOD',
    'KEY_OEM_PLUS',
    'KEY_P',
    'KEY_PA1',
    'KEY_PAUSE',
    'KEY_PLAY',
    'KEY_PRINT',
    'KEY_PRIOR',
    'KEY_PROCESSKEY',
    'KEY_Q',
    'KEY_R',
    'KEY_RBUTTON',
    'KEY_RCONTROL',
    'KEY_RETURN',
    'KEY_RIGHT',
    'KEY_RMENU',
    'KEY_RSHIFT',
    'KEY_RWIN',
    'KEY_S',
    'KEY_SCROLL',
    'KEY_SELECT',
    'KEY_SEPARATOR',
    'KEY_SHIFT',
    'KEY_SLEEP',
    'KEY_SNAPSHOT',
    'KEY_SPACE',
    'KEY_SUBTRACT',
    'KEY_T',
    'KEY_TAB',
    'KEY_U',
    'KEY_UP',
    'KEY_V',
    'KEY_VOLUME_DOWN',
    'KEY_VOLUME_MUTE',
    'KEY_VOLUME_UP',
    'KEY_W',
    'KEY_X',
    'KEY_XBUTTON1',
    'KEY_XBUTTON2',
    'KEY_Y',
    'KEY_Z',
    'KEY_ZOOM',
    'MUSIC_CHANNELS',
    'Points',
    'RGB',
    'SOUND_CHANNELS',
    'SoundBankHandle',
    'VideoMode',
    'allnotesoff',
    'bar',
    'blit',
    'boundaryfill',
    'centertextxy',
    'circle',
    'clearscreen',
    'clrscr',
    'cputs',
    'createmus',
    'createsound',
    'cursoff',
    'curson',
    'drawpoly',
    'ellipse',
    'fillcircle',
    'fillellipse',
    'fillpoly',
    'floodfill',
    'getcolor',
    'getpal',
    'getpixel',
    'gotoxy',
    'hline',
    'installuserfont',
    'installuserfont',
    'installusersoundbank',
    'keystate',
    'line',
    'loadgif',
    'loadmid',
    'loadmod',
    'loadmus',
    'loadopb',
    'loadwav',
    'maskblit',
    'mouserelx',
    'mouserely',
    'mousex',
    'mousey',
    'musicplaying',
    'musicvolume',
    'new_buffer',
    'noteoff',
    'noteon',
    'outtextxy',
    'playmusic',
    'playsound',
    'putpixel',
    'readchars',
    'readkeys',
    'rectangle',
    'resetdrawtarget',
    'screenbuffer',
    'screenheight',
    'screenwidth',
    'setcolor',
    'setdoublebuffer',
    'setdrawtarget',
    'setinstrument',
    'setpal',
    'setsoundbank',
    'setsoundmode',
    'settextstyle',
    'settextstyle',
    'setvideomode',
    'shuttingdown',
    'soundmode_16bit_mono_11025',
    'soundmode_16bit_mono_16000',
    'soundmode_16bit_mono_22050',
    'soundmode_16bit_mono_32000',
    'soundmode_16bit_mono_44100',
    'soundmode_16bit_mono_5000',
    'soundmode_16bit_mono_8000',
    'soundmode_16bit_stereo_11025',
    'soundmode_16bit_stereo_16000',
    'soundmode_16bit_stereo_22050',
    'soundmode_16bit_stereo_32000',
    'soundmode_16bit_stereo_44100',
    'soundmode_16bit_stereo_5000',
    'soundmode_16bit_stereo_8000',
    'soundmode_8bit_mono_11025',
    'soundmode_8bit_mono_16000',
    'soundmode_8bit_mono_22050',
    'soundmode_8bit_mono_32000',
    'soundmode_8bit_mono_44100',
    'soundmode_8bit_mono_5000',
    'soundmode_8bit_mono_8000',
    'soundmode_8bit_stereo_11025',
    'soundmode_8bit_stereo_16000',
    'soundmode_8bit_stereo_22050',
    'soundmode_8bit_stereo_32000',
    'soundmode_8bit_stereo_44100',
    'soundmode_8bit_stereo_5000',
    'soundmode_8bit_stereo_8000',
    'soundplaying',
    'soundvolume',
    'stopmusic',
    'stopsound',
    'swapbuffers',
    'textbackground',
    'textcolor',
    'videomode_320x200',
    'videomode_320x240',
    'videomode_320x400',
    'videomode_40x25_8x8',
    'videomode_40x25_9x16',
    'videomode_640x200',
    'videomode_640x350',
    'videomode_640x400',
    'videomode_640x480',
    'videomode_80x25_8x16',
    'videomode_80x25_8x8',
    'videomode_80x25_9x16',
    'videomode_80x43_8x8',
    'videomode_80x50_8x8',
    'waitvbl',
    'wherex',
    'wherey',
    'wraptextxy',
]

#
# CONSTANTS, TYPES, AND ENUMS
# ---------------------------

# Screen buffer size is not exposed by the dos-like API
SCREEN_BUFFER_SIZE = 1024 * 1024

MUSIC_CHANNELS = _dos.lib.MUSIC_CHANNELS
"""Maximum number of channels for music notes."""

SOUND_CHANNELS = _dos.lib.SOUND_CHANNELS
"""Maximum number of channels for sounds."""

if typing.TYPE_CHECKING:
    # Type checker gets to use Readable/WriteableBuffer, but needs bogus cffi
    # CData and buffer types.
    import _typeshed
    import cffi
    buffer: TypeAlias = cffi.buffer
    CData: TypeAlias = cffi.CData
    WriteableBuffer: TypeAlias = Union[buffer, _typeshed.WriteableBuffer]
    ReadableBuffer: TypeAlias = Union[buffer, _typeshed.ReadableBuffer]
else:
    # Runtime can use the real cffi types, but can't use the typeshed
    # Readable/WriteableBuffer types.
    CData = _dos.ffi.CData
    buffer = _dos.ffi.buffer
    WriteableBuffer: TypeAlias = Union[bytearray, memoryview, CData, buffer]
    ReadableBuffer: TypeAlias = Union[WriteableBuffer, bytes]

Points: TypeAlias = Union[list[int], list[tuple[int, int]], ReadableBuffer]
Samples: TypeAlias = Union[list[int], ReadableBuffer]

RGB = collections.namedtuple('RGB', 'r g b')
RGB.__doc__ = 'Red, green, and blue color tuple'
RGB.r.__doc__ = 'Red channel, valid values 0..63'
RGB.g.__doc__ = 'Green channel, valid values 0..63'
RGB.b.__doc__ = 'Blue channel, valid values 0..63'

# Reference to the current music to prevent it from being garbage collected
_current_music: Music | None = None

# Reference to the current draw target to prevent it from being garbage
# collected
_current_draw_target: WriteableBuffer | None = None


def _data_for_points(points: Points) -> CData:
    """Return a CFFI data object for an array of ints representing 2D points.

    :param points: a buffer of ints, a list of ints, or a list of (x, y) tuples

    """
    if not isinstance(points, list):
        # Adapt existing buffer
        return _dos.ffi.from_buffer('int[]', points)
    if len(points) < 2:
        raise ValueError('At least two points are required')
    if isinstance(points[0], tuple):
        xy: list[int] = []
        for point in typing.cast(list[tuple[int, int]], points):
            xy.extend(point)
    else:
        xy = typing.cast(list[int], points)
    return _dos.ffi.new('int[]', xy)


def _data_for_samples(samples: Samples) -> tuple[CData, int]:
    """Return CFFI data for an array of shorts representing audio samples.

    :param samples: a buffer of shorts, or a list of ints
    :return: a tuple of the sound data, and its size in bytes.  The __len__ of
        the return value is not useful, since it may return the size in bytes
        *or* in words
    :raises ValueError: if **samples** is a buffer of unknown size

    """
    if isinstance(samples, list):
        result = _dos.ffi.new('short[]', samples)
        return result, len(result) * 2
    # Adapt existing buffer
    result = _dos.ffi.from_buffer('short[]', samples)
    return result, buffer_size(samples)


@dataclasses.dataclass
class GIF:
    """GIF image."""
    filename: str
    """GIF filename"""

    width: int
    """Image width in pixels"""

    height: int
    """Image height in pixels"""

    palette: list[RGB]
    """Image color map"""

    pixels: buffer
    """Image pixels in row-major order.  Values are indices of
    :attr:`palette`."""

    _pixels_ptr: CData

    def __del__(self):
        _dos.lib.free(self._pixels_ptr)


# mypy can't do dynamic enums
VideoMode = enum.Enum(  # type: ignore
    'VideoMode', {
        k.removeprefix('videomode_'): v
        for k, v in _dos.lib.__dict__.items() if k.startswith('videomode_')
    })
VideoMode.__doc__ = 'Enumeration of text and graphics modes.'
videomode_40x25_8x8: VideoMode = getattr(VideoMode, '40x25_8x8')
videomode_40x25_8x8.__doc__ = '40x25 text mode with 8x8 characters.'
videomode_40x25_9x16: VideoMode = getattr(VideoMode, '40x25_9x16')
videomode_40x25_9x16.__doc__ = '40x25 text mode with 9x16 characters.'
videomode_80x25_8x16: VideoMode = getattr(VideoMode, '80x25_8x16')
videomode_80x25_8x16.__doc__ = '80x25 text mode with 8x16 characters.'
videomode_80x25_8x8: VideoMode = getattr(VideoMode, '80x25_8x8')
videomode_80x25_8x8.__doc__ = '80x25 text mode with 8x8 characters.'
videomode_80x25_9x16: VideoMode = getattr(VideoMode, '80x25_9x16')
videomode_80x25_9x16.__doc__ = '80x25 text mode with 9x16 characters.'
videomode_80x43_8x8: VideoMode = getattr(VideoMode, '80x43_8x8')
videomode_80x43_8x8.__doc__ = '80x43 text mode with 8x8 characters.'
videomode_80x50_8x8: VideoMode = getattr(VideoMode, '80x50_8x8')
videomode_80x50_8x8.__doc__ = '80x50 text mode with 8x8 characters.'
videomode_320x200: VideoMode = getattr(VideoMode, '320x200')
videomode_320x200.__doc__ = '320x200 graphics mode.'
videomode_320x240: VideoMode = getattr(VideoMode, '320x240')
videomode_320x240.__doc__ = '320x240 graphics mode.'
videomode_320x400: VideoMode = getattr(VideoMode, '320x400')
videomode_320x400.__doc__ = '320x400 graphics mode.'
videomode_640x200: VideoMode = getattr(VideoMode, '640x200')
videomode_640x200.__doc__ = '640x200 graphics mode.'
videomode_640x350: VideoMode = getattr(VideoMode, '640x350')
videomode_640x350.__doc__ = '640x350 graphics mode.'
videomode_640x400: VideoMode = getattr(VideoMode, '640x400')
videomode_640x400.__doc__ = '640x400 graphics mode.'
videomode_640x480: VideoMode = getattr(VideoMode, '640x480')
videomode_640x480.__doc__ = '640x480 graphics mode.'


class FontHandle(int):
    """Handle to an installed font."""
    pass


DEFAULT_FONT_8X8: FontHandle = FontHandle(_dos.lib.DEFAULT_FONT_8X8)
DEFAULT_FONT_8X8.__doc__ = '8x8 font'
DEFAULT_FONT_8X16: FontHandle = FontHandle(_dos.lib.DEFAULT_FONT_8X16)
DEFAULT_FONT_8X16.__doc__ = '8x16 font'
DEFAULT_FONT_9X16: FontHandle = FontHandle(_dos.lib.DEFAULT_FONT_9X16)
DEFAULT_FONT_9X16.__doc__ = '9x16 font'


class SoundBankHandle(int):
    """Handle to an installed sound bank."""
    pass


DEFAULT_SOUNDBANK_AWE32: SoundBankHandle = SoundBankHandle(
    _dos.lib.DEFAULT_SOUNDBANK_AWE32)
DEFAULT_SOUNDBANK_AWE32.__doc__ = 'Sound Blaster AWE32 sound bank.'
DEFAULT_SOUNDBANK_SB16: SoundBankHandle = SoundBankHandle(
    _dos.lib.DEFAULT_SOUNDBANK_SB16)
DEFAULT_SOUNDBANK_SB16.__doc__ = 'Sound Blaster 16 sound bank.'


@dataclasses.dataclass
class Music:
    """Loaded music."""

    filename: str | None
    """Original filename, if loaded from disk."""

    _music_ptr: CData

    def __del__(self):
        _dos.lib.free(self._music_ptr)


# mypy can't do dynamic enums
SoundMode = enum.Enum(  # type: ignore
    'SoundMode', {
        k.removeprefix('soundmode_'): v
        for k, v in _dos.lib.__dict__.items() if k.startswith('soundmode_')
    })
SoundMode.__doc__ = 'Enumeration of sound modes.'
soundmode_8bit_mono_5000: SoundMode = getattr(SoundMode, '8bit_mono_5000')
soundmode_8bit_mono_5000.__doc__ = '8-bit, 1 channel, 5,000 Hz sound mode'
soundmode_8bit_mono_8000: SoundMode = getattr(SoundMode, '8bit_mono_8000')
soundmode_8bit_mono_8000.__doc__ = '8-bit, 1 channel, 8,000 Hz sound mode'
soundmode_8bit_mono_11025: SoundMode = getattr(SoundMode, '8bit_mono_11025')
soundmode_8bit_mono_11025.__doc__ = '8-bit, 1 channel, 11,025 Hz sound mode'
soundmode_8bit_mono_16000: SoundMode = getattr(SoundMode, '8bit_mono_16000')
soundmode_8bit_mono_16000.__doc__ = '8-bit, 1 channel, 16,000 Hz sound mode'
soundmode_8bit_mono_22050: SoundMode = getattr(SoundMode, '8bit_mono_22050')
soundmode_8bit_mono_22050.__doc__ = '8-bit, 1 channel, 22,050 Hz sound mode'
soundmode_8bit_mono_32000: SoundMode = getattr(SoundMode, '8bit_mono_32000')
soundmode_8bit_mono_32000.__doc__ = '8-bit, 1 channel, 32,000 Hz sound mode'
soundmode_8bit_mono_44100: SoundMode = getattr(SoundMode, '8bit_mono_44100')
soundmode_8bit_mono_44100.__doc__ = '8-bit, 1 channel, 44,100 Hz sound mode'
soundmode_16bit_mono_5000: SoundMode = getattr(SoundMode, '16bit_mono_5000')
soundmode_16bit_mono_5000.__doc__ = '16-bit, 1 channel, 5,000 Hz sound mode'
soundmode_16bit_mono_8000: SoundMode = getattr(SoundMode, '16bit_mono_8000')
soundmode_16bit_mono_8000.__doc__ = '16-bit, 1 channel, 8,000 Hz sound mode'
soundmode_16bit_mono_11025: SoundMode = getattr(SoundMode, '16bit_mono_11025')
soundmode_16bit_mono_11025.__doc__ = '16-bit, 1 channel, 11,025 Hz sound mode'
soundmode_16bit_mono_16000: SoundMode = getattr(SoundMode, '16bit_mono_16000')
soundmode_16bit_mono_16000.__doc__ = '16-bit, 1 channel, 16,000 Hz sound mode'
soundmode_16bit_mono_22050: SoundMode = getattr(SoundMode, '16bit_mono_22050')
soundmode_16bit_mono_22050.__doc__ = '16-bit, 1 channel, 22,050 Hz sound mode'
soundmode_16bit_mono_32000: SoundMode = getattr(SoundMode, '16bit_mono_32000')
soundmode_16bit_mono_32000.__doc__ = '16-bit, 1 channel, 32,000 Hz sound mode'
soundmode_16bit_mono_44100: SoundMode = getattr(SoundMode, '16bit_mono_44100')
soundmode_16bit_mono_44100.__doc__ = '16-bit, 1 channel, 44,100 Hz sound mode'
soundmode_8bit_stereo_5000: SoundMode = getattr(SoundMode, '8bit_stereo_5000')
soundmode_8bit_stereo_5000.__doc__ = '8-bit, 2 channel, 5,000 Hz sound mode'
soundmode_8bit_stereo_8000: SoundMode = getattr(SoundMode, '8bit_stereo_8000')
soundmode_8bit_stereo_8000.__doc__ = '8-bit, 2 channel, 8,000 Hz sound mode'
soundmode_8bit_stereo_11025: SoundMode = getattr(SoundMode,
                                                 '8bit_stereo_11025')
soundmode_8bit_stereo_11025.__doc__ = '8-bit, 2 channel, 11,025 Hz sound mode'
soundmode_8bit_stereo_16000: SoundMode = getattr(SoundMode,
                                                 '8bit_stereo_16000')
soundmode_8bit_stereo_16000.__doc__ = '8-bit, 2 channel, 16,000 Hz sound mode'
soundmode_8bit_stereo_22050: SoundMode = getattr(SoundMode,
                                                 '8bit_stereo_22050')
soundmode_8bit_stereo_22050.__doc__ = '8-bit, 2 channel, 22,050 Hz sound mode'
soundmode_8bit_stereo_32000: SoundMode = getattr(SoundMode,
                                                 '8bit_stereo_32000')
soundmode_8bit_stereo_32000.__doc__ = '8-bit, 2 channel, 32,000 Hz sound mode'
soundmode_8bit_stereo_44100: SoundMode = getattr(SoundMode,
                                                 '8bit_stereo_44100')
soundmode_8bit_stereo_44100.__doc__ = '8-bit, 2 channel, 44,100 Hz sound mode'
soundmode_16bit_stereo_5000: SoundMode = getattr(SoundMode,
                                                 '16bit_stereo_5000')
soundmode_16bit_stereo_5000.__doc__ = '16-bit, 2 channel, 5,000 Hz sound mode'
soundmode_16bit_stereo_8000: SoundMode = getattr(SoundMode,
                                                 '16bit_stereo_8000')
soundmode_16bit_stereo_8000.__doc__ = '16-bit, 2 channel, 8,000 Hz sound mode'
soundmode_16bit_stereo_11025: SoundMode = getattr(SoundMode,
                                                  '16bit_stereo_11025')
soundmode_16bit_stereo_11025.__doc__ = ('16-bit, 2 channel, 11,025 Hz sound '
                                        'mode')
soundmode_16bit_stereo_16000: SoundMode = getattr(SoundMode,
                                                  '16bit_stereo_16000')
soundmode_16bit_stereo_16000.__doc__ = ('16-bit, 2 channel, 16,000 Hz sound '
                                        'mode')
soundmode_16bit_stereo_22050: SoundMode = getattr(SoundMode,
                                                  '16bit_stereo_22050')
soundmode_16bit_stereo_22050.__doc__ = ('16-bit, 2 channel, 22,050 Hz sound '
                                        'mode')
soundmode_16bit_stereo_32000: SoundMode = getattr(SoundMode,
                                                  '16bit_stereo_32000')
soundmode_16bit_stereo_32000.__doc__ = ('16-bit, 2 channel, 32,000 Hz sound '
                                        'mode')
soundmode_16bit_stereo_44100: SoundMode = getattr(SoundMode,
                                                  '16bit_stereo_44100')
soundmode_16bit_stereo_44100.__doc__ = ('16-bit, 2 channel, 44,100 Hz sound'
                                        'mode')


@dataclasses.dataclass
class Sound:
    """Loaded sound."""
    filename: str | None
    """Original filename, if loaded from disk."""

    _sound_ptr: CData

    def __del__(self):
        _dos.lib.free(self._sound_ptr)


if typing.TYPE_CHECKING:
    # mypy doesn't understand enum subclasses
    # https://github.com/python/mypy/issues/6037
    class KeyCode:
        _flags_: dict[str, int]
        value: int

        def __init__(self, value: int):
            ...
else:
    KeyCode = int_with_flags.IntWithFlags(
        'KeyCode', {
            k.removeprefix('KEY_'): v
            for k, v in _dos.lib.__dict__.items() if k.startswith('KEY')
        })
KeyCode._flags_ = {'KEY_MODIFIER_RELEASED': _dos.lib.KEY_MODIFIER_RELEASED}
KeyCode.__doc__ = """\
    Keyboard code.

    May be bitwise or'd with :data:`KEY_MODIFIER_RELEASED` to indicate a key
    has been released.  Otherwise indicates a key has been pressed.

    """
# TODO: these all need docstrings
KEY_INVALID: KeyCode = getattr(KeyCode, 'INVALID')
KEY_LBUTTON: KeyCode = getattr(KeyCode, 'LBUTTON')
KEY_RBUTTON: KeyCode = getattr(KeyCode, 'RBUTTON')
KEY_CANCEL: KeyCode = getattr(KeyCode, 'CANCEL')
KEY_MBUTTON: KeyCode = getattr(KeyCode, 'MBUTTON')
KEY_XBUTTON1: KeyCode = getattr(KeyCode, 'XBUTTON1')
KEY_XBUTTON2: KeyCode = getattr(KeyCode, 'XBUTTON2')
KEY_BACK: KeyCode = getattr(KeyCode, 'BACK')
KEY_TAB: KeyCode = getattr(KeyCode, 'TAB')
KEY_CLEAR: KeyCode = getattr(KeyCode, 'CLEAR')
KEY_RETURN: KeyCode = getattr(KeyCode, 'RETURN')
KEY_SHIFT: KeyCode = getattr(KeyCode, 'SHIFT')
KEY_CONTROL: KeyCode = getattr(KeyCode, 'CONTROL')
KEY_MENU: KeyCode = getattr(KeyCode, 'MENU')
KEY_PAUSE: KeyCode = getattr(KeyCode, 'PAUSE')
KEY_CAPITAL: KeyCode = getattr(KeyCode, 'CAPITAL')
KEY_KANA: KeyCode = getattr(KeyCode, 'KANA')
KEY_HANGUL: KeyCode = KEY_KANA
KEY_JUNJA: KeyCode = getattr(KeyCode, 'JUNJA')
KEY_FINAL: KeyCode = getattr(KeyCode, 'FINAL')
KEY_HANJA: KeyCode = getattr(KeyCode, 'HANJA')
KEY_KANJI = KEY_HANJA
KEY_ESCAPE: KeyCode = getattr(KeyCode, 'ESCAPE')
KEY_CONVERT: KeyCode = getattr(KeyCode, 'CONVERT')
KEY_NONCONVERT: KeyCode = getattr(KeyCode, 'NONCONVERT')
KEY_ACCEPT: KeyCode = getattr(KeyCode, 'ACCEPT')
KEY_MODECHANGE: KeyCode = getattr(KeyCode, 'MODECHANGE')
KEY_SPACE: KeyCode = getattr(KeyCode, 'SPACE')
KEY_PRIOR: KeyCode = getattr(KeyCode, 'PRIOR')
KEY_NEXT: KeyCode = getattr(KeyCode, 'NEXT')
KEY_END: KeyCode = getattr(KeyCode, 'END')
KEY_HOME: KeyCode = getattr(KeyCode, 'HOME')
KEY_LEFT: KeyCode = getattr(KeyCode, 'LEFT')
KEY_UP: KeyCode = getattr(KeyCode, 'UP')
KEY_RIGHT: KeyCode = getattr(KeyCode, 'RIGHT')
KEY_DOWN: KeyCode = getattr(KeyCode, 'DOWN')
KEY_SELECT: KeyCode = getattr(KeyCode, 'SELECT')
KEY_PRINT: KeyCode = getattr(KeyCode, 'PRINT')
KEY_EXEC: KeyCode = getattr(KeyCode, 'EXEC')
KEY_SNAPSHOT: KeyCode = getattr(KeyCode, 'SNAPSHOT')
KEY_INSERT: KeyCode = getattr(KeyCode, 'INSERT')
KEY_DELETE: KeyCode = getattr(KeyCode, 'DELETE')
KEY_HELP: KeyCode = getattr(KeyCode, 'HELP')
KEY_0: KeyCode = getattr(KeyCode, '0')
KEY_1: KeyCode = getattr(KeyCode, '1')
KEY_2: KeyCode = getattr(KeyCode, '2')
KEY_3: KeyCode = getattr(KeyCode, '3')
KEY_4: KeyCode = getattr(KeyCode, '4')
KEY_5: KeyCode = getattr(KeyCode, '5')
KEY_6: KeyCode = getattr(KeyCode, '6')
KEY_7: KeyCode = getattr(KeyCode, '7')
KEY_8: KeyCode = getattr(KeyCode, '8')
KEY_9: KeyCode = getattr(KeyCode, '9')
KEY_A: KeyCode = getattr(KeyCode, 'A')
KEY_B: KeyCode = getattr(KeyCode, 'B')
KEY_C: KeyCode = getattr(KeyCode, 'C')
KEY_D: KeyCode = getattr(KeyCode, 'D')
KEY_E: KeyCode = getattr(KeyCode, 'E')
KEY_F: KeyCode = getattr(KeyCode, 'F')
KEY_G: KeyCode = getattr(KeyCode, 'G')
KEY_H: KeyCode = getattr(KeyCode, 'H')
KEY_I: KeyCode = getattr(KeyCode, 'I')
KEY_J: KeyCode = getattr(KeyCode, 'J')
KEY_K: KeyCode = getattr(KeyCode, 'K')
KEY_L: KeyCode = getattr(KeyCode, 'L')
KEY_M: KeyCode = getattr(KeyCode, 'M')
KEY_N: KeyCode = getattr(KeyCode, 'N')
KEY_O: KeyCode = getattr(KeyCode, 'O')
KEY_P: KeyCode = getattr(KeyCode, 'P')
KEY_Q: KeyCode = getattr(KeyCode, 'Q')
KEY_R: KeyCode = getattr(KeyCode, 'R')
KEY_S: KeyCode = getattr(KeyCode, 'S')
KEY_T: KeyCode = getattr(KeyCode, 'T')
KEY_U: KeyCode = getattr(KeyCode, 'U')
KEY_V: KeyCode = getattr(KeyCode, 'V')
KEY_W: KeyCode = getattr(KeyCode, 'W')
KEY_X: KeyCode = getattr(KeyCode, 'X')
KEY_Y: KeyCode = getattr(KeyCode, 'Y')
KEY_Z: KeyCode = getattr(KeyCode, 'Z')
KEY_LWIN: KeyCode = getattr(KeyCode, 'LWIN')
KEY_RWIN: KeyCode = getattr(KeyCode, 'RWIN')
KEY_APPS: KeyCode = getattr(KeyCode, 'APPS')
KEY_SLEEP: KeyCode = getattr(KeyCode, 'SLEEP')
KEY_NUMPAD0: KeyCode = getattr(KeyCode, 'NUMPAD0')
KEY_NUMPAD1: KeyCode = getattr(KeyCode, 'NUMPAD1')
KEY_NUMPAD2: KeyCode = getattr(KeyCode, 'NUMPAD2')
KEY_NUMPAD3: KeyCode = getattr(KeyCode, 'NUMPAD3')
KEY_NUMPAD4: KeyCode = getattr(KeyCode, 'NUMPAD4')
KEY_NUMPAD5: KeyCode = getattr(KeyCode, 'NUMPAD5')
KEY_NUMPAD6: KeyCode = getattr(KeyCode, 'NUMPAD6')
KEY_NUMPAD7: KeyCode = getattr(KeyCode, 'NUMPAD7')
KEY_NUMPAD8: KeyCode = getattr(KeyCode, 'NUMPAD8')
KEY_NUMPAD9: KeyCode = getattr(KeyCode, 'NUMPAD9')
KEY_MULTIPLY: KeyCode = getattr(KeyCode, 'MULTIPLY')
KEY_ADD: KeyCode = getattr(KeyCode, 'ADD')
KEY_SEPARATOR: KeyCode = getattr(KeyCode, 'SEPARATOR')
KEY_SUBTRACT: KeyCode = getattr(KeyCode, 'SUBTRACT')
KEY_DECIMAL: KeyCode = getattr(KeyCode, 'DECIMAL')
KEY_DIVIDE: KeyCode = getattr(KeyCode, 'DIVIDE')
KEY_F1: KeyCode = getattr(KeyCode, 'F1')
KEY_F2: KeyCode = getattr(KeyCode, 'F2')
KEY_F3: KeyCode = getattr(KeyCode, 'F3')
KEY_F4: KeyCode = getattr(KeyCode, 'F4')
KEY_F5: KeyCode = getattr(KeyCode, 'F5')
KEY_F6: KeyCode = getattr(KeyCode, 'F6')
KEY_F7: KeyCode = getattr(KeyCode, 'F7')
KEY_F8: KeyCode = getattr(KeyCode, 'F8')
KEY_F9: KeyCode = getattr(KeyCode, 'F9')
KEY_F10: KeyCode = getattr(KeyCode, 'F10')
KEY_F11: KeyCode = getattr(KeyCode, 'F11')
KEY_F12: KeyCode = getattr(KeyCode, 'F12')
KEY_F13: KeyCode = getattr(KeyCode, 'F13')
KEY_F14: KeyCode = getattr(KeyCode, 'F14')
KEY_F15: KeyCode = getattr(KeyCode, 'F15')
KEY_F16: KeyCode = getattr(KeyCode, 'F16')
KEY_F17: KeyCode = getattr(KeyCode, 'F17')
KEY_F18: KeyCode = getattr(KeyCode, 'F18')
KEY_F19: KeyCode = getattr(KeyCode, 'F19')
KEY_F20: KeyCode = getattr(KeyCode, 'F20')
KEY_F21: KeyCode = getattr(KeyCode, 'F21')
KEY_F22: KeyCode = getattr(KeyCode, 'F22')
KEY_F23: KeyCode = getattr(KeyCode, 'F23')
KEY_F24: KeyCode = getattr(KeyCode, 'F24')
KEY_NUMLOCK: KeyCode = getattr(KeyCode, 'NUMLOCK')
KEY_SCROLL: KeyCode = getattr(KeyCode, 'SCROLL')
KEY_LSHIFT: KeyCode = getattr(KeyCode, 'LSHIFT')
KEY_RSHIFT: KeyCode = getattr(KeyCode, 'RSHIFT')
KEY_LCONTROL: KeyCode = getattr(KeyCode, 'LCONTROL')
KEY_RCONTROL: KeyCode = getattr(KeyCode, 'RCONTROL')
KEY_LMENU: KeyCode = getattr(KeyCode, 'LMENU')
KEY_RMENU: KeyCode = getattr(KeyCode, 'RMENU')
KEY_BROWSER_BACK: KeyCode = getattr(KeyCode, 'BROWSER_BACK')
KEY_BROWSER_FORWARD: KeyCode = getattr(KeyCode, 'BROWSER_FORWARD')
KEY_BROWSER_REFRESH: KeyCode = getattr(KeyCode, 'BROWSER_REFRESH')
KEY_BROWSER_STOP: KeyCode = getattr(KeyCode, 'BROWSER_STOP')
KEY_BROWSER_SEARCH: KeyCode = getattr(KeyCode, 'BROWSER_SEARCH')
KEY_BROWSER_FAVORITES: KeyCode = getattr(KeyCode, 'BROWSER_FAVORITES')
KEY_BROWSER_HOME: KeyCode = getattr(KeyCode, 'BROWSER_HOME')
KEY_VOLUME_MUTE: KeyCode = getattr(KeyCode, 'VOLUME_MUTE')
KEY_VOLUME_DOWN: KeyCode = getattr(KeyCode, 'VOLUME_DOWN')
KEY_VOLUME_UP: KeyCode = getattr(KeyCode, 'VOLUME_UP')
KEY_MEDIA_NEXT_TRACK: KeyCode = getattr(KeyCode, 'MEDIA_NEXT_TRACK')
KEY_MEDIA_PREV_TRACK: KeyCode = getattr(KeyCode, 'MEDIA_PREV_TRACK')
KEY_MEDIA_STOP: KeyCode = getattr(KeyCode, 'MEDIA_STOP')
KEY_MEDIA_PLAY_PAUSE: KeyCode = getattr(KeyCode, 'MEDIA_PLAY_PAUSE')
KEY_LAUNCH_MAIL: KeyCode = getattr(KeyCode, 'LAUNCH_MAIL')
KEY_LAUNCH_MEDIA_SELECT: KeyCode = getattr(KeyCode, 'LAUNCH_MEDIA_SELECT')
KEY_LAUNCH_APP1: KeyCode = getattr(KeyCode, 'LAUNCH_APP1')
KEY_LAUNCH_APP2: KeyCode = getattr(KeyCode, 'LAUNCH_APP2')
KEY_OEM_1: KeyCode = getattr(KeyCode, 'OEM_1')
KEY_OEM_PLUS: KeyCode = getattr(KeyCode, 'OEM_PLUS')
KEY_OEM_COMMA: KeyCode = getattr(KeyCode, 'OEM_COMMA')
KEY_OEM_MINUS: KeyCode = getattr(KeyCode, 'OEM_MINUS')
KEY_OEM_PERIOD: KeyCode = getattr(KeyCode, 'OEM_PERIOD')
KEY_OEM_2: KeyCode = getattr(KeyCode, 'OEM_2')
KEY_OEM_3: KeyCode = getattr(KeyCode, 'OEM_3')
KEY_OEM_4: KeyCode = getattr(KeyCode, 'OEM_4')
KEY_OEM_5: KeyCode = getattr(KeyCode, 'OEM_5')
KEY_OEM_6: KeyCode = getattr(KeyCode, 'OEM_6')
KEY_OEM_7: KeyCode = getattr(KeyCode, 'OEM_7')
KEY_OEM_8: KeyCode = getattr(KeyCode, 'OEM_8')
KEY_OEM_102: KeyCode = getattr(KeyCode, 'OEM_102')
KEY_PROCESSKEY: KeyCode = getattr(KeyCode, 'PROCESSKEY')
KEY_ATTN: KeyCode = getattr(KeyCode, 'ATTN')
KEY_CRSEL: KeyCode = getattr(KeyCode, 'CRSEL')
KEY_EXSEL: KeyCode = getattr(KeyCode, 'EXSEL')
KEY_EREOF: KeyCode = getattr(KeyCode, 'EREOF')
KEY_PLAY: KeyCode = getattr(KeyCode, 'PLAY')
KEY_ZOOM: KeyCode = getattr(KeyCode, 'ZOOM')
KEY_NONAME: KeyCode = getattr(KeyCode, 'NONAME')
KEY_PA1: KeyCode = getattr(KeyCode, 'PA1')
KEY_OEM_CLEAR: KeyCode = getattr(KeyCode, 'OEM_CLEAR')
KEYCOUNT: KeyCode = getattr(KeyCode, 'KEYCOUNT')
KEYPADDING: KeyCode = getattr(KeyCode, 'KEYPADDING')
KEY_MODIFIER_RELEASED: KeyCode = getattr(KeyCode, 'MODIFIER_RELEASED')
KEY_MODIFIER_RELEASED.__doc__ = \
    "or'd with a :class:`KeyCode` to indicate a key has been released."

#
# UTILITIES
# ---------


def new_buffer(data: bytes = None, size: int = None) -> buffer:
    """Allocate a new buffer to pass to dos-like functions that accept one.

    :param data: data to fill the buffer with, or use :obj:`None` and **size**
    :param size: if data is :obj:`None`, allocate a buffer of this size in
        bytes
    :return: new :class:`buffer`

    """
    if data is None and size is None:
        raise ValueError('data or size is required')
    if size is None and data is not None:
        size = len(data)
    return buffer(_dos.ffi.new(f'char[{size}]', data),
                  size if size is not None else -1)


def buffer_size(b: CData | ReadableBuffer | WriteableBuffer | Sized) -> int:
    """Get the size of a buffer.

    :param b: buffer to use
    :return: buffer size
    :raises ValueError: on unknown size

    """
    try:
        return len(typing.cast(Sized, b))
    except TypeError:
        # buffer type should really be the intersection of the Sized protocol
        # and the Buffer protocol, but the latter doesn't exist (PEP 688)
        raise ValueError('Buffer has unknown size')


def c_string(s: str | bytes | os.PathLike,
             encoding: str | dict[str, bytes] = 'utf-8') -> CData:
    """Convert a python string-like type to a C string.

    :param s: python string-like type
    :param encoding: encoding name (e.g. "utf-8") or a dict mapping characters
        to bytes
    :return: C string

    """
    if isinstance(s, bytes):
        encoded = s
    else:
        s = str(s)
        if isinstance(encoding, str):
            encoded = s.encode(encoding)
        else:
            encoded = b''.join(encoding[c] for c in s)
    return _dos.ffi.new('char[]', encoded)


def get_filename(path: bytes | str | os.PathLike | None) -> str | None:
    """Get the filename part of a path.

    :param path: string-like type containing a filesystem path
    :return: filename from that path, or :obj:`None` if the path was
        :obj:`None`

    """
    if path is None:
        return None
    if isinstance(path, bytes):
        path = path.decode('utf-8')
    if not isinstance(path, pathlib.Path):
        path = pathlib.Path(path)
    return path.name


#
# DOS-LIKE API
# ------------


def setvideomode(mode: VideoMode) -> None:
    """Set the video mode.

    :param mode: new video mode

    """
    _dos.lib.setvideomode(mode.value)


def setdoublebuffer(enabled: bool) -> None:
    """Enable or disable double buffer mode.

    :param enabled: new double buffer mode

    When enabled, updates to the screen buffer do not appear on screen until
    :func:`swapbuffers` is called.

    """
    _dos.lib.setdoublebuffer(enabled)


def screenwidth() -> int:
    """Get the current screen width.

    :return: width in characters (if text mode) or pixels (if graphics mode)

    """
    return _dos.lib.screenwidth()


def screenheight() -> int:
    """Get the current screen height.

    :return: height in characters (if text mode) or pixels (if graphics mode)

    """
    return _dos.lib.screenheight()


def screenbuffer() -> buffer:
    """Get the screen buffer.

    :return: screen buffer of pixels if graphics mode, or (character, color)
        pairs if text mode, in row-major order

    This will return the on-screen buffer in single buffer mode, or the
    off-screen buffer double buffer mode.

    Once :func:`swapbuffers` is called, this buffer will be displayed, and you
    will need to use its returned buffer as the new off-screen buffer.

    """
    return buffer(_dos.lib.screenbuffer(), SCREEN_BUFFER_SIZE)


def swapbuffers() -> buffer:
    """In double buffer mode, swap the off-screen buffer with the on-screen
    buffer.

    :return: the new off-screen buffer

    """
    return buffer(_dos.lib.swapbuffers(), SCREEN_BUFFER_SIZE)


def waitvbl() -> None:
    """Wait for the next vertical blanking interval (screen refresh)."""
    _dos.lib.waitvbl()


def setpal(
    index: int,
    r: RGB | tuple[int, int, int] | int,
    g: int = None,
    b: int = None,
) -> None:
    """Set a palette entry.

    May be called with a single :class:`RGB` or 3-``tuple`` argument, or 3
    ``int`` arguments.

    :param index: palette index to update, 0..255
    :param r: new :class:`RGB` or 3-``tuple`` color, or the red component in
        0..63
    :param g: green component in 0..63
    :param b: blue component in 0..63

    """
    if not isinstance(r, int) and (g is not None or b is not None):
        raise ValueError('Either pass in a single RGB argument, or 3 channels')
    if isinstance(r, tuple):
        if len(r) != 3:
            raise ValueError(
                'A 3-tuple is required if passing a single RGB value')
        r, g, b = r
    if g is None or b is None:
        raise ValueError('All color channels must be specified')
    _dos.lib.setpal(index, r, g, b)


def getpal(index: int) -> RGB:
    """Get a palette entry.

    :param index: palette index in 0..255
    :return: color at that index

    """
    result = _dos.ffi.new('int[3]')
    _dos.lib.getpal(index, result + 0, result + 1, result + 2)
    return RGB(result[0], result[1], result[2])


def shuttingdown() -> bool:
    """Check if the user has requested to quit by closing the window.

    :return: True if the app window is closing

    This should be checked periodically. When it returns True, the main
    function should return.

    """
    return bool(_dos.lib.shuttingdown())


def cputs(string: bytes | str | os.PathLike) -> None:
    """Display text and advance the cursor (text mode only).

    :param string: text to put to the screen

    If the text would extend beyond the current line, it will be truncated and
    the cursor will remain at the end of the line.

    In graphics mode, see :func:`outtextxy`, :func:`wraptextxy`, and
    :func:`centertextxy`.

    """
    _dos.lib.cputs(c_string(string, encoding=cp437.ENCODING))


def textcolor(color: int) -> None:
    """Change the text color (text mode only).

    :param color: text palette index in 0..15

    """
    _dos.lib.textcolor(color)


def textbackground(color: int) -> None:
    """Change the text background color (text mode only).

    :param color: background palette index in 0..15

    """
    _dos.lib.textbackground(color)


def gotoxy(x: int, y: int) -> None:
    """Set the cursor position (text mode only).

    :param x: cursor 𝑥 position, starting at 0
    :param y: cursor 𝑦 position, starting at 0

    """
    _dos.lib.gotoxy(x, y)


def wherex() -> int:
    """Return the current cursor 𝑥 position.

    :return: cursor 𝑥 position

    """
    return _dos.lib.wherex()


def wherey() -> int:
    """Return the current cursor 𝑦 position.

    :return: cursor 𝑦 position

    """
    return _dos.lib.wherey()


def clrscr() -> None:
    """Clear the screen (text mode only).

    Fill the screen with the space character (``b'\\x20'``) with the current
    text and background color.

    For graphics mode, see :func:`clearscreen`.

    """
    _dos.lib.clrscr()


def curson() -> None:
    """Show the text mode cursor."""
    _dos.lib.curson()


def cursoff() -> None:
    """Hide the text mode cursor."""
    _dos.lib.cursoff()


def loadgif(filename: bytes | str | os.PathLike) -> GIF:
    """Load a GIF image.

    :param filename: path to the GIF file
    :return: :class:`GIF` image
    :raises ValueError: if unable to load image

    """
    width_ptr = _dos.ffi.new('int *')
    height_ptr = _dos.ffi.new('int *')
    palcount_ptr = _dos.ffi.new('int *')
    palette = _dos.ffi.new('unsigned char[768]')
    pixels = _dos.lib.loadgif(c_string(filename), width_ptr, height_ptr,
                              palcount_ptr, palette)

    if pixels == _dos.ffi.NULL:
        raise ValueError(f'Unable to load GIF {filename!r}')
    width = width_ptr[0]
    height = height_ptr[0]
    palcount = palcount_ptr[0]

    rgb_palette = [
        RGB(palette[3 * i], palette[3 * i + 1], palette[3 * i + 2])
        for i in range(palcount)
    ]
    pixelbuf = buffer(pixels, width * height)

    # get_filename won't return None if filename isn't None
    name = typing.cast(str, get_filename(filename))
    return GIF(name, width, height, rgb_palette, pixelbuf, pixels)


def blit(
    x: int,
    y: int,
    source: ReadableBuffer,
    width: int,
    height: int,
    srcx: int,
    srcy: int,
    srcw: int,
    srch: int,
) -> None:
    """Copy an image buffer to the screen.

    :param x: destination 𝑥 position
    :param y: destination 𝑦 position
    :param source: source image buffer, e.g. :attr:`GIF.pixels`
    :param width: source image width
    :param height: source image height
    :param srcx: source 𝑥 position in the image
    :param srcy: source 𝑦 position in the image
    :param srcw: width to copy
    :param srch: height to copy

    """
    _dos.lib.blit(x, y, _dos.ffi.from_buffer(source), width, height, srcx,
                  srcy, srcw, srch)


def maskblit(
    x: int,
    y: int,
    source: ReadableBuffer,
    width: int,
    height: int,
    srcx: int,
    srcy: int,
    srcw: int,
    srch: int,
    colorkey: int,
) -> None:
    """Copy an image buffer to the screen using 1 color as transparent.

    :param x: destination 𝑥 position
    :param y: destination 𝑦 position
    :param source: source image buffer, e.g. :attr:`GIF.pixels`
    :param width: source image width
    :param height: source image height
    :param srcx: source 𝑥 position in the image
    :param srcy: source 𝑦 position in the image
    :param srcw: width to copy
    :param srch: height to copy
    :param colorkey: palette index to use as transparent

    """
    _dos.lib.maskblit(x, y, _dos.ffi.from_buffer(source), width, height, srcx,
                      srcy, srcw, srch, colorkey)


def clearscreen() -> None:
    """Fill the screen buffer with 0s."""
    _dos.lib.clearscreen()


def getpixel(x: int, y: int) -> int:
    """Return the pixel value at this position

    :param x: screen 𝑥 position
    :param y: screen 𝑦 position
    :return: pixel value

    """
    return _dos.lib.getpixel(x, y)


def hline(x: int, y: int, len: int, color: int) -> None:
    """Draw a horizontal line from left to right.

    :param x: starting 𝑥 position
    :param y: starting 𝑦 position
    :param len: total length in pixels
    :param color: palette index

    """
    _dos.lib.hline(x, y, len, color)


def putpixel(x: int, y: int, color: int) -> None:
    """Set the pixel value at this position.

    :param x: screen 𝑥 position
    :param y: screen 𝑦 position
    :param color: palette index

    """
    _dos.lib.putpixel(x, y, color)


def setdrawtarget(pixels: WriteableBuffer, width: int, height: int) -> None:
    """Start drawing to an off-screen buffer.

    :param pixels: pixel buffer to draw to
    :param width: width of the pixel buffer
    :param height: height of the pixel buffer

    Future draw calls will update **pixels** instead of the screen buffer.  To
    resume drawing to the screen, call :func:`resetdrawtarget`.

    """
    global _current_draw_target
    size = width * height
    if buffer_size(pixels) < size:
        raise ValueError(f'pixel buffer must be at least {size} bytes')
    _dos.lib.setdrawtarget(_dos.ffi.from_buffer(pixels), width, height)
    # Retain the draw target to prevent it from being garbage collected
    _current_draw_target = pixels


def resetdrawtarget() -> None:
    """Start drawing to the screen buffer.

    Call this to stop drawing to the off-screen buffer set by
    :func:`setdrawtarget`.

    """
    global _current_draw_target
    _dos.lib.resetdrawtarget()
    _current_draw_target = None


def setcolor(color: int) -> None:
    """Set the palette index for drawing functions that don't take a color
    (e.g. :func:`circle`).

    :param color: palette index

    """
    _dos.lib.setcolor(color)


def getcolor() -> int:
    """Get the palette index set by :func:`setcolor`.

    :return: palette index

    """
    return _dos.lib.getcolor()


def line(x1: int, y1: int, x2: int, y2: int) -> None:
    """Draw a line between two points.

    :param x1: 𝑥 position of point 1
    :param y1: 𝑦 position of point 1
    :param x2: 𝑥 position of point 2
    :param y2: 𝑦 position of point 2

    The palette index set by :func:`setcolor` will be used.

    """
    _dos.lib.line(x1, y1, x2, y2)


def rectangle(x: int, y: int, w: int, h: int) -> None:
    """Draw a rectangle outline.

    :param x: 𝑥 position of the top-left corner
    :param y: 𝑦 position of the top-left corner
    :param w: rectangle width
    :param h: rectangle height

    The palette index set by :func:`setcolor` will be used.

    """
    _dos.lib.rectangle(x, y, w, h)


def bar(x: int, y: int, w: int, h: int) -> None:
    """Draw a filled rectangle.

    :param x: 𝑥 position of the top-left corner
    :param y: 𝑦 position of the top-left corner
    :param w: rectangle width
    :param h: rectangle height

    The palette index set by :func:`setcolor` will be used.

    """
    _dos.lib.bar(x, y, w, h)


def circle(x: int, y: int, r: int) -> None:
    """Draw a circle outline.

    :param x: 𝑥 position of the circle's center
    :param y: 𝑦 position of the circle's center
    :param r: circle radius

    The palette index set by :func:`setcolor` will be used.

    """
    _dos.lib.circle(x, y, r)


def fillcircle(x: int, y: int, r: int) -> None:
    """Draw a filled circle.

    :param x: 𝑥 position of the circle's center
    :param y: 𝑦 position of the circle's center
    :param r: circle radius

    The palette index set by :func:`setcolor` will be used.

    """
    _dos.lib.fillcircle(x, y, r)


def ellipse(x: int, y: int, rx: int, ry: int) -> None:
    """Draw an ellipse outline.

    :param x: 𝑥 position of the ellipse's center
    :param y: 𝑦 position of the ellipse's center
    :param rx: 𝑥 radius
    :param ry: 𝑦 radius

    The palette index set by :func:`setcolor` will be used.

    """
    _dos.lib.ellipse(x, y, rx, ry)


def fillellipse(x: int, y: int, rx: int, ry: int) -> None:
    """Draw a filled ellipse.

    :param x: 𝑥 position of the ellipse's center
    :param y: 𝑦 position of the ellipse's center
    :param rx: 𝑥 radius
    :param ry: 𝑦 radius

    The palette index set by :func:`setcolor` will be used.

    """
    _dos.lib.fillellipse(x, y, rx, ry)


def drawpoly(points_xy: Points) -> None:
    """Draw a polygon outline.

    :param points_xy: The points to draw, in one of these formats:

        * a list of 𝑥, 𝑦 tuples: ``[(x1, y1), (x2, y2), ...]``
        * a flattened list of points: ``[x1, y1, x2, y2, ...]``
        * an ``int[]`` buffer

    The palette index set by :func:`setcolor` will be used.

    """
    points_data = _data_for_points(points_xy)
    count = buffer_size(points_data) // 2
    _dos.lib.drawpoly(points_data, count)


def fillpoly(points_xy: Points) -> None:
    """Draw a filled polygon.

    :param points_xy: The points to draw, in one of these formats:

        * a list of 𝑥, 𝑦 tuples: ``[(x1, y1), (x2, y2), ...]``
        * a flattened list of points: ``[x1, y1, x2, y2, ...]``
        * an ``int[]`` buffer

    The palette index set by :func:`setcolor` will be used.

    """
    points_data = _data_for_points(points_xy)
    count = buffer_size(points_data) // 2
    _dos.lib.fillpoly(points_data, count)


def floodfill(x: int, y: int) -> None:
    """Flood fill starting at this point.

    :param x: 𝑥 position of the start point
    :param y: 𝑦 position of the start point

    Fill out from the start point, setting all pixels with a color index
    matching the original color of the start point.

    The palette index set by :func:`setcolor` will be used.

    """
    _dos.lib.floodfill(x, y)


def boundaryfill(x: int, y: int, boundary: int) -> None:
    """Boundary fill starting at this point.

    :param x: 𝑥 position of the start point
    :param y: 𝑦 position of the start point
    :param boundary: boundary color index

    Fill out from the start point, setting all pixels with a color index
    not matching the boundary color.

    The palette index set by :func:`setcolor` will be used.

    """
    _dos.lib.boundaryfill(x, y, boundary)


def outtextxy(x: int, y: int, text: bytes | str | os.PathLike) -> None:
    """Draw graphics mode text.

    :param x: 𝑥 position of the start point
    :param y: 𝑦 position of the start point
    :param text: text to draw

    The font set by :func:`settextstyle` will be used.

    For text mode, see :func:`cputs`.

    """
    _dos.lib.outtextxy(x, y, c_string(text, encoding=cp437.ENCODING))


def wraptextxy(x: int, y: int, text: bytes | str | os.PathLike,
               width: int) -> None:
    """Draw graphics mode text with word wrap.

    :param x: 𝑥 position of the start point
    :param y: 𝑦 position of the start point
    :param text: text to draw
    :param width: wrap to the next line beyond this width

    The font set by :func:`settextstyle` will be used.

    For text mode, see :func:`cputs`.

    """
    _dos.lib.wraptextxy(x, y, c_string(text, encoding=cp437.ENCODING), width)


def centertextxy(x: int, y: int, text: bytes | str | os.PathLike,
                 width: int) -> None:
    """Draw graphics mode text centered between a start point and width.

    :param x: 𝑥 position of the start point
    :param y: 𝑦 position of the start point
    :param text: text to draw
    :param width: centering end point (between 𝑥 and 𝑥 + **width**)

    The font set by :func:`settextstyle` will be used.

    For text mode, see :func:`cputs`.

    """
    _dos.lib.centertextxy(x, y, c_string(text, encoding=cp437.ENCODING), width)


def settextstyle(font: FontHandle,
                 bold: bool = False,
                 italic: bool = False,
                 underline: bool = False) -> None:
    """Set the graphics mode text style.

    :param font: font to draw with
    :param bold: enable **bold**
    :param italic: enable *italics*
    :param underline: enable :underline:`underline`

    This will affect the next calls to :func:`outtextxy`, :func:`wraptextxy`,
    and :func:`centertextxy`.

    """
    _dos.lib.settextstyle(font, bold, italic, underline)


def installuserfont(filename: bytes | str | os.PathLike) -> FontHandle:
    """Install a font generated by the pixelfont library used by dos-like.

    :param filename: filesystem path of the font to load
    :return: handle to the installed font
    :raises ValueError: if unable to load the font

    """
    result: int = _dos.lib.installuserfont(c_string(filename))
    if result == 0:
        raise ValueError(f'Failed to load font {filename!r}')
    return FontHandle(result)


def setsoundbank(soundbank: SoundBankHandle) -> None:
    """Set the current sound bank.

    :param soundbank: handle to an installed sound bank

    The sound bank will be used by music functions like :func:`noteon` and
    :func:`playmusic`.

    """
    _dos.lib.setsoundbank(soundbank)


def installusersoundbank(
        filename: bytes | str | os.PathLike) -> SoundBankHandle:
    """Install a sound bank.

    :param filename: filesystem path to a SoundFont (.sf2) or OP2 bank (.op2)
    :return: handle to the new sound bank
    :raises ValueError: if unable to load the sound bank

    """
    result: int = _dos.lib.installuserfont(c_string(filename))
    if result == 0:
        raise ValueError(f'Failed to load soundbank {filename!r}')
    return SoundBankHandle(result)


def noteon(channel: int, note: int, velocity: int) -> None:
    """Play a note on a music channel.

    :param channel: music channel number from 0 up to but not including
        :data:`MUSIC_CHANNELS`
    :param note: MIDI note number in 0..127
    :param velocity: note velocity in 0..127

    If invalid parameters are given, the function call will be ignored.

    For a chart of MIDI note numbers, see
    http://www.phys.unsw.edu.au/jw/notes.html

    """
    _dos.lib.noteon(channel, note, velocity)


def noteoff(channel: int, note: int) -> None:
    """Stop playing a note on a music channel.

    :param channel: music channel number from 0 up to but not including
        :data:`MUSIC_CHANNELS`
    :param note: MIDI note number in 0..127

    If invalid parameters are given, the function call will be ignored.

    For a chart of MIDI note numbers, see
    http://www.phys.unsw.edu.au/jw/notes.html

    """
    _dos.lib.noteoff(channel, note)


def allnotesoff(channel: int) -> None:
    """Stop playing all notes on a music channel.

    :param channel: music channel number from 0 up to but not including
        :data:`MUSIC_CHANNELS`

    """
    _dos.lib.allnotesoff(channel)


def setinstrument(channel: int, instrument: int) -> None:
    """Set the instrument number for a music channel.

    :param channel: music channel number from 0 up to but not including
        :data:`MUSIC_CHANNELS`
    :param instrument: instrument number in 0..127

    """
    _dos.lib.setinstrument(channel, instrument)


def loadmid(filename: bytes | str | os.PathLike) -> Music:
    """Load music from a MIDI (.mid) file.

    :param filename: filesystem path of the MIDI to load
    :return: loaded MIDI music
    :raises ValueError: if unable to load the music file

    """
    result = _dos.lib.loadmid(c_string(filename))
    if result == _dos.ffi.NULL:
        raise ValueError(f'Failed to load music {filename!r}')
    return Music(get_filename(filename), result)


def loadmus(filename: bytes | str | os.PathLike) -> Music:
    """Load music from a
    `MUS <https://moddingwiki.shikadi.net/wiki/MUS_Format>`_ (.mus) file.

    :param filename: filesystem path of the MUS to load
    :return: loaded MUS music
    :raises ValueError: if unable to load the music file

    """
    result = _dos.lib.loadmus(c_string(filename))
    if result == _dos.ffi.NULL:
        raise ValueError(f'Failed to load music {filename!r}')
    return Music(get_filename(filename), result)


def loadmod(filename: bytes | str | os.PathLike) -> Music:
    """Load music from a
    `module <https://en.wikipedia.org/wiki/MOD_(file_format)>`_ (.mod) file.

    :param filename: filesystem path of the MOD to load
    :return: loaded MOD music
    :raises ValueError: if unable to load the music file

    """
    result = _dos.lib.loadmod(c_string(filename))
    if result == _dos.ffi.NULL:
        raise ValueError(f'Failed to load music {filename!r}')
    return Music(get_filename(filename), result)


def loadopb(filename: bytes | str | os.PathLike) -> Music:
    """Load music from an
    `OPBinaryLib <https://github.com/Enichan/OPBinaryLib>`_ (.opb) file.

    :param filename: filesystem path of the OPB to load
    :return: loaded OPB music
    :raises ValueError: if unable to load the music file

    """
    result = _dos.lib.loadopb(c_string(filename))
    if result == _dos.ffi.NULL:
        raise ValueError(f'Failed to load music {filename!r}')
    return Music(get_filename(filename), result)


def createmus(data: ReadableBuffer | bytes) -> Music:
    """Load music from an in-memory
     `MUS <https://moddingwiki.shikadi.net/wiki/MUS_Format>`_ (.mus) buffer.

    :param data: buffer or byte string containing the MUS data
    :return: loaded MUS music
    :raises ValueError: if unable to load the music data

    """
    c_data = _dos.ffi.from_buffer(data)
    result = _dos.lib.createmus(c_data, buffer_size(data))
    if result == _dos.ffi.NULL:
        raise ValueError
    return Music(filename=None, _music_ptr=result)


def playmusic(music: Music, loop: bool = False, volume: int = 255) -> None:
    """Start playing music.

    :param music: music to play
    :param loop: whether the music should loop
    :param volume: volume level in 0..255

    The music may be stopped with :func:`stopmusic`.

    """
    global _current_music
    _dos.lib.playmusic(music._music_ptr, loop, volume)
    # Prevent current music from being garbage collected
    _current_music = music


def stopmusic() -> None:
    """Stop playing music that was started by :func:`playmusic`."""
    global _current_music
    _dos.lib.stopmusic()
    _current_music = None


def musicplaying() -> bool:
    """Check if music is currently playing.

    :return: :obj:`True` if music is playing, :obj:`False` otherwise

    Music playback can be controlled with :func:`playmusic` and
    :func:`stopmusic`.

    """
    return bool(_dos.lib.musicplaying())


def musicvolume(volume: int) -> None:
    """Set the music playback volume.

    :param volume: volume level in 0..255

    """
    _dos.lib.musicvolume(volume)


def setsoundmode(mode: SoundMode) -> None:
    """Set the sound playback mode.

    :param mode: new sound mode

    """
    _dos.lib.setsoundmode(mode.value)


def loadwav(filename: bytes | str | os.PathLike) -> Sound:
    """Load a .wav sound file.

    :param filename: filesystem path of the WAV to load
    :return: new sound
    :raises ValueError: if unable to load the sound

    .. warning::

        Sound memory is freed when the returned :class:`Sound` object is
        garbage collected.  Deleting or releasing the last reference to a
        playing sound may cause issues.

    """
    result = _dos.lib.loadwav(c_string(filename))
    if result == _dos.ffi.NULL:
        raise ValueError(f'Unable to load sound {filename!r}')
    return Sound(get_filename(filename), result)


def createsound(channels: int, samplerate: int, samples: Samples) -> Sound:
    """Create a sound from a sample buffer.

    :param channels: 1 for mono, 2 for stereo
    :param samplerate: sample playback rate in 1000..44,100 Hz
    :param samples: sample buffer in one of these formats:

        * a list of integers in -32,768..32,767
        * a ``short[]`` buffer

    :return: new sound
    :raises ValueError: for invalid parameters

    .. warning::

        Sound memory is freed when the returned :class:`Sound` object is
        garbage collected.  Deleting or releasing the last reference to a
        playing sound may cause issues.

    """
    data, size = _data_for_samples(samples)
    framecount = size // channels // 2  # 2 bytes per sample
    result = _dos.lib.createsound(channels, samplerate, framecount, data)
    if result == _dos.ffi.NULL:
        raise ValueError('Invalid parameters')
    return Sound(None, result)


def playsound(channel: int,
              sound: Sound,
              loop: bool = False,
              volume: int = 255) -> None:
    """Play a sound.

    :param channel: sound channel number from 0 up to but not including
        :data:`SOUND_CHANNELS`
    :param sound: sound to play
    :param loop: whether the sound should loop
    :param volume: volume level in 0..255

    Sounds may be loaded with :func:`loadwav` or created from a buffer with
    :func:`createsound`.

    The sound may be stopped with :func:`stopsound`.

    """
    _dos.lib.playsound(channel, sound._sound_ptr, loop, volume)


def stopsound(channel: int) -> None:
    """Stop the sound playing on a channel.

    :param channel: sound channel number from 0 up to but not including
        :data:`SOUND_CHANNELS`

    This will stop a sound that was played by :func:`playsound`.

    """
    _dos.lib.stopsound(channel)


def soundplaying(channel: int) -> bool:
    """Check if sound is playing on a channel.

    :param channel: sound channel number from 0 up to but not including
        :data:`SOUND_CHANNELS`
    :return: :obj:`True` if sound is playing, :obj:`False` otherwise

    Sound can be played with :func:`playsound` and stopped with
    :func:`stopsound`.

    """
    return bool(_dos.lib.soundplaying(channel))


def soundvolume(channel: int, left: int, right: int) -> None:
    """Set the sound volume for a channel.

    :param channel: sound channel number from 0 up to but not including
        :data:`SOUND_CHANNELS`
    :param left: left volume level in 0..255
    :param right: right volume level in 0..255

    """
    _dos.lib.soundvolume(channel, left, right)


def keystate(key: KeyCode) -> bool:
    """Check if a key is pressed, by code.

    :param key: key code to check
    :return: :obj:`True` if pressed, :obj:`False` otherwise

    """
    return bool(_dos.lib.keystate(key.value))


def readkeys() -> list[KeyCode]:
    """Get the key codes received since the last call to :func:`readkeys`.

    :return: list of :class:`KeyCode` values, may be empty if no keys were
        pressed or released since the last call.

    The returned key codes may be bitwise or'd with
    :data:`KEY_MODIFIER_RELEASED` to indicate a key has been released.
    Otherwise, indicates a key has been pressed.

    """
    result: list[KeyCode] = []
    keycodes = _dos.lib.readkeys()
    while keycodes[0] != KEY_INVALID.value:
        result.append(KeyCode(keycodes[0]))
        keycodes += 1
    return result


def readchars() -> str:
    """Get the characters typed since the last call to :func:`readchars`.

    :return: string of characters, may be empty if no characters were typed
        since the last call.

    """
    chars = _dos.lib.readchars()
    return _dos.ffi.string(chars).decode('cp437')


def mousex() -> int:
    """Get the current mouse 𝑥 position.

    :return: mouse 𝑥 position

    """
    return _dos.lib.mousex()


def mousey() -> int:
    """Get the current mouse 𝑦 position.

    :return: mouse 𝑦 position

    """
    return _dos.lib.mousey()


def mouserelx() -> int:
    """Get the last relative mouse 𝑥 direction.

    :return: mouse movement in the 𝑥 direction relative to the position of the
        last mouse input event, may be positive or negative

    """
    return _dos.lib.mouserelx()


def mouserely() -> int:
    """Get the last relative mouse 𝑦 direction.

    :return: mouse movement in the 𝑦 direction relative to the position of the
        last mouse input event, may be positive or negative

    """
    return _dos.lib.mouserely()
