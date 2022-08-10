from __future__ import annotations

import collections
import dataclasses
import enum
import os
import pathlib
from typing import Union

try:
    from typing import TypeAlias
except ImportError:
    from typing_extensions import TypeAlias

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
    'Points',
    'RGB',
    'SOUND_CHANNELS',
    'SoundBankHandle',
    'VideoMode',
    'allnotesoff',
    'bar',
    'blit',
    'boundaryfill',
    'buffer',
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
SCREEN_BUFFER_SIZE = 640 * 480

MUSIC_CHANNELS = _dos.lib.MUSIC_CHANNELS
SOUND_CHANNELS = _dos.lib.SOUND_CHANNELS

# The buffer protocol cannot be referenced by python code,
# so expose cffi's concrete buffer (see PEP 688)
buffer = _dos.ffi.buffer

RGB = collections.namedtuple('RGB', 'r g b')

Points: TypeAlias = Union[buffer, list[int], list[tuple[int, int]]]


def _data_for_points(points: Points) -> _dos.ffi.CData:
    """Return a CFFI data object for an array of ints representing 2D points.

    :param points: a buffer of ints, a list of ints, or a list of (x, y) tuples

    """
    if isinstance(points, buffer):
        return _dos.ffi.from_buffer('int[]', points)
    if len(points) < 2:
        raise ValueError('At least two points are required')
    if isinstance(points[0], tuple):
        points: list[tuple[int, int]]
        xy: list[int] = []
        for point in points:
            xy.extend(point)
    else:
        xy = points
    return _dos.ffi.new('int[]', xy)


Samples: TypeAlias = Union[buffer, list[int]]


def _data_for_samples(samples: Samples) -> tuple[_dos.ffi.CData, int]:
    """Return CFFI data for an array of shorts representing audio samples.

    :param samples: a buffer of shorts, or a list of ints
    :return: a tuple of the sound data, and its size in bytes.  The __len__ of
        the return value is not useful, since it may return the size in bytes
        *or* in words

    """
    if isinstance(samples, buffer):
        result = _dos.ffi.from_buffer('short[]', samples)
        return result, len(samples)
    result = _dos.ffi.new('short[]', samples)
    return result, len(result) * 2


@dataclasses.dataclass
class GIF:
    filename: str
    width: int
    height: int
    palette: list[RGB]
    pixels: buffer
    # TODO: handle pixels lifecycle


VideoMode = enum.Enum(
    'VideoMode', {
        k.removeprefix('videomode_'): v
        for k, v in _dos.lib.__dict__.items() if k.startswith('videomode_')
    })
videomode_40x25_8x8: VideoMode = getattr(VideoMode, '40x25_8x8')
videomode_40x25_9x16: VideoMode = getattr(VideoMode, '40x25_9x16')
videomode_80x25_8x16: VideoMode = getattr(VideoMode, '80x25_8x16')
videomode_80x25_8x8: VideoMode = getattr(VideoMode, '80x25_8x8')
videomode_80x25_9x16: VideoMode = getattr(VideoMode, '80x25_9x16')
videomode_80x43_8x8: VideoMode = getattr(VideoMode, '80x43_8x8')
videomode_80x50_8x8: VideoMode = getattr(VideoMode, '80x50_8x8')
videomode_320x200: VideoMode = getattr(VideoMode, '320x200')
videomode_320x240: VideoMode = getattr(VideoMode, '320x240')
videomode_320x400: VideoMode = getattr(VideoMode, '320x400')
videomode_640x200: VideoMode = getattr(VideoMode, '640x200')
videomode_640x350: VideoMode = getattr(VideoMode, '640x350')
videomode_640x400: VideoMode = getattr(VideoMode, '640x400')
videomode_640x480: VideoMode = getattr(VideoMode, '640x480')


class FontHandle(int):
    pass


DEFAULT_FONT_8X8: FontHandle = FontHandle(_dos.lib.DEFAULT_FONT_8X8)
DEFAULT_FONT_8X16: FontHandle = FontHandle(_dos.lib.DEFAULT_FONT_8X16)
DEFAULT_FONT_9X16: FontHandle = FontHandle(_dos.lib.DEFAULT_FONT_9X16)


