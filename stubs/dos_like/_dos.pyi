import cffi

ffi: cffi.FFI


class Lib:
    DEFAULT_FONT_8X8: int
    DEFAULT_FONT_8X16: int
    DEFAULT_FONT_9X16: int
    DEFAULT_SOUNDBANK_AWE32: int
    DEFAULT_SOUNDBANK_SB16: int
    KEY_MODIFIER_RELEASED: int
    MUSIC_CHANNELS: int
    SOUND_CHANNELS: int

    def main(self, argc: int, argv: cffi.CData) -> int:
        ...

    def free(self, ptr: cffi.CData) -> None:
        ...

    def setvideomode(self, mode: int) -> None:
        ...

    def setdoublebuffer(self, enabled: int) -> None:
        ...

    def screenwidth(self) -> int:
        ...

    def screenheight(self) -> int:
        ...

    def screenbuffer(self) -> cffi.CData:
        ...

    def swapbuffers(self) -> cffi.CData:
        ...

    def waitvbl(self) -> None:
        ...

    def setpal(self, index: int, r: int, g: int, b: int) -> None:
        ...

    def getpal(self, index: int, r: cffi.CData, g: cffi.CData,
               b: cffi.CData) -> None:
        ...

    def shuttingdown(self) -> int:
        ...

    def cputs(self, string: cffi.CData) -> None:
        ...

    def textcolor(self, color: int) -> None:
        ...

    def textbackground(self, color: int) -> None:
        ...

    def gotoxy(self, x: int, y: int) -> None:
        ...

    def wherex(self) -> int:
        ...

    def wherey(self) -> int:
        ...

    def clrscr(self) -> None:
        ...

    def curson(self) -> None:
        ...

    def cursoff(self) -> None:
        ...

    def loadgif(self, filename: cffi.CData, width: cffi.CData,
                height: cffi.CData, palcount: cffi.CData,
                palette: cffi.CData) -> cffi.CData:
        ...

    def blit(self, x: int, y: int, source: cffi.CData, width: int, height: int,
             srcx: int, srcy: int, srcw: int, srch: int) -> None:
        ...

    def maskblit(self, x: int, y: int, source: cffi.CData, width: int,
                 height: int, srcx: int, srcy: int, srcw: int, srch: int,
                 colorkey: int) -> None:
        ...

    def clearscreen(self) -> None:
        ...

    def getpixel(self, x: int, y: int) -> int:
        ...

    def hline(self, x: int, y: int, len: int, color: int) -> None:
        ...

    def putpixel(self, x: int, y: int, color: int) -> None:
        ...

    def setdrawtarget(self, pixels: cffi.CData, width: int,
                      height: int) -> None:
        ...

    def resetdrawtarget(self) -> None:
        ...

    def setcolor(self, color: int) -> None:
        ...

    def getcolor(self) -> int:
        ...

    def line(self, x1: int, y1: int, x2: int, y2: int) -> None:
        ...

    def rectangle(self, x: int, y: int, w: int, h: int) -> None:
        ...

    def bar(self, x: int, y: int, w: int, h: int) -> None:
        ...

    def circle(self, x: int, y: int, r: int) -> None:
        ...

    def fillcircle(self, x: int, y: int, r: int) -> None:
        ...

    def ellipse(self, x: int, y: int, rx: int, ry: int) -> None:
        ...

    def fillellipse(self, x: int, y: int, rx: int, ry: int) -> None:
        ...

    def drawpoly(self, points_xy: cffi.CData, count: int) -> None:
        ...

    def fillpoly(self, points_xy: cffi.CData, count: int) -> None:
        ...

    def floodfill(self, x: int, y: int) -> None:
        ...

    def boundaryfill(self, x: int, y: int, boundary: int) -> None:
        ...

    def outtextxy(self, x: int, y: int, text: cffi.CData) -> None:
        ...

    def wraptextxy(self, x: int, y: int, text: cffi.CData, width: int) -> None:
        ...

    def centertextxy(self, x: int, y: int, text: cffi.CData,
                     width: int) -> None:
        ...

    def settextstyle(self, font: int, bold: int, italic: int,
                     underline: int) -> None:
        ...

    def installuserfont(self, filename: cffi.CData) -> int:
        ...

    def setsoundbank(self, soundbank: int) -> None:
        ...

    def installusersoundbank(self, filename: cffi.CData) -> int:
        ...

    def noteon(self, channel: int, note: int, velocity: int) -> None:
        ...

    def noteoff(self, channel: int, note: int) -> None:
        ...

    def allnotesoff(self, channel: int) -> None:
        ...

    def setinstrument(self, channel: int, instrument: int) -> None:
        ...

    def loadmid(self, filename: cffi.CData) -> cffi.CData:
        ...

    def loadmus(self, filename: cffi.CData) -> cffi.CData:
        ...

    def loadmod(self, filename: cffi.CData) -> cffi.CData:
        ...

    def loadopb(self, filename: cffi.CData) -> cffi.CData:
        ...

    def createmus(self, data: cffi.CData, size: int) -> cffi.CData:
        ...

    def playmusic(self, music: cffi.CData, loop: int, volume: int) -> None:
        ...

    def stopmusic(self) -> None:
        ...

    def musicplaying(self) -> int:
        ...

    def musicvolume(self, volume: int) -> None:
        ...

    def setsoundmode(self, mode: int) -> None:
        ...

    def loadwav(self, filename: cffi.CData) -> cffi.CData:
        ...

    def createsound(self, channels: int, samplerate: int, framecount: int,
                    samples: cffi.CData) -> cffi.CData:
        ...

    def playsound(self, channel: int, sound: cffi.CData, loop: int,
                  volume: int) -> None:
        ...

    def stopsound(self, channel: int) -> None:
        ...

    def soundplaying(self, channel: int) -> int:
        ...

    def soundvolume(self, channel: int, left: int, right: int) -> None:
        ...

    def keystate(self, key: int) -> int:
        ...

    def readkeys(self) -> cffi.CData:
        ...

    def readchars(self) -> cffi.CData:
        ...

    def mousex(self) -> int:
        ...

    def mousey(self) -> int:
        ...

    def mouserelx(self) -> int:
        ...

    def mouserely(self) -> int:
        ...


lib: Lib
