# Source: https://en.wikipedia.org/wiki/Code_page_437#Character_set
CP437 = ('\u0000☺☻♥♦♣♠•◘○◙♂♀♪♫☼'
         '►◄↕‼¶§▬↨↑↓→←∟↔▲▼'
         ' !"#$%&\'()*+,-./'
         '0123456789:;<=>?'
         '@ABCDEFGHIJKLMNO'
         'PQRSTUVWXYZ[\\]^_'
         '`abcdefghijklmno'
         'pqrstuvwxyz{|}~⌂'
         'ÇüéâäàåçêëèïîìÄÅ'
         'ÉæÆôöòûùÿÖÜ¢£¥₧ƒ'
         'áíóúñÑªº¿⌐¬½¼¡«»'
         '░▒▓│┤╡╢╖╕╣║╗╝╜╛┐'
         '└┴┬├─┼╞╟╚╔╩╦╠═╬╧'
         '╨╤╥╙╘╒╓╫╪┘┌█▄▌▐▀'
         'αßΓπΣσµτΦΘΩδ∞φε∩'
         '≡±≥≤⌠⌡÷≈°∙·√ⁿ²■\u00a0')

# Thanks for making me specify the endianness of 1 byte, Python
ENCODING = {CP437[i]: i.to_bytes(1, 'little') for i in range(256)}
