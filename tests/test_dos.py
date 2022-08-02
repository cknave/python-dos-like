#!/usr/bin/env python
import base64
import os
import pathlib
import struct
import tempfile
import unittest
import uuid

import dos_like
from dos_like.dos import *


class Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        dos_like.run_in_background(['-w'])

    @classmethod
    def tearDownClass(cls) -> None:
        super().tearDownClass()
        dos_like.stop()

    def setUp(self) -> None:
        super().setUp()
        resetdrawtarget()
        clearscreen()
        # clear out keyboard buffers
        while readchars():
            pass
        while readkeys():
            pass

    def test_set_video_mode(self):
        setvideomode(videomode_320x200)
        self.assertEqual(320, screenwidth())
        self.assertEqual(200, screenheight())

    def test_double_buffer(self):
        setdoublebuffer(True)
        screenbuffer()[0] = b'\x42'
        self.assertNotEqual(swapbuffers()[0], b'\x42')
        self.assertNotEqual(screenbuffer()[0], b'\x42')

    def test_single_buffer(self):
        setdoublebuffer(False)
        screenbuffer()[0] = b'\x42'
        self.assertEqual(swapbuffers()[0], b'\x42')
        self.assertEqual(screenbuffer()[0], b'\x42')

    def test_set_palette_with_ints(self):
        setpal(10, 2, 4, 6)
        self.assertEqual(RGB(2, 4, 6), getpal(10))

    def test_set_palette_with_rgb(self):
        setpal(20, RGB(3, 5, 7))
        self.assertEqual(RGB(3, 5, 7), getpal(20))

    def test_set_palette_with_tuple(self):
        setpal(30, (5, 9, 13))
        self.assertEqual(RGB(5, 9, 13), getpal(30))

    def test_not_shutting_down(self):
        self.assertIs(False, shuttingdown())

    def test_cputs(self):
        setvideomode(videomode_80x25_8x16)
        for value in 'hello ☻', b'hello \x02', pathlib.Path('hello ☻'):
            gotoxy(0, 0)
            textbackground(0x00)
            textcolor(0x0f)
            clrscr()
            cputs(value)
            screen = screenbuffer()
            self.assertEqual(b'h\x0fe\x0fl\x0fl\x0fo\x0f \x0f\x02\x0f',
                             screen[:14], f'for value {value!r}')

    def test_textcolor(self):
        setvideomode(videomode_80x25_8x16)
        gotoxy(0, 0)
        textbackground(0x01)
        textcolor(0x09)
        cputs('X')
        self.assertEqual(b'\x19', screenbuffer()[1])

    def test_cursor_toggle(self):
        # Not much to test here
        curson()
        cursoff()

    def test_clrscr(self):
        setvideomode(videomode_80x25_8x16)
        textbackground(0x07)
        textcolor(0x00)
        clrscr()
        self.assertEqual(b' \x70' * 80 * 25, screenbuffer()[:80 * 25 * 2])

    def test_cursor_position(self):
        setvideomode(videomode_80x25_8x16)
        gotoxy(6, 7)
        self.assertEqual(6, wherex())
        self.assertEqual(7, wherey())

    def test_loadgif(self):
        gif_data = base64.b64decode(
            'R0lGODdhAwACAMIGAAAA//8AAP8A/wD/AAD/////AP///wAAACwAAAAAAwACAAADBAghQ5UAOw=='
        )
        with tempfile.NamedTemporaryFile(mode='wb') as f:
            f.write(gif_data)
            f.flush()
            gif = loadgif(f.name)
            self.assertIsNotNone(gif)
            self.assertEqual(f.name, gif.filename)
            self.assertEqual(3, gif.width)
            self.assertEqual(2, gif.height)
            self.assertEqual(bytearray([0, 1, 2, 3, 4, 5]), bytes(gif.pixels))
            self.assertListEqual([
                RGB(0, 0, 63),
                RGB(63, 0, 0),
                RGB(63, 0, 63),
                RGB(0, 63, 0),
                RGB(0, 63, 63),
                RGB(63, 63, 0),
                RGB(63, 63, 63),
                RGB(0, 0, 0),
            ], gif.palette)

    def test_loadgif_returns_none_for_nonexistent_path(self):
        result = loadgif(str(uuid.uuid4()))
        self.assertIsNone(result)

    def test_blit(self):
        pixels = new_buffer(b'\x01\x02\x03'
                            b'\x04\x05\x06', 6)
        setvideomode(videomode_320x200)
        blit(10, 15, pixels, width=3, height=2, srcx=0, srcy=0, srcw=3, srch=2)
        screen = screenbuffer()
        self.assertEqual(b'\x01', screen[15 * 320 + 10])
        self.assertEqual(b'\x02', screen[15 * 320 + 11])
        self.assertEqual(b'\x03', screen[15 * 320 + 12])
        self.assertEqual(b'\x04', screen[16 * 320 + 10])
        self.assertEqual(b'\x05', screen[16 * 320 + 11])
        self.assertEqual(b'\x06', screen[16 * 320 + 12])

    def test_maskblit(self):
        pixels = new_buffer(b'\x01\x02\x01'
                            b'\x02\x01\x02', 6)
        setvideomode(videomode_320x200)
        maskblit(10,
                 15,
                 pixels,
                 width=3,
                 height=2,
                 srcx=0,
                 srcy=0,
                 srcw=3,
                 srch=2,
                 colorkey=1)
        screen = screenbuffer()
        self.assertEqual(b'\x00', screen[15 * 320 + 10])
        self.assertEqual(b'\x02', screen[15 * 320 + 11])
        self.assertEqual(b'\x00', screen[15 * 320 + 12])
        self.assertEqual(b'\x02', screen[16 * 320 + 10])
        self.assertEqual(b'\x00', screen[16 * 320 + 11])
        self.assertEqual(b'\x02', screen[16 * 320 + 12])

    def test_clearscreen(self):
        setvideomode(videomode_320x200)
        screen = screenbuffer()
        screen[:320 * 200] = b'\xff' * 320 * 200
        clearscreen()
        self.assertEqual(b'\x00' * 320 * 200, screenbuffer()[:320 * 200])

    def test_getpixel(self):
        setvideomode(videomode_320x200)
        screenbuffer()[322] = b'\x03'
        self.assertEqual(3, getpixel(2, 1))

    def test_hline(self):
        setvideomode(videomode_320x200)
        hline(2, 3, len=2, color=0x0f)
        screen = screenbuffer()
        self.assertEqual(b'\x00', screen[320 * 3 + 1])
        self.assertEqual(b'\x0f', screen[320 * 3 + 2])
        self.assertEqual(b'\x0f', screen[320 * 3 + 3])
        self.assertEqual(b'\x00', screen[320 * 3 + 4])

    def test_putpixel(self):
        setvideomode(videomode_320x200)
        putpixel(7, 8, 9)
        self.assertEqual(b'\x09', screenbuffer()[8 * 320 + 7])

    def test_setdrawtarget_too_small(self):
        pixels = new_buffer(size=3)
        with self.assertRaises(ValueError):
            setdrawtarget(pixels, width=2, height=2)

    def test_setdrawtarget(self):
        pixels = new_buffer(b'\x00' * 4, 4)
        setdrawtarget(pixels, width=2, height=2)
        putpixel(1, 1, 0x0f)
        self.assertEqual(b'\x0f', pixels[3])

    def test_setcolor(self):
        setcolor(42)
        self.assertEqual(42, getcolor())

    @unittest.skipIf(not int(os.environ.get('INTERACTIVE_TESTS', '0')),
                     'INTERACTIVE_TESTS is not set')
    def test_keystate(self):
        self.assertFalse(keystate(KEY_A))
        print('\n\n  Hold and release the A key now...')
        while not keystate(KEY_A):
            pass
        while keystate(KEY_A):
            pass

    @unittest.skipIf(not int(os.environ.get('INTERACTIVE_TESTS', '0')),
                     'INTERACTIVE_TESTS is not set')
    def test_readkeys(self):
        print('\n\n   Hold and release the A key now...')
        # Find a buffer where A is held
        while True:
            keys = readkeys()
            if not keys:
                continue
            self.assertEqual(KEY_A, keys[0])
            break
        # Find a buffer where A is released
        while True:
            keys = [k for k in keys if k != KEY_A]
            if not keys:
                keys = readkeys()
                continue
            self.assertEqual([KEY_A | KEY_MODIFIER_RELEASED], keys)
            break

    @unittest.skipIf(not int(os.environ.get('INTERACTIVE_TESTS', '0')),
                     'INTERACTIVE_TESTS is not set')
    def test_readchars(self):
        print('\n\n   Quickly alternate pressing the A and O keys...')
        while True:
            chars = readchars()
            if len(chars) < 2:
                continue
            if 'a' in chars and 'o' in chars:
                break
            if 'a' not in chars and 'o' not in chars:
                self.fail(f'Unexpected chars: {chars}')
            break
        print('\nOkay stop mashing keys!')
        quiet_vblanks = 0
        while quiet_vblanks < 30:
            if readchars():
                quiet_vblanks = 0
            waitvbl()
            quiet_vblanks += 1

    def test_line(self):
        setvideomode(videomode_320x200)
        setcolor(1)
        line(0, 0, 1, 1)
        screen = screenbuffer()
        self.assertEqual(b'\x01\x00', screen[0:2])
        self.assertEqual(b'\x00\x01', screen[320:322])

    def test_rectangle(self):
        setvideomode(videomode_320x200)
        setcolor(1)
        # height is off by 1?
        rectangle(0, 0, 3, 2)
        screen = screenbuffer()
        self.assertEqual(b'\x01\x01\x01', screen[0:3])
        self.assertEqual(b'\x01\x00\x01', screen[320:323])
        self.assertEqual(b'\x01\x01\x01', screen[640:643])

    def test_bar(self):
        setvideomode(videomode_320x200)
        setcolor(1)
        bar(0, 0, 3, 3)
        screen = screenbuffer()
        self.assertEqual(b'\x01\x01\x01', screen[0:3])
        self.assertEqual(b'\x01\x01\x01', screen[320:323])
        self.assertEqual(b'\x01\x01\x01', screen[640:643])

    def test_circle(self):
        setvideomode(videomode_320x200)
        setcolor(1)
        circle(1, 1, 1)
        screen = screenbuffer()
        self.assertEqual(b'\x00\x01\x00', screen[0:3])
        self.assertEqual(b'\x01\x00\x01', screen[320:323])
        self.assertEqual(b'\x00\x01\x00', screen[640:643])

    def test_fillcircle(self):
        setvideomode(videomode_320x200)
        setcolor(1)
        fillcircle(2, 2, 2)
        screen = screenbuffer()
        self.assertEqual(b'\x00\x01\x01\x00', screen[0:4])
        self.assertEqual(b'\x01\x01\x01\x01', screen[320:324])
        self.assertEqual(b'\x01\x01\x01\x01', screen[640:644])
        self.assertEqual(b'\x01\x01\x01\x01', screen[960:964])
        self.assertEqual(b'\x00\x01\x01\x00', screen[1280:1284])

    def test_ellipse(self):
        setvideomode(videomode_320x200)
        setcolor(1)
        ellipse(2, 1, 2, 1)
        screen = screenbuffer()
        self.assertEqual(b'\x00\x01\x01\x01\x00', screen[0:5])
        self.assertEqual(b'\x01\x00\x00\x00\x01', screen[320:325])
        self.assertEqual(b'\x00\x01\x01\x01\x00', screen[640:645])

    def test_fillellipse(self):
        setvideomode(videomode_320x200)
        setcolor(1)
        fillellipse(2, 1, 2, 1)
        screen = screenbuffer()
        self.assertEqual(b'\x00\x01\x01\x00', screen[0:4])
        self.assertEqual(b'\x01\x01\x01\x01', screen[320:324])
        self.assertEqual(b'\x00\x01\x01\x00', screen[640:644])

    def test_drawpoly_fails_with_too_few_points(self):
        with self.assertRaises(ValueError):
            drawpoly([])
        with self.assertRaises(ValueError):
            drawpoly([1])

    def test_fillpoly_fails_with_too_few_points(self):
        with self.assertRaises(ValueError):
            fillpoly([])
        with self.assertRaises(ValueError):
            fillpoly([1])

    def test_drawpoly(self):
        setvideomode(videomode_320x200)
        screen = screenbuffer()

        int_list = [1, 0, 2, 1, 1, 2, 0, 1]
        int_pairs = [(int_list[i], int_list[i + 1])
                     for i in range(0, len(int_list), 2)]
        packed = new_buffer(struct.pack('8i', *int_list))
        for points in [int_list, int_pairs, packed]:
            clearscreen()
            setcolor(1)
            try:
                drawpoly(points)
            except Exception:
                print(f'Failed for points {points!r}')
                raise
            self.assertEqual(b'\x00\x01\x00', screen[0:3],
                             f'for points {points!r}')
            self.assertEqual(b'\x01\x00\x01', screen[320:323],
                             f'for points {points!r}')
            self.assertEqual(b'\x00\x01\x00', screen[640:643],
                             f'for points {points!r}')

    def test_fillpoly(self):
        setvideomode(videomode_320x200)
        screen = screenbuffer()

        int_list = [2, 0, 4, 2, 2, 4, 0, 2]
        int_pairs = [(int_list[i], int_list[i + 1])
                     for i in range(0, len(int_list), 2)]
        packed = new_buffer(struct.pack('8i', *int_list))
        for points in [int_list, int_pairs, packed]:
            clearscreen()
            setcolor(1)
            try:
                fillpoly(points)
            except Exception:
                print(f'Failed for points {points!r}')
                raise
            self.assertEqual(b'\x00\x00\x00\x00', screen[0:4],
                             f'for points {points!r}')
            self.assertEqual(b'\x00\x01\x01\x00', screen[320:324],
                             f'for points {points!r}')
            self.assertEqual(b'\x01\x01\x01\x01', screen[640:644],
                             f'for points {points!r}')
            self.assertEqual(b'\x00\x01\x01\x00', screen[960:964],
                             f'for points {points!r}')

    def test_floodfill(self):
        setvideomode(videomode_320x200)
        screen = screenbuffer()

        # yapf: disable
        screen[0:4]     = b'\x01\x01\x01\x01'
        screen[320:324] = b'\x01\x00\x00\x01'
        screen[640:644] = b'\x01\x00\x00\x01'
        screen[960:964] = b'\x01\x01\x01\x01'
        # yapf: enable

        setcolor(2)
        floodfill(1, 1)
        self.assertEqual(b'\x01\x01\x01\x01', screen[0:4])
        self.assertEqual(b'\x01\x02\x02\x01', screen[320:324])
        self.assertEqual(b'\x01\x02\x02\x01', screen[640:644])
        self.assertEqual(b'\x01\x01\x01\x01', screen[960:964])

    def test_boundaryfill(self):
        setvideomode(videomode_320x200)
        screen = screenbuffer()

        # yapf: disable
        screen[0:4]     = b'\x00\x01\x01\x00'
        screen[320:324] = b'\x01\x00\x00\x01'
        screen[640:644] = b'\x01\x00\x00\x01'
        screen[960:964] = b'\x00\x01\x01\x00'
        # yapf: enable

        setcolor(2)
        boundaryfill(1, 1, 1)
        self.assertEqual(b'\x00\x01\x01\x00', screen[0:4])
        self.assertEqual(b'\x01\x02\x02\x01', screen[320:324])
        self.assertEqual(b'\x01\x02\x02\x01', screen[640:644])
        self.assertEqual(b'\x00\x01\x01\x00', screen[960:964])

    def test_outtextxy(self):
        setvideomode(videomode_320x200)
        settextstyle(DEFAULT_FONT_8X8)
        outtextxy(0, 0, 'Hi')
        self.assertNotEqual(b'\x00' * 8, screenbuffer()[:8])

    def test_wraptextxy(self):
        setvideomode(videomode_320x200)
        settextstyle(DEFAULT_FONT_8X8)
        wraptextxy(0, 0, 'AA', width=7)
        ofs = 9 * 320
        self.assertNotEqual(b'\x00' * 8, screenbuffer()[ofs:ofs + 8])

    def test_centertextxy(self):
        setvideomode(videomode_320x200)
        settextstyle(DEFAULT_FONT_8X8)
        centertextxy(0, 0, 'AA', width=320)
        self.assertNotEqual(b'\x00' * 8, screenbuffer()[152:160])

    def test_installuserfont(self):
        pixels = (b'####### '
                  b'#  #  # '
                  b'   #    '
                  b'   # ## '
                  b'   ##   '
                  b'   # #  '
                  b'   #  # '
                  b'  ###  #').replace(b'#', b'\x01').replace(b' ', b'\x00')
        header_size = 8
        num_offsets = 256
        glyph_size = 2 + 8 * 8
        total_size = header_size + num_offsets * 4 + glyph_size

        # Font header
        height = 8
        line_spacing = 8
        baseline = 6
        font = struct.pack('IBBBx', total_size, height, line_spacing, baseline)

        # Offsets (all to the same glyph)
        font += struct.pack('I', 0) * 256

        # The glyph
        font += b'\x00\x08' + pixels

        with tempfile.NamedTemporaryFile(mode='wb') as f:
            f.write(font)
            f.flush()
            font_handle = installuserfont(f.name)
            self.assertNotEqual(0, font_handle)

        setvideomode(videomode_320x200)
        settextstyle(font_handle)
        setcolor(0x01)
        outtextxy(0, 0, 'A')

        screen = screenbuffer()
        for row in range(8):
            self.assertEqual(pixels[8 * row:8 * (row + 1)],
                             screen[320 * row:320 * row + 8])

    def test_installuserfont_with_nonexistent_path_fails(self):
        with self.assertRaises(ValueError):
            installuserfont(str(uuid.uuid4()))

    def test_installusersoundbank(self):
        op2_path = pathlib.Path(__file__).parent / 'data' / 'test.op2'
        sb_handle = installusersoundbank(op2_path)
        self.assertNotEqual(0, sb_handle)
        setsoundbank(sb_handle)
        setinstrument(0, 0)
        noteon(0, 72, 127)
        allnotesoff(0)

    def test_installusersoundbank_with_nonexistent_path_fails(self):
        with self.assertRaises(ValueError):
            installusersoundbank(str(uuid.uuid4()))

    def test_note_on_and_off(self):
        setsoundbank(DEFAULT_SOUNDBANK_SB16)
        setinstrument(0, 0)
        noteon(0, 72, 64)
        waitvbl()
        noteoff(0, 72)

    def test_load_and_play_music(self):
        for filename, loader in [('test.mod', loadmod), ('test.mid', loadmid),
                                 ('test.mus', loadmus), ('test.opb', loadopb)]:
            path = pathlib.Path(__file__).parent / 'data' / filename
            music = loader(path)
            self.assertIsNotNone(music, f'for {loader.__name__}("{path}")')
            self.assertEqual(path, music.filename)
            playmusic(music)
            self.assertTrue(musicplaying(), f'for {path}')
            stopmusic()
            self.assertFalse(musicplaying(), f'for {path}')

    def test_loadmid_nonexistent_music_paths_returns_none(self):
        for loader in loadmid, loadmus, loadmod, loadopb:
            result = loader(str(uuid.uuid4()))
            self.assertIsNone(result, f'for {loader.__name__}')

    def test_musicvolume(self):
        musicvolume(255)

    def test_createmus(self):
        path = pathlib.Path(__file__).parent / 'data' / 'test.mus'
        with open(path, 'rb') as f:
            mus_data = f.read()
        music = createmus(mus_data)
        self.assertIsNotNone(music)
        self.assertIsNone(music.filename)
        playmusic(music)
        self.assertTrue(musicplaying())
        stopmusic()
        self.assertFalse(musicplaying())

    def test_load_and_play_wav(self):
        wav_path = pathlib.Path(__file__).parent / 'data' / 'test.wav'
        sound = loadwav(wav_path)
        self.assertIsNotNone(sound)
        playsound(0, sound)
        self.assertTrue(soundplaying(0))
        stopsound(0)
        self.assertFalse(soundplaying(0))

    def test_createsound(self):
        sample_rate = 8000
        period = 1 / 440
        amplitude = 8192
        channels = 2
        duration = 0.5
        samples_ints: list[int] = []
        for i in range(int(sample_rate * duration)):
            t = i / sample_rate
            if t % period < period / 2:
                value = amplitude
            else:
                value = -amplitude
            samples_ints.extend([value] * channels)
        samples_buffer = dos_like._dos.ffi.buffer(
            dos_like._dos.ffi.new('short[]', samples_ints))

        for samples in samples_ints, samples_buffer:
            sound = createsound(channels, sample_rate, samples)
            self.assertIsNotNone(sound, f'for samples {type(samples)}')
            playsound(0, sound)
            self.assertTrue(soundplaying(0), f'for samples {type(samples)}')
            stopsound(0)
            self.assertFalse(soundplaying(0), f'for samples {type(samples)}')

    def test_mouse_coords(self):
        # Not much to test here
        mousex()
        mousey()
        mouserelx()
        mouserely()

    def test_new_buffer_with_no_args_fails(self):
        with self.assertRaises(ValueError):
            new_buffer()

    def test_setpal_with_mixed_args_fails(self):
        with self.assertRaises(ValueError):
            setpal(0, RGB(1, 2, 3), 4, 5)
        with self.assertRaises(ValueError):
            setpal(0, (1, 2, 3), 4, 5)

    def test_setpal_with_non_3_tuple_fails(self):
        with self.assertRaises(ValueError):
            setpal(0, (1, 2, 3, 4))

    def test_setsoundmode(self):
        setsoundmode(soundmode_16bit_stereo_44100)
        # Not much else to test

    def test_soundvolume(self):
        soundvolume(0, 255, 255)
        # Not much else to test
