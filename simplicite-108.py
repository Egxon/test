# return string without spaces
def erase(cc):

    compteurEspace = 0
    chaine = ""

    # on parcours la chaine de caractère lettre à lettre
    for k in cc :

        # boucle pour check les espaces
        if (k == " ") :
            compteurEspace = compteurEspace+1
        else:
            compteurEspace = 0

        # boucle de remplacement des caractères
        
        if (compteurEspace == 0) :
            chaine = chaine + k
        elif (compteurEspace == 2) :
            chaine = chaine + "  "
        
        #print(k)
        #print(compteurEspace)

    print(chaine)





erase(' Y e s  j e   µ f)à ')
