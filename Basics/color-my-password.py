## Сгенерировать случайный пароль, учитывая необходимость или ее отсутствие
## для добавления заглавных букв и спецсимволов.
## Вывести, раскрасив шрифты с помощью библиотеки colorama

from colorama import Fore
print (Fore.BLUE,'Hello World!')

import colorama
import random

def generate_password(length,case=False,special=False):
   simple_chars='sdfbvdsfnbvafngbvadsfddhgwoerzmagndofgapkjkndfv'
   case_chars='QWERTYUIOPASDFGHJKZXCVBNM'
   special_chars='!@#$%^&%(){:"}>?'
   chars = simple_chars
   password = ''
   if case:
       chars+=case_chars
   if special:
       chars+=special_chars
   for i in range(length):
       password+=random.choice(chars)
   return password

print (colorama.Fore.CYAN,generate_password(8))
print (colorama.Fore.RED,generate_password(10,True,True))