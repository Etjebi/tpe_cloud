# VERIFICATION DE L'OTENTICITE D'UNE ADRESSE IP

# definition de la fonction
def est_adresse_ip_valide(adresse_ip):
# on divise la dresse ip en 4 par un point (.)
    parties= adresse_ip.split(".")
# on verifie si la somme des parties obtenue et differente de 4
    if len(parties) != 4:
        return False
#on verifie si l'adresse est constituee de chiffres et est compride entre 0 et 255
    for partie in parties:
        if not partie.isdigit() or int(partie) > 255 or int(partie) < 0:
            return False
    return True

#ON ENTRE L'ADRESSE
adresse_ip=input("entrez une adresse_ip:")
# ON APPEL LA FONCTION
print(est_adresse_ip_valide(adresse_ip))