class SoundBankHandle(int):
    pass


DEFAULT_SOUNDBANK_AWE32: SoundBankHandle = SoundBankHandle(
    _dos.lib.DEFAULT_SOUNDBANK_AWE32)
DEFAULT_SOUNDBANK_SB16: SoundBankHandle = SoundBankHandle(
    _dos.lib.DEFAULT_SOUNDBANK_SB16)


class Music:

    def __init__(self,
                 music_ptr: _dos.ffi.CData,
                 path: bytes | str | os.PathLike = None):
        # TODO: handle music lifecycle
        self._music_ptr = music_ptr
        self.filename: str = get_filename(path)


SoundMode = enum.Enum(
    'SoundMode', {
        k.removeprefix('soundmode_'): v
        for k, v in _dos.lib.__dict__.items() if k.startswith('soundmode_')
    })
soundmode_8bit_mono_5000: SoundMode = getattr(SoundMode, '8bit_mono_5000')
soundmode_8bit_mono_8000: SoundMode = getattr(SoundMode, '8bit_mono_8000')
soundmode_8bit_mono_11025: SoundMode = getattr(SoundMode, '8bit_mono_11025')
soundmode_8bit_mono_16000: SoundMode = getattr(SoundMode, '8bit_mono_16000')
soundmode_8bit_mono_22050: SoundMode = getattr(SoundMode, '8bit_mono_22050')
soundmode_8bit_mono_32000: SoundMode = getattr(SoundMode, '8bit_mono_32000')
soundmode_8bit_mono_44100: SoundMode = getattr(SoundMode, '8bit_mono_44100')
soundmode_16bit_mono_5000: SoundMode = getattr(SoundMode, '16bit_mono_5000')
soundmode_16bit_mono_8000: SoundMode = getattr(SoundMode, '16bit_mono_8000')
soundmode_16bit_mono_11025: SoundMode = getattr(SoundMode, '16bit_mono_11025')
soundmode_16bit_mono_16000: SoundMode = getattr(SoundMode, '16bit_mono_16000')
soundmode_16bit_mono_22050: SoundMode = getattr(SoundMode, '16bit_mono_22050')
soundmode_16bit_mono_32000: SoundMode = getattr(SoundMode, '16bit_mono_32000')
soundmode_16bit_mono_44100: SoundMode = getattr(SoundMode, '16bit_mono_44100')
soundmode_8bit_stereo_5000: SoundMode = getattr(SoundMode, '8bit_stereo_5000')
soundmode_8bit_stereo_8000: SoundMode = getattr(SoundMode, '8bit_stereo_8000')
soundmode_8bit_stereo_11025: SoundMode = getattr(SoundMode,
                                                 '8bit_stereo_11025')
soundmode_8bit_stereo_16000: SoundMode = getattr(SoundMode,
                                                 '8bit_stereo_16000')
soundmode_8bit_stereo_22050: SoundMode = getattr(SoundMode,
                                                 '8bit_stereo_22050')
soundmode_8bit_stereo_32000: SoundMode = getattr(SoundMode,
                                                 '8bit_stereo_32000')
soundmode_8bit_stereo_44100: SoundMode = getattr(SoundMode,
                                                 '8bit_stereo_44100')
soundmode_16bit_stereo_5000: SoundMode = getattr(SoundMode,
                                                 '16bit_stereo_5000')
soundmode_16bit_stereo_8000: SoundMode = getattr(SoundMode,
                                                 '16bit_stereo_8000')
soundmode_16bit_stereo_11025: SoundMode = getattr(SoundMode,
                                                  '16bit_stereo_11025')
soundmode_16bit_stereo_16000: SoundMode = getattr(SoundMode,
                                                  '16bit_stereo_16000')
soundmode_16bit_stereo_22050: SoundMode = getattr(SoundMode,
                                                  '16bit_stereo_22050')
soundmode_16bit_stereo_32000: SoundMode = getattr(SoundMode,
                                                  '16bit_stereo_32000')
soundmode_16bit_stereo_44100: SoundMode = getattr(SoundMode,
                                                  '16bit_stereo_44100')


