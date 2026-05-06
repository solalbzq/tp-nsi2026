from ascii import *
from qrcode import *

def bin2dec(t):
    """
    Convertie le tuple correspondant à un nombre binaire en nombre de base de 10
    :param t:(tuple), "un tuple correspondant à un nombre binaire"
    :return:(int), " un nombre entier en base de 10"
    
    Exemple:
    >>> bin2dec((0,1,1,0,0,0,0,1))
    97
    """
    assert isinstance(t,tuple),"t dois etre un tuple"
    for elem in t:
        assert elem==1 or elem==0 ,"les elements doivent etre compris entre 1 et 0"
    res = 0
    j=len(t)-1
    for elem in t:
        if elem == 0:
            j-=1
        else:
            res += 2**j
            j-=1
    return res


def qrcode2dec(q):
    """
    Renvoie une liste d'entier décimaux
    :param q:(list),"une liste de tuples représentant un QR code"
    :return:(list),"une liste d'entier décimaux correspondant aux lignes du QR code"
    """
    l=[]
    for i in range (len(q)):
        l.append(bin2dec(q[i]))
    return l

# les entiers doivent être compris entre 0 et 127

def dec2str(liste_dec):
    """ entrée: liste d'entiers décimaux
        sortie: chaine de caractère formée des caractères correspondant
        de la table ascii """
    table_ascii = ascii.dict_ascii
    chaine = ""
    for entier in liste_dec:
        chaine += table_ascii.get(entier, "?")
    return chaine

def test_dec2str():
    """ Teste la fonction dec2str avec des données issues du module fourni """
    tests = [ascii.test1, ascii.test2, ascii.test3]
    for test in tests:
        print(dec2str(test))

def qrcode2str(qrcode):
    return dec2str(qrcode2dec(qrcode))

def str2qrcode(message):
    """
    Convertit une chaine de caractères en liste de tuples binaires.
    """
    qrcode = []
    table_inverse = {valeur: cle for cle, valeur in ascii.dict_ascii.items()}

    for caractere in message:
        entier = table_inverse.get(caractere, 63)
        binaire_str = bin(entier)[2:]
        ligne = tuple(int(bit) for bit in binaire_str)
        qrcode.append(ligne)
        
    return qrcode
