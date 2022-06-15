#include <stdio.h>
#include <string.h>

/*
 * Supprime les caractères espace seuls, non groupés, dans la chaîne
 * de caractères src_text et retourne la chaîne traitée dans dest_text.
 * Chacune des cahîne est parcourue par un indice différent, qui permet
 * de supprimer les espaces.
 */
void remove_solo_spaces(char *src_text, char *dest_text) {

	/* Longueur de la chaine à traiter */
	int length = strlen(src_text);

	/* Indice du caractère sur la chaîne à traiter src_text */
	int i_src = 0;

	/* Indice du caractère sur la chaîne traitée dest_text */
	int i_dest = 0;

	/* Parcours de la chaine à traiter */
	while (i_src < length) {

		/* Si le caractère n'est pas un espace ou si c'est le dernier */
		if ((src_text[i_src] != ' ') || (i_src == length - 1)) {
			/* Il est copié dans la chaine destination */
			dest_text[i_dest] = src_text[i_src];
			/* On avance les deux indices de position */
			i_src++;
			i_dest++;
		}

		/* Sinon c'est un espace et il n'est pas le dernier caractère */
		else {
			/* Si le caractère suivant n'est pas un espace (espace seul) */
			if (src_text[i_src + 1] != ' ') {
				/* On ne le copie pas dans la chaîne destination */
				/* et on avance seulement l'indice de la source */
				i_src++;
			}
			/* Sinon le caractère suivant est aussi un espace */
			else {
				/* On avance dans la chaîne source tant que les caractères
				   lus sont des espaces ou que l'on n'est pas en fin de chaîne */
				while ((src_text[i_src] == ' ') && (i_src != length - 1)) {
					/* Le caractère est copié dans la chaîne de destination */
					dest_text[i_dest] = src_text[i_src];
					/* On avance les deux indices de position */
					i_src++;
					i_dest++;
				}
			}
		}

	}

}
