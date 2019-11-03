from datetime import datetime

EN_TO_MORSE_DICT = {
	'a':'.-',
	'b':'-...',
	'c':'-.-.',
	'd':'-..',
	'e':'.',
	'f':'..-.',
	'g':'--.',
	'h':'....',
	'i':'..',
	'j':'.---',
	'k':'-.-',
	'l':'.-..',
	'm':'--',
	'n':'-.',
	'o':'---',
	'p':'.--.',
	'q':'--.-',
	'r':'.-.',
	's':'...',
	't':'-',
	'u':'..-',
	'v':'...-',
	'w':'.--',
	'x':'-..-',
	'y':'-.--',
	'z':'--..',
	'-':'-....-',
	';': '−·−·−·',
	' ':' / ',
	'.': '.-.-.-',
}

MORSE_TO_EN_DICT = {v: k for k, v in EN_TO_MORSE_DICT.items()}
pause = ' ';

def encode_word(word):
	return pause.join(map(EN_TO_MORSE_DICT.get, word))

def decode_word(word):
	return ''.join(map(MORSE_TO_EN_DICT.get, word.split(pause)))

def encode_text(text):
	return EN_TO_MORSE_DICT[' '].join(map(encode_word, text.split()))

def decode_text(text):
	return ' '.join(map(decode_word, text.split(EN_TO_MORSE_DICT[' '])))