class Sound:

    def __init__(self,
                 sound_ptr: _dos.ffi.CData,
                 path: bytes | str | os.PathLike = None):
        # TODO: handle sound lifecycle
        self._sound_ptr = sound_ptr
        self.filename = get_filename(path)


KeyCode = int_with_flags.IntWithFlags(
    'KeyCode', {
        k.removeprefix('KEY_'): v
        for k, v in _dos.lib.__dict__.items() if k.startswith('KEY')
    })
KeyCode._flags_ = {'KEY_MODIFIER_RELEASED': _dos.lib.KEY_MODIFIER_RELEASED}

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

#
# UTILITIES
# ---------


def new_buffer(data: bytes = None, size: int = None) -> buffer:
    if data is None and size is None:
        raise ValueError('data or size is required')
    if size is None:
        size = len(data)
    return _dos.ffi.buffer(_dos.ffi.new(f'char[{size}]', data), size)


def c_string(s: str | bytes | os.PathLike,
             encoding: str | dict[str, bytes] = 'utf-8') -> _dos.lib.CData:
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
    if path is None:
        return None
    if isinstance(path, bytes):
        path = path.decode('utf-8')
    if isinstance(path, str):
        path = pathlib.Path(path)
    return path.name


#
# DOS-LIKE API
# ------------


def setvideomode(mode: VideoMode) -> None:
    _dos.lib.setvideomode(mode.value)


def setdoublebuffer(enabled: bool) -> None:
    _dos.lib.setdoublebuffer(enabled)


def screenwidth() -> int:
    return _dos.lib.screenwidth()


def screenheight() -> int:
    return _dos.lib.screenheight()


def screenbuffer() -> buffer:
    return _dos.ffi.buffer(_dos.lib.screenbuffer(), SCREEN_BUFFER_SIZE)


def swapbuffers() -> buffer:
    return _dos.ffi.buffer(_dos.lib.swapbuffers(), SCREEN_BUFFER_SIZE)


def waitvbl() -> None:
    _dos.lib.waitvbl()


def setpal(
    index: int,
    r: RGB | tuple | int,
    g: int = None,
    b: int = None,
) -> None:
    if not isinstance(r, int) and (g is not None or b is not None):
        raise ValueError('Either pass in a single RGB argument, or 3 channels')
    if isinstance(r, tuple):
        if len(r) != 3:
            raise ValueError(
                'A 3-tuple is required if passing a single RGB value')
        r, g, b = r
    _dos.lib.setpal(index, r, g, b)


def getpal(index: int) -> RGB:
    result = _dos.ffi.new('int[3]')
    _dos.lib.getpal(index, result + 0, result + 1, result + 2)
    return RGB(result[0], result[1], result[2])


def shuttingdown() -> bool:
    return bool(_dos.lib.shuttingdown())


def cputs(string: bytes | str | os.PathLike) -> None:
    _dos.lib.cputs(c_string(string, encoding=cp437.ENCODING))


def textcolor(color: int) -> None:
    _dos.lib.textcolor(color)


def textbackground(color: int) -> None:
    _dos.lib.textbackground(color)


def gotoxy(x: int, y: int) -> None:
    _dos.lib.gotoxy(x, y)


def wherex() -> int:
    return _dos.lib.wherex()


def wherey() -> int:
    return _dos.lib.wherey()


def clrscr() -> None:
    _dos.lib.clrscr()


def curson() -> None:
    _dos.lib.curson()


def cursoff() -> None:
    _dos.lib.cursoff()


def loadgif(filename: bytes | str | os.PathLike) -> GIF | None:
    width_ptr = _dos.ffi.new('int *')
    height_ptr = _dos.ffi.new('int *')
    palcount_ptr = _dos.ffi.new('int *')
    palette = _dos.ffi.new('unsigned char[768]')
    pixels = _dos.lib.loadgif(c_string(filename), width_ptr, height_ptr,
                              palcount_ptr, palette)

    if pixels == _dos.ffi.NULL:
        return None
    width = width_ptr[0]
    height = height_ptr[0]
    palcount = palcount_ptr[0]

    rgb_palette = [
        RGB(palette[3 * i], palette[3 * i + 1], palette[3 * i + 2])
        for i in range(palcount)
    ]
    pixelbuf = _dos.ffi.buffer(pixels, width * height)
    return GIF(get_filename(filename), width, height, rgb_palette, pixelbuf)


