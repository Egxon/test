#
#Documentation :
#
#La librairie « re » permet de faire du Regex (Comme ce que nous avons vu en unix avec grep. Par exemple : [^.open*e$] va rechercher toutes chaînes commencant par un caractère quelconque (.) suivit par open et une suite quelconque (*) et se termine par e (e$)).
#
#Ici,
#	\S représente un caractère quelconque différent d'un espace.
#	\s représente un espace.
#
#Ainsi, r'([\S])\s([\S])' (r'' étant la syntaxe pour une chaîne en Regex) va cherche dans la chaîne de caractères, une suite de caractères de la forme "l a" ou "1 ?"...
#
#La deuxième partie : r'\1\2' permet de ne pas remplacer les caractères \1 et \2 qui ne sont pas les espaces (\S\S).
#
#Enfin, « phrase » est la chaîne de caractères en entrée.
#

import re

phrase = input("Entrez une phrase : ")

def spaces(string):
  return re.sub(r'([\S])\s([\S])',r'\1\2',phrase)

print(spaces(phrase))
