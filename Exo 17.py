#DEFINITIONS

import os #On importe la bibliothèque os pour faire des pauses dans le programme

def palindrome(mot): #fonction qui teste si un mot est un palindrome ou non
    mot = mot.upper() #on met tout en majuscule pour éviter les faux négatif, parce que "K" est différent de "k" donc "Kayak" n'est pas un palindrome

    moitie_taille = int(len(mot)/2)   # on divise la taille en deux
    test_lapindrome = 0 #on défini une variable témoin qui dire si on est en présence d'un palindrome ou non

    for i in range(0,moitie_taille):

        if mot[i] != mot[len(mot)-i-1]:#si une lettre et son symetrique par rapport au milieu du mot sont différentes, la variable témoin augmente et on casse la boucle
            test_lapindrome +=1
            break
    if test_lapindrome != 0: #si la variable témoin est différente de 0
        print(" ")
        print(mot + " n'est pas un palindrome")# alors on affiche que le mot n'est pas un palindrome
        os.system("pause") #et on mets une pause dans le programme pour que l'utilisateur puisse voir la réponse
    else : #sinon
        print(" ")
        print(mot + " est un palindrome") #on dit que c'est un palindrome
        os.system("pause") #et on met aussi une pause pour la même raison


#CORPS DU PROGRAMME

while True : #on fait une boucle infinie
    #affichage d'un menu
    print("Ce programme vérifie si un mot est un palindrome ou non.")
    print("1 - tester un mot")
    print("2 - Quitter")
    entree = input("Que voulez vous faire ? : ")

    if entree == "1": #si l'utilisateur tape "1"
        palindrome(input("Entrez le mot à tester : ")) #on lui demande d'entrer le mot qu'il veut tester, la valeur qu'il rentre sera l'argument lors de l'appel de la fonction palindrome()

    elif entree == "2": #sinon si l'utilisateur tape "2"
        print("Fin du programme, au revoir")
        break #On quitte la boucle et donc fini le programme

    else: #si il n'a rentré ni "1" ni "2"
        print(" ")
        print("entrée invalide, réessayez") #on lui demande de rentrer une valeur correcte
        print(" ")