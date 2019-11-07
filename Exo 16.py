#DEFINITIONS
def distance_hamming(mot1,mot2):
    if len(mot1) == len(mot2): #On regarde d'abord si les mots sont de même taille pour prévenir les erreurs
        mot1 = mot1.upper()#on mets les mots en majuscule pour que toutes les lettres soient identiques (a != A)
        mot2 = mot2.upper()
        distance = 0 #On initialise la distance à 0
        for i in range(0,len(mot1)): #pour i allant de 0 à la taille de la chaine, #si la ième lettre des deux mots sont différentes, on incrémente la distance de 1
            if mot1[i] != mot2[i]:
                distance+=1
        print(distance)
    else:
        print("mots pas de la même taille")

#CORPS DU PROGRAMME
distance_hamming("japon","savON") #on appelle la fonction avec les deux mots à tester