def blit(
    x: int,
    y: int,
    source: buffer,
    width: int,
    height: int,
    srcx: int,
    srcy: int,
    srcw: int,
    srch: int,
) -> None:
    _dos.lib.blit(x, y, _dos.ffi.from_buffer(source), width, height, srcx,
                  srcy, srcw, srch)


def maskblit(
    x: int,
    y: int,
    source: buffer,
    width: int,
    height: int,
    srcx: int,
    srcy: int,
    srcw: int,
    srch: int,
    colorkey: int,
) -> None:
    _dos.lib.maskblit(x, y, _dos.ffi.from_buffer(source), width, height, srcx,
                      srcy, srcw, srch, colorkey)


def clearscreen() -> None:
    _dos.lib.clearscreen()


def getpixel(x: int, y: int) -> int:
    return _dos.lib.getpixel(x, y)


def hline(x: int, y: int, len: int, color: int) -> None:
    _dos.lib.hline(x, y, len, color)


def putpixel(x: int, y: int, color: int) -> None:
    _dos.lib.putpixel(x, y, color)


def setdrawtarget(pixels: buffer, width: int, height: int) -> None:
    size = width * height
    if len(pixels) < size:
        raise ValueError(f'pixel buffer must be at least {size} bytes')
    _dos.lib.setdrawtarget(_dos.ffi.from_buffer(pixels), width, height)


def resetdrawtarget() -> None:
    _dos.lib.resetdrawtarget()


def setcolor(color: int) -> None:
    _dos.lib.setcolor(color)


def getcolor() -> int:
    return _dos.lib.getcolor()


def line(x1: int, y1: int, x2: int, y2: int) -> None:
    _dos.lib.line(x1, y1, x2, y2)


def rectangle(x: int, y: int, w: int, h: int) -> None:
    _dos.lib.rectangle(x, y, w, h)


def bar(x: int, y: int, w: int, h: int) -> None:
    _dos.lib.bar(x, y, w, h)


def circle(x: int, y: int, r: int) -> None:
    _dos.lib.circle(x, y, r)


def fillcircle(x: int, y: int, r: int) -> None:
    _dos.lib.fillcircle(x, y, r)


def ellipse(x: int, y: int, rx: int, ry: int) -> None:
    _dos.lib.ellipse(x, y, rx, ry)


def fillellipse(x: int, y: int, rx: int, ry: int) -> None:
    _dos.lib.fillellipse(x, y, rx, ry)


def drawpoly(points_xy: Points) -> None:
    points_data = _data_for_points(points_xy)
    count = len(points_data) // 2
    _dos.lib.drawpoly(points_data, count)


def fillpoly(points_xy: Points) -> None:
    points_data = _data_for_points(points_xy)
    count = len(points_data) // 2
    _dos.lib.fillpoly(points_data, count)


def floodfill(x: int, y: int) -> None:
    _dos.lib.floodfill(x, y)


def boundaryfill(x: int, y: int, boundary: int) -> None:
    _dos.lib.boundaryfill(x, y, boundary)


def outtextxy(x: int, y: int, text: bytes | str | os.PathLike) -> None:
    _dos.lib.outtextxy(x, y, c_string(text, encoding=cp437.ENCODING))


def wraptextxy(x: int, y: int, text: bytes | str | os.PathLike,
               width: int) -> None:
    _dos.lib.wraptextxy(x, y, c_string(text, encoding=cp437.ENCODING), width)


def centertextxy(x: int, y: int, text: bytes | str | os.PathLike,
                 width: int) -> None:
    _dos.lib.centertextxy(x, y, c_string(text, encoding=cp437.ENCODING), width)


def settextstyle(font: FontHandle,
                 bold: bool = False,
                 italic: bool = False,
                 underline: bool = False) -> None:
    _dos.lib.settextstyle(font, bold, italic, underline)


def installuserfont(filename: bytes | str | os.PathLike) -> FontHandle:
    result: int = _dos.lib.installuserfont(c_string(filename))
    if result == 0:
        raise ValueError(f'Failed to load font {filename}')
    return FontHandle(result)


