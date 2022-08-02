#!/usr/bin/env python
import pathlib

import cffi

lib_dir = pathlib.Path(__file__).parent / '..' / 'libs' / 'dos-like' / 'source'

ffibuilder = cffi.FFI()
ffibuilder.set_source_pkgconfig(
    'dos_like._dos',
    ['sdl2'],
    """\
    #define DOS_IMPLEMENTATION
    #include "dos.h"

    static int _pydosmain(int, char **);

    int dosmain(int argc, char **argv) {
        return _pydosmain(argc, argv);
    }
    """,
    include_dirs=[lib_dir],
    libraries=['GLEW', 'GL', 'm', 'pthread'],
    # Uncomment if gdb is needed:
    # extra_compile_args=['-g', '-O0'],
    define_macros=[('NO_MAIN_DEF', '1')],
)
ffibuilder.cdef("""\
    // Define this in python to be called by the C dosmain().
    extern "Python" int _pydosmain(int argc, char **argv);
    
    // dos-like is designed as an executable, so just expose its main function to the API.
    int main(int argc, char **argv);

    // 8< 8< 8< 8< 8< 8< 8< 8< 8< 8<  START COPY PASTE  8< 8< 8< 8< 8< 8< 8< 8< 8< 8<

    enum videomode_t {
        videomode_40x25_8x8,
        videomode_40x25_9x16,
        videomode_80x25_8x8,
        videomode_80x25_8x16,
        videomode_80x25_9x16,
        videomode_80x43_8x8,
        videomode_80x50_8x8,
        videomode_320x200,
        videomode_320x240,
        videomode_320x400,
        videomode_640x200,
        videomode_640x350,
        videomode_640x400,
        videomode_640x480,
    };

    void setvideomode( enum videomode_t mode );
    void setdoublebuffer( int enabled );
    int screenwidth( void );
    int screenheight( void );
    unsigned char* screenbuffer( void );
    unsigned char* swapbuffers( void );
    void waitvbl( void );
    void setpal( int index, int r, int g, int b );
    void getpal( int index, int* r, int* g, int* b );
    
    int shuttingdown( void );
    
    
    void cputs( char const* string );
    void textcolor( int color );
    void textbackground( int color );
    void gotoxy( int x, int y );
    int wherex( void );
    int wherey( void );
    void clrscr( void );
    void curson( void );
    void cursoff( void );
    
    unsigned char* loadgif( char const* filename, int* width, int* height, int* palcount, unsigned char palette[ 768 ] );
    
    void blit( int x, int y, unsigned char* source, int width, int height, int srcx, int srcy, int srcw, int srch );
    void maskblit( int x, int y, unsigned char* source, int width, int height, int srcx, int srcy, int srcw, int srch, 
        int colorkey );
    
    void clearscreen( void );
    int getpixel( int x, int y );
    void hline( int x, int y, int len, int color );
    void putpixel( int x, int y, int color );
    
    void setdrawtarget( unsigned char* pixels, int width, int height );
    void resetdrawtarget( void );
    
    void setcolor( int color );
    int getcolor( void );
    void line( int x1, int y1, int x2, int y2 );
    void rectangle( int x, int y, int w, int h );
    void bar( int x, int y, int w, int h );
    void circle( int x, int y, int r );
    void fillcircle( int x, int y, int r );
    void ellipse( int x, int y, int rx, int ry );
    void fillellipse( int x, int y, int rx, int ry );
    void drawpoly( int* points_xy, int count );
    void fillpoly( int* points_xy, int count );
    void floodfill( int x, int y );
    void boundaryfill( int x, int y, int boundary );
    
    void outtextxy( int x, int y, char const* text ); 
    void wraptextxy( int x, int y, char const* text, int width ); 
    void centertextxy( int x, int y, char const* text, int width ); 
    
    enum {
        DEFAULT_FONT_8X8  = 1,
        DEFAULT_FONT_8X16 = 2,
        DEFAULT_FONT_9X16 = 3,
    };
    
    void settextstyle( int font, int bold, int italic, int underline );
    int installuserfont( char const* filename ); 
    
    
    enum {
        DEFAULT_SOUNDBANK_AWE32 = 1,
        DEFAULT_SOUNDBANK_SB16  = 2,
    };
    
    void setsoundbank( int soundbank );
    int installusersoundbank( char const* filename );
    
    #define MUSIC_CHANNELS 16 
    void noteon( int channel, int note, int velocity);
    void noteoff( int channel, int note );
    void allnotesoff( int channel );
    void setinstrument( int channel, int instrument );
    
    struct music_t;
    struct music_t* loadmid( char const* filename );
    struct music_t* loadmus( char const* filename );
    struct music_t* loadmod( char const* filename );
    struct music_t* loadopb( char const* filename );
    struct music_t* createmus( void* data, int size );
    void playmusic( struct music_t* music, int loop, int volume );
    void stopmusic( void );
    int musicplaying( void );
    void musicvolume( int volume );
    
    enum soundmode_t {
        soundmode_8bit_mono_5000,
        soundmode_8bit_mono_8000,
        soundmode_8bit_mono_11025,
        soundmode_8bit_mono_16000,
        soundmode_8bit_mono_22050,
        soundmode_8bit_mono_32000,
        soundmode_8bit_mono_44100,
        soundmode_16bit_mono_5000,
        soundmode_16bit_mono_8000,
        soundmode_16bit_mono_11025,
        soundmode_16bit_mono_16000,
        soundmode_16bit_mono_22050,
        soundmode_16bit_mono_32000,
        soundmode_16bit_mono_44100,
        soundmode_8bit_stereo_5000,
        soundmode_8bit_stereo_8000,
        soundmode_8bit_stereo_11025,
        soundmode_8bit_stereo_16000,
        soundmode_8bit_stereo_22050,
        soundmode_8bit_stereo_32000,
        soundmode_8bit_stereo_44100,
        soundmode_16bit_stereo_5000,
        soundmode_16bit_stereo_8000,
        soundmode_16bit_stereo_11025,
        soundmode_16bit_stereo_16000,
        soundmode_16bit_stereo_22050,
        soundmode_16bit_stereo_32000,
        soundmode_16bit_stereo_44100,
    };
    
    void setsoundmode( enum soundmode_t mode );
    
    #define SOUND_CHANNELS 16
    struct sound_t;
    struct sound_t* loadwav( char const* filename );
    struct sound_t* createsound( int channels, int samplerate, int framecount, short* samples );
    void playsound( int channel, struct sound_t* sound, int loop, int volume );
    void stopsound( int channel );
    int soundplaying( int channel );
    void soundvolume( int channel, int left, int right );
    
    enum keycode_t { 
        KEY_INVALID, KEY_LBUTTON, KEY_RBUTTON, KEY_CANCEL, KEY_MBUTTON, KEY_XBUTTON1, KEY_XBUTTON2, KEY_BACK, KEY_TAB, 
        KEY_CLEAR, KEY_RETURN, KEY_SHIFT, KEY_CONTROL, KEY_MENU, KEY_PAUSE, KEY_CAPITAL, KEY_KANA, KEY_HANGUL = KEY_KANA,
        KEY_JUNJA, KEY_FINAL, KEY_HANJA, KEY_KANJI = KEY_HANJA, KEY_ESCAPE, KEY_CONVERT, KEY_NONCONVERT, KEY_ACCEPT, 
        KEY_MODECHANGE, KEY_SPACE, KEY_PRIOR, KEY_NEXT, KEY_END, KEY_HOME, KEY_LEFT, KEY_UP, KEY_RIGHT, KEY_DOWN, 
        KEY_SELECT, KEY_PRINT, KEY_EXEC, KEY_SNAPSHOT, KEY_INSERT, KEY_DELETE, KEY_HELP, KEY_0, KEY_1, KEY_2, KEY_3, KEY_4, 
        KEY_5, KEY_6, KEY_7, KEY_8, KEY_9, KEY_A, KEY_B, KEY_C, KEY_D, KEY_E, KEY_F, KEY_G, KEY_H, KEY_I, KEY_J, KEY_K, 
        KEY_L, KEY_M, KEY_N, KEY_O, KEY_P, KEY_Q, KEY_R, KEY_S, KEY_T, KEY_U, KEY_V, KEY_W, KEY_X, KEY_Y, KEY_Z, KEY_LWIN, 
        KEY_RWIN, KEY_APPS, KEY_SLEEP, KEY_NUMPAD0, KEY_NUMPAD1, KEY_NUMPAD2, KEY_NUMPAD3, KEY_NUMPAD4, KEY_NUMPAD5, 
        KEY_NUMPAD6, KEY_NUMPAD7, KEY_NUMPAD8, KEY_NUMPAD9, KEY_MULTIPLY, KEY_ADD, KEY_SEPARATOR, KEY_SUBTRACT, KEY_DECIMAL, 
        KEY_DIVIDE, KEY_F1, KEY_F2, KEY_F3, KEY_F4, KEY_F5, KEY_F6, KEY_F7, KEY_F8, KEY_F9, KEY_F10, KEY_F11, KEY_F12, 
        KEY_F13, KEY_F14, KEY_F15, KEY_F16, KEY_F17, KEY_F18, KEY_F19, KEY_F20, KEY_F21, KEY_F22, KEY_F23, KEY_F24, 
        KEY_NUMLOCK, KEY_SCROLL, KEY_LSHIFT, KEY_RSHIFT, KEY_LCONTROL, KEY_RCONTROL, KEY_LMENU, KEY_RMENU, KEY_BROWSER_BACK, 
        KEY_BROWSER_FORWARD, KEY_BROWSER_REFRESH, KEY_BROWSER_STOP, KEY_BROWSER_SEARCH, KEY_BROWSER_FAVORITES, 
        KEY_BROWSER_HOME, KEY_VOLUME_MUTE, KEY_VOLUME_DOWN, KEY_VOLUME_UP, KEY_MEDIA_NEXT_TRACK, KEY_MEDIA_PREV_TRACK, 
        KEY_MEDIA_STOP, KEY_MEDIA_PLAY_PAUSE, KEY_LAUNCH_MAIL, KEY_LAUNCH_MEDIA_SELECT, KEY_LAUNCH_APP1, KEY_LAUNCH_APP2, 
        KEY_OEM_1, KEY_OEM_PLUS, KEY_OEM_COMMA, KEY_OEM_MINUS, KEY_OEM_PERIOD, KEY_OEM_2, KEY_OEM_3, KEY_OEM_4, KEY_OEM_5, 
        KEY_OEM_6, KEY_OEM_7, KEY_OEM_8, KEY_OEM_102, KEY_PROCESSKEY, KEY_ATTN, KEY_CRSEL, KEY_EXSEL, KEY_EREOF, KEY_PLAY, 
        KEY_ZOOM, KEY_NONAME, KEY_PA1, KEY_OEM_CLEAR, 
        KEYCOUNT, KEYPADDING = 0xFFFFFFFF 
    };
    
    #define KEY_MODIFIER_RELEASED 0x80000000
    int keystate( enum keycode_t key );
    enum keycode_t* readkeys( void );
    char const* readchars( void );
    
    int mousex( void );
    int mousey( void );
    int mouserelx( void );
    int mouserely( void );
""")

if __name__ == '__main__':
    ffibuilder.compile(verbose=True)
