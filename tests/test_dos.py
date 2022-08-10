#!/usr/bin/env python
import os
import pathlib
import struct
import tempfile
import unittest
import uuid

import dos_like
from dos_like import dos


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
        dos.resetdrawtarget()
        dos.clearscreen()
        # clear out keyboard buffers
        while dos.readchars():
            pass
        while dos.readkeys():
            pass

    def test_set_video_mode(self):
        dos.setvideomode(dos.videomode_320x200)
        self.assertEqual(320, dos.screenwidth())
        self.assertEqual(200, dos.screenheight())

    def test_double_buffer(self):
        dos.setdoublebuffer(True)
        dos.screenbuffer()[0] = b'\x42'
        self.assertNotEqual(dos.swapbuffers()[0], b'\x42')
        self.assertNotEqual(dos.screenbuffer()[0], b'\x42')

    def test_single_buffer(self):
        dos.setdoublebuffer(False)
        dos.screenbuffer()[0] = b'\x42'
        self.assertEqual(dos.swapbuffers()[0], b'\x42')
        self.assertEqual(dos.screenbuffer()[0], b'\x42')

    def test_set_palette_with_ints(self):
        dos.setpal(10, 2, 4, 6)
        self.assertEqual(dos.RGB(2, 4, 6), dos.getpal(10))

    def test_set_palette_with_dos_rgb(self):
        dos.setpal(20, dos.RGB(3, 5, 7))
        self.assertEqual(dos.RGB(3, 5, 7), dos.getpal(20))

    def test_set_palette_with_tuple(self):
        dos.setpal(30, (5, 9, 13))
        self.assertEqual(dos.RGB(5, 9, 13), dos.getpal(30))

    def test_not_shutting_down(self):
        self.assertIs(False, dos.shuttingdown())

    def test_dos_cputs(self):
        dos.setvideomode(dos.videomode_80x25_8x16)
        for value in 'hello ☻', b'hello \x02', pathlib.Path('hello ☻'):
            dos.gotoxy(0, 0)
            dos.textbackground(0x00)
            dos.textcolor(0x0f)
            dos.clrscr()
            dos.cputs(value)
            screen = dos.screenbuffer()
            self.assertEqual(b'h\x0fe\x0fl\x0fl\x0fo\x0f \x0f\x02\x0f',
                             screen[:14], f'for value {value!r}')

    def test_dos_textcolor(self):
        dos.setvideomode(dos.videomode_80x25_8x16)
        dos.gotoxy(0, 0)
        dos.textbackground(0x01)
        dos.textcolor(0x09)
        dos.cputs('X')
        self.assertEqual(b'\x19', dos.screenbuffer()[1])

    def test_cursor_toggle(self):
        # Not much to test here
        dos.curson()
        dos.cursoff()

    def test_dos_clrscr(self):
        dos.setvideomode(dos.videomode_80x25_8x16)
        dos.textbackground(0x07)
        dos.textcolor(0x00)
        dos.clrscr()
        self.assertEqual(b' \x70' * 80 * 25, dos.screenbuffer()[:80 * 25 * 2])

    def test_cursor_position(self):
        dos.setvideomode(dos.videomode_80x25_8x16)
        dos.gotoxy(6, 7)
        self.assertEqual(6, dos.wherex())
        self.assertEqual(7, dos.wherey())

    def test_loadgif(self):
        gif_path = pathlib.Path(__file__).parent / 'data' / 'test.gif'
        gif = dos.loadgif(gif_path)
        self.assertIsNotNone(gif)
        self.assertEqual('test.gif', gif.filename)
        self.assertEqual(3, gif.width)
        self.assertEqual(2, gif.height)
        self.assertEqual(bytearray([0, 1, 2, 3, 4, 5]), bytes(gif.pixels))
        self.assertListEqual([
            dos.RGB(0, 0, 63),
            dos.RGB(63, 0, 0),
            dos.RGB(63, 0, 63),
            dos.RGB(0, 63, 0),
            dos.RGB(0, 63, 63),
            dos.RGB(63, 63, 0),
            dos.RGB(63, 63, 63),
            dos.RGB(0, 0, 0),
        ], gif.palette)

    def test_loadgif_returns_none_for_nonexistent_path(self):
        result = dos.loadgif(str(uuid.uuid4()))
        self.assertIsNone(result)

    def test_blit(self):
        pixels = dos.new_buffer(b'\x01\x02\x03'
                                b'\x04\x05\x06', 6)
        dos.setvideomode(dos.videomode_320x200)
        dos.blit(10,
                 15,
                 pixels,
                 width=3,
                 height=2,
                 srcx=0,
                 srcy=0,
                 srcw=3,
                 srch=2)
        screen = dos.screenbuffer()
        self.assertEqual(b'\x01', screen[15 * 320 + 10])
        self.assertEqual(b'\x02', screen[15 * 320 + 11])
        self.assertEqual(b'\x03', screen[15 * 320 + 12])
        self.assertEqual(b'\x04', screen[16 * 320 + 10])
        self.assertEqual(b'\x05', screen[16 * 320 + 11])
        self.assertEqual(b'\x06', screen[16 * 320 + 12])

    def test_maskblit(self):
        pixels = dos.new_buffer(b'\x01\x02\x01'
                                b'\x02\x01\x02', 6)
        dos.setvideomode(dos.videomode_320x200)
        dos.maskblit(10,
                     15,
                     pixels,
                     width=3,
                     height=2,
                     srcx=0,
                     srcy=0,
                     srcw=3,
                     srch=2,
                     colorkey=1)
        screen = dos.screenbuffer()
        self.assertEqual(b'\x00', screen[15 * 320 + 10])
        self.assertEqual(b'\x02', screen[15 * 320 + 11])
        self.assertEqual(b'\x00', screen[15 * 320 + 12])
        self.assertEqual(b'\x02', screen[16 * 320 + 10])
        self.assertEqual(b'\x00', screen[16 * 320 + 11])
        self.assertEqual(b'\x02', screen[16 * 320 + 12])

    def test_dos_clearscreen(self):
        dos.setvideomode(dos.videomode_320x200)
        screen = dos.screenbuffer()
        screen[:320 * 200] = b'\xff' * 320 * 200
        dos.clearscreen()
        self.assertEqual(b'\x00' * 320 * 200, dos.screenbuffer()[:320 * 200])

    def test_getpixel(self):
        dos.setvideomode(dos.videomode_320x200)
        dos.screenbuffer()[322] = b'\x03'
        self.assertEqual(3, dos.getpixel(2, 1))

    def test_hline(self):
        dos.setvideomode(dos.videomode_320x200)
        dos.hline(2, 3, len=2, color=0x0f)
        screen = dos.screenbuffer()
        self.assertEqual(b'\x00', screen[320 * 3 + 1])
        self.assertEqual(b'\x0f', screen[320 * 3 + 2])
        self.assertEqual(b'\x0f', screen[320 * 3 + 3])
        self.assertEqual(b'\x00', screen[320 * 3 + 4])

    def test_putpixel(self):
        dos.setvideomode(dos.videomode_320x200)
        dos.putpixel(7, 8, 9)
        self.assertEqual(b'\x09', dos.screenbuffer()[8 * 320 + 7])

    def test_setdrawtarget_too_small(self):
        pixels = dos.new_buffer(size=3)
        with self.assertRaises(ValueError):
            dos.setdrawtarget(pixels, width=2, height=2)

    def test_setdrawtarget(self):
        pixels = dos.new_buffer(b'\x00' * 4, 4)
        dos.setdrawtarget(pixels, width=2, height=2)
        dos.putpixel(1, 1, 0x0f)
        self.assertEqual(b'\x0f', pixels[3])

    def test_dos_setcolor(self):
        dos.setcolor(42)
        self.assertEqual(42, dos.getcolor())

    @unittest.skipIf(not int(os.environ.get('INTERACTIVE_TESTS', '0')),
                     'INTERACTIVE_TESTS is not set')
    def test_keystate(self):
        self.assertFalse(dos.keystate(dos.KEY_A))
        print('\n\n  Hold and release the A key now...')
        while not dos.keystate(dos.KEY_A):
            pass
        while dos.keystate(dos.KEY_A):
            pass

    @unittest.skipIf(not int(os.environ.get('INTERACTIVE_TESTS', '0')),
                     'INTERACTIVE_TESTS is not set')
    def test_dos_readkeys(self):
        print('\n\n   Hold and release the A key now...')
        # Find a buffer where A is held
        while True:
            keys = dos.readkeys()
            if not keys:
                continue
            self.assertEqual(dos.KEY_A, keys[0])
            break
        # Find a buffer where A is released
        while True:
            keys = [k for k in keys if k != dos.KEY_A]
            if not keys:
                keys = dos.readkeys()
                continue
            self.assertEqual([dos.KEY_A | dos.KEY_MODIFIER_RELEASED], keys)
            break

    @unittest.skipIf(not int(os.environ.get('INTERACTIVE_TESTS', '0')),
                     'INTERACTIVE_TESTS is not set')
    def test_dos_readchars(self):
        print('\n\n   Quickly alternate pressing the A and O keys...')
        while True:
            chars = dos.readchars()
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
            if dos.readchars():
                quiet_vblanks = 0
            dos.waitvbl()
            quiet_vblanks += 1

    def test_line(self):
        dos.setvideomode(dos.videomode_320x200)
        dos.setcolor(1)
        dos.line(0, 0, 1, 1)
        screen = dos.screenbuffer()
        self.assertEqual(b'\x01\x00', screen[0:2])
        self.assertEqual(b'\x00\x01', screen[320:322])

    def test_rectangle(self):
        dos.setvideomode(dos.videomode_320x200)
        dos.setcolor(1)
        # height is off by 1?
        dos.rectangle(0, 0, 3, 2)
        screen = dos.screenbuffer()
        self.assertEqual(b'\x01\x01\x01', screen[0:3])
        self.assertEqual(b'\x01\x00\x01', screen[320:323])
        self.assertEqual(b'\x01\x01\x01', screen[640:643])

    def test_bar(self):
        dos.setvideomode(dos.videomode_320x200)
        dos.setcolor(1)
        dos.bar(0, 0, 3, 3)
        screen = dos.screenbuffer()
        self.assertEqual(b'\x01\x01\x01', screen[0:3])
        self.assertEqual(b'\x01\x01\x01', screen[320:323])
        self.assertEqual(b'\x01\x01\x01', screen[640:643])

    def test_circle(self):
        dos.setvideomode(dos.videomode_320x200)
        dos.setcolor(1)
        dos.circle(1, 1, 1)
        screen = dos.screenbuffer()
        self.assertEqual(b'\x00\x01\x00', screen[0:3])
        self.assertEqual(b'\x01\x00\x01', screen[320:323])
        self.assertEqual(b'\x00\x01\x00', screen[640:643])

    def test_fillcircle(self):
        dos.setvideomode(dos.videomode_320x200)
        dos.setcolor(1)
        dos.fillcircle(2, 2, 2)
        screen = dos.screenbuffer()
        self.assertEqual(b'\x00\x01\x01\x00', screen[0:4])
        self.assertEqual(b'\x01\x01\x01\x01', screen[320:324])
        self.assertEqual(b'\x01\x01\x01\x01', screen[640:644])
        self.assertEqual(b'\x01\x01\x01\x01', screen[960:964])
        self.assertEqual(b'\x00\x01\x01\x00', screen[1280:1284])

    def test_ellipse(self):
        dos.setvideomode(dos.videomode_320x200)
        dos.setcolor(1)
        dos.ellipse(2, 1, 2, 1)
        screen = dos.screenbuffer()
        self.assertEqual(b'\x00\x01\x01\x01\x00', screen[0:5])
        self.assertEqual(b'\x01\x00\x00\x00\x01', screen[320:325])
        self.assertEqual(b'\x00\x01\x01\x01\x00', screen[640:645])

    def test_fillellipse(self):
        dos.setvideomode(dos.videomode_320x200)
        dos.setcolor(1)
        dos.fillellipse(2, 1, 2, 1)
        screen = dos.screenbuffer()
        self.assertEqual(b'\x00\x01\x01\x00', screen[0:4])
        self.assertEqual(b'\x01\x01\x01\x01', screen[320:324])
        self.assertEqual(b'\x00\x01\x01\x00', screen[640:644])

    def test_drawpoly_fails_with_too_few_points(self):
        with self.assertRaises(ValueError):
            dos.drawpoly([])
        with self.assertRaises(ValueError):
            dos.drawpoly([1])

    def test_fillpoly_fails_with_too_few_points(self):
        with self.assertRaises(ValueError):
            dos.fillpoly([])
        with self.assertRaises(ValueError):
            dos.fillpoly([1])

    def test_drawpoly(self):
        dos.setvideomode(dos.videomode_320x200)
        screen = dos.screenbuffer()

        int_list = [1, 0, 2, 1, 1, 2, 0, 1]
        int_pairs = [(int_list[i], int_list[i + 1])
                     for i in range(0, len(int_list), 2)]
        packed = dos.new_buffer(struct.pack('8i', *int_list))
        for points in [int_list, int_pairs, packed]:
            dos.clearscreen()
            dos.setcolor(1)
            try:
                dos.drawpoly(points)
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
        dos.setvideomode(dos.videomode_320x200)
        screen = dos.screenbuffer()

        int_list = [2, 0, 4, 2, 2, 4, 0, 2]
        int_pairs = [(int_list[i], int_list[i + 1])
                     for i in range(0, len(int_list), 2)]
        packed = dos.new_buffer(struct.pack('8i', *int_list))
        for points in [int_list, int_pairs, packed]:
            dos.clearscreen()
            dos.setcolor(1)
            try:
                dos.fillpoly(points)
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
        dos.setvideomode(dos.videomode_320x200)
        screen = dos.screenbuffer()

        # yapf: disable
        screen[0:4]     = b'\x01\x01\x01\x01'  # noqa: E221
        screen[320:324] = b'\x01\x00\x00\x01'
        screen[640:644] = b'\x01\x00\x00\x01'
        screen[960:964] = b'\x01\x01\x01\x01'
        # yapf: enable

        dos.setcolor(2)
        dos.floodfill(1, 1)
        self.assertEqual(b'\x01\x01\x01\x01', screen[0:4])
        self.assertEqual(b'\x01\x02\x02\x01', screen[320:324])
        self.assertEqual(b'\x01\x02\x02\x01', screen[640:644])
        self.assertEqual(b'\x01\x01\x01\x01', screen[960:964])

    def test_boundaryfill(self):
        dos.setvideomode(dos.videomode_320x200)
        screen = dos.screenbuffer()

        # yapf: disable
        screen[0:4]     = b'\x00\x01\x01\x00'  # noqa: E221
        screen[320:324] = b'\x01\x00\x00\x01'
        screen[640:644] = b'\x01\x00\x00\x01'
        screen[960:964] = b'\x00\x01\x01\x00'
        # yapf: enable

        dos.setcolor(2)
        dos.boundaryfill(1, 1, 1)
        self.assertEqual(b'\x00\x01\x01\x00', screen[0:4])
        self.assertEqual(b'\x01\x02\x02\x01', screen[320:324])
        self.assertEqual(b'\x01\x02\x02\x01', screen[640:644])
        self.assertEqual(b'\x00\x01\x01\x00', screen[960:964])

    def test_dos_outtextxy(self):
        dos.setvideomode(dos.videomode_320x200)
        dos.settextstyle(dos.DEFAULT_FONT_8X8)
        dos.outtextxy(0, 0, 'Hi')
        self.assertNotEqual(b'\x00' * 8, dos.screenbuffer()[:8])

    def test_wraptextxy(self):
        dos.setvideomode(dos.videomode_320x200)
        dos.settextstyle(dos.DEFAULT_FONT_8X8)
        dos.wraptextxy(0, 0, 'AA', width=7)
        ofs = 9 * 320
        self.assertNotEqual(b'\x00' * 8, dos.screenbuffer()[ofs:ofs + 8])

    def test_centertextxy(self):
        dos.setvideomode(dos.videomode_320x200)
        dos.settextstyle(dos.DEFAULT_FONT_8X8)
        dos.centertextxy(0, 0, 'AA', width=320)
        self.assertNotEqual(b'\x00' * 8, dos.screenbuffer()[152:160])

    def test_dos_installuserfont(self):
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
            font_handle = dos.installuserfont(f.name)
            self.assertNotEqual(0, font_handle)

        dos.setvideomode(dos.videomode_320x200)
        dos.settextstyle(font_handle)
        dos.setcolor(0x01)
        dos.outtextxy(0, 0, 'A')

        screen = dos.screenbuffer()
        for row in range(8):
            self.assertEqual(pixels[8 * row:8 * (row + 1)],
                             screen[320 * row:320 * row + 8])

    def test_dos_installuserfont_with_nonexistent_path_fails(self):
        with self.assertRaises(ValueError):
            dos.installuserfont(str(uuid.uuid4()))

    def test_installusersoundbank(self):
        op2_path = pathlib.Path(__file__).parent / 'data' / 'test.op2'
        sb_handle = dos.installusersoundbank(op2_path)
        self.assertNotEqual(0, sb_handle)
        dos.setsoundbank(sb_handle)
        dos.setinstrument(0, 0)
        dos.noteon(0, 72, 127)
        dos.allnotesoff(0)

    def test_installusersoundbank_with_nonexistent_path_fails(self):
        with self.assertRaises(ValueError):
            dos.installusersoundbank(str(uuid.uuid4()))

    def test_note_on_and_off(self):
        dos.setsoundbank(dos.DEFAULT_SOUNDBANK_SB16)
        dos.setinstrument(0, 0)
        dos.noteon(0, 72, 64)
        dos.waitvbl()
        dos.noteoff(0, 72)

    def test_load_and_play_music(self):
        for filename, loader in [('test.mod', dos.loadmod),
                                 ('test.mid', dos.loadmid),
                                 ('test.mus', dos.loadmus),
                                 ('test.opb', dos.loadopb)]:
            path = pathlib.Path(__file__).parent / 'data' / filename
            music = loader(path)
            self.assertIsNotNone(music, f'for {loader.__name__}("{path}")')
            self.assertEqual(filename, music.filename)
            dos.playmusic(music)
            self.assertTrue(dos.musicplaying(), f'for {path}')
            dos.stopmusic()
            self.assertFalse(dos.musicplaying(), f'for {path}')

    def test_loadmid_nonexistent_music_paths_returns_none(self):
        for loader in dos.loadmid, dos.loadmus, dos.loadmod, dos.loadopb:
            result = loader(str(uuid.uuid4()))
            self.assertIsNone(result, f'for {loader.__name__}')

    def test_musicvolume(self):
        dos.musicvolume(255)

    def test_createmus(self):
        path = pathlib.Path(__file__).parent / 'data' / 'test.mus'
        with open(path, 'rb') as f:
            mus_data = f.read()
        music = dos.createmus(mus_data)
        self.assertIsNotNone(music)
        self.assertIsNone(music.filename)
        dos.playmusic(music)
        self.assertTrue(dos.musicplaying())
        dos.stopmusic()
        self.assertFalse(dos.musicplaying())

    def test_load_and_play_wav(self):
        wav_path = pathlib.Path(__file__).parent / 'data' / 'test.wav'
        sound = dos.loadwav(wav_path)
        self.assertIsNotNone(sound)
        dos.playsound(0, sound)
        self.assertTrue(dos.soundplaying(0))
        dos.stopsound(0)
        self.assertFalse(dos.soundplaying(0))

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
            sound = dos.createsound(channels, sample_rate, samples)
            self.assertIsNotNone(sound, f'for samples {type(samples)}')
            dos.playsound(0, sound)
            self.assertTrue(dos.soundplaying(0),
                            f'for samples {type(samples)}')
            dos.stopsound(0)
            self.assertFalse(dos.soundplaying(0),
                             f'for samples {type(samples)}')

    def test_mouse_coords(self):
        # Not much to test here
        dos.mousex()
        dos.mousey()
        dos.mouserelx()
        dos.mouserely()

    def test_new_buffer_with_no_args_fails(self):
        with self.assertRaises(ValueError):
            dos.new_buffer()

    def test_dos_setpal_with_mixed_args_fails(self):
        with self.assertRaises(ValueError):
            dos.setpal(0, dos.RGB(1, 2, 3), 4, 5)
        with self.assertRaises(ValueError):
            dos.setpal(0, (1, 2, 3), 4, 5)

    def test_dos_setpal_with_non_3_tuple_fails(self):
        with self.assertRaises(ValueError):
            dos.setpal(0, (1, 2, 3, 4))

    def test_setsoundmode(self):
        dos.setsoundmode(dos.soundmode_16bit_stereo_44100)
        # Not much else to test

    def test_soundvolume(self):
        dos.soundvolume(0, 255, 255)
        # Not much else to test
