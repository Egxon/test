"""
Replace single space to nothing.
If the string has two or more than two spaces, then do nothing.
:param string : string to edit
:return : edited string with modifications
"""


def erase(string):
    chaine = ""
    for i in range(len(string)):
        # Vérifie si le dernier élément de la chaîne est un espace, si oui alors on le retire sinon on l'ajoute.
        if i == len(string) - 1 and string[i] == " ":
            if string[i] == " ":
                chaine += ""
            else:
                chaine += string[-1]
            break

        if string[i] != " ":
            chaine += string[i]
        # Y a-t-il deux espaces ou plus ?
        elif (string[i] == " " and string[i + 1]) == " " or (string[i] == " " and string[i - 1] == " "):
            chaine += string[i]
        else:
            chaine += ""
    return chaine


thomas = erase("F als    ima  gne")
print(thomas)
