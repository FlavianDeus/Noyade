#DEFINITIONS

#on défini les segments ADN à tester
coupable1 = "CATA"
coupable2 = "ATGC"

#On défini les suspects à analyser
mout = ["Colonel Moutarde","CCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGCADN"]
rose = ["Mlle Rose","CTCCTGATGCTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGADN"]
perv = ["Mme Pervenche","AAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGTACTCCGCGCGCCGGGACAGAATGCCAD"]
lebl = ["M. Leblanc","CTGCAGGAACTTCTTCTGGAAGTACTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAG"]

#On défini une fonction qui permet de tester l'ADN sur un suspect avec comme argument le code ADN de ce dernier
def test_adn(suspect):

    if coupable1 in suspect and coupable2 in suspect: #si les deux segments se retrouvent dans l'ADN du suspect, on retourne coupable
        return "coupable"

    else: #sinon on retourne innocent
        return "innocent"

#CORPS DU PROGRAMME

#On teste les suspects un par un et affiche leurs résultats
print(mout[0] + " semble : " + test_adn(mout[1]))
print(rose[0] + " semble : " + test_adn(rose[1]))
print(perv[0] + " semble : " + test_adn(perv[1]))
print(lebl[0] + " semble : " + test_adn(lebl[1]))