def setsoundbank(soundbank: SoundBankHandle) -> None:
    _dos.lib.setsoundbank(soundbank)


def installusersoundbank(
        filename: bytes | str | os.PathLike) -> SoundBankHandle:
    result: int = _dos.lib.installuserfont(c_string(filename))
    if result == 0:
        raise ValueError(f'Failed to load soundbank {filename}')
    return SoundBankHandle(result)


def noteon(channel: int, note: int, velocity: int) -> None:
    _dos.lib.noteon(channel, note, velocity)


def noteoff(channel: int, note: int) -> None:
    _dos.lib.noteoff(channel, note)


def allnotesoff(channel: int) -> None:
    _dos.lib.allnotesoff(channel)


def setinstrument(channel: int, instrument: int) -> None:
    _dos.lib.setinstrument(channel, instrument)


def loadmid(filename: bytes | str | os.PathLike) -> Music | None:
    result = _dos.lib.loadmid(c_string(filename))
    return None if result == _dos.ffi.NULL else Music(result, filename)


def loadmus(filename: bytes | str | os.PathLike) -> Music | None:
    result = _dos.lib.loadmus(c_string(filename))
    return None if result == _dos.ffi.NULL else Music(result, filename)


def loadmod(filename: bytes | str | os.PathLike) -> Music | None:
    result = _dos.lib.loadmod(c_string(filename))
    return None if result == _dos.ffi.NULL else Music(result, filename)


def loadopb(filename: bytes | str | os.PathLike) -> Music | None:
    result = _dos.lib.loadopb(c_string(filename))
    return None if result == _dos.ffi.NULL else Music(result, filename)


def createmus(data: buffer) -> Music | None:
    result = _dos.lib.createmus(_dos.ffi.from_buffer(data), len(data))
    return None if result == _dos.ffi.NULL else Music(result)


def playmusic(music: Music, loop: bool = False, volume: int = 255) -> None:
    _dos.lib.playmusic(music._music_ptr, loop, volume)


def stopmusic() -> None:
    _dos.lib.stopmusic()


def musicplaying() -> bool:
    return bool(_dos.lib.musicplaying())


def musicvolume(volume: int) -> None:
    _dos.lib.musicvolume(volume)


def setsoundmode(mode: SoundMode) -> None:
    _dos.lib.setsoundmode(mode.value)


def loadwav(filename: bytes | str | os.PathLike) -> Sound | None:
    result = _dos.lib.loadwav(c_string(filename))
    return None if result == _dos.ffi.NULL else Sound(result, filename)


def createsound(
    channels: int,
    samplerate: int,
    samples: Samples,
) -> Sound | None:
    data, size = _data_for_samples(samples)
    framecount = size // channels // 2  # 2 bytes per sample
    result = _dos.lib.createsound(channels, samplerate, framecount, data)
    return None if result == _dos.ffi.NULL else Sound(result)


def playsound(channel: int,
              sound: Sound,
              loop: bool = False,
              volume: int = 255) -> None:
    _dos.lib.playsound(channel, sound._sound_ptr, loop, volume)


def stopsound(channel: int) -> None:
    _dos.lib.stopsound(channel)


def soundplaying(channel: int) -> bool:
    return bool(_dos.lib.soundplaying(channel))


def soundvolume(channel: int, left: int, right: int) -> None:
    _dos.lib.soundvolume(channel, left, right)


def keystate(key: KeyCode) -> bool:
    return bool(_dos.lib.keystate(key.value))


def readkeys() -> list[KeyCode]:
    result: list[KeyCode] = []
    keycodes = _dos.lib.readkeys()
    while keycodes[0] != KEY_INVALID.value:
        result.append(KeyCode(keycodes[0]))
        keycodes += 1
    return result


def readchars() -> str:
    chars = _dos.lib.readchars()
    return _dos.ffi.string(chars).decode('cp437')


def mousex() -> int:
    return _dos.lib.mousex()


def mousey() -> int:
    return _dos.lib.mousey()


def mouserelx() -> int:
    return _dos.lib.mouserelx()


def mouserely() -> int:
    return _dos.lib.mouserely()
