
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 10 08:25:45 2025

@author: argoud
"""
from personnage import personnage
from personnage import ennemy
import random



porte=ennemy("porte", "", 20)
a=0
b=0
c=0
d=0
e=0
f=0
g=0
h=0
i=0
j=0
k=0
l=0
m=0
n=0
o=0
p=0
q=0
r=0
s=0
t=0
u=0
v=0
w=0
x=0
y=0
z=0
aa=0
ab=0
ac=0
ad=0
ae=0
af=0
fightportetuto=0
fighton=0





"""
----------
FONCTIONS
----------
"""
""" intro du combat"""

def bagarrh(ennemi):
    fighton=1
    aleatoire=random.randint(1,5)
    print("---------------")
    if aleatoire==1:
        print("Un",ennemi.nom,"sauvage apparaît!\n")
    elif aleatoire==2:
        print(ennemi.nom,"veut te voler ton goûter!\n")
    elif aleatoire==3:
        print(ennemi.nom,"te barre la route!\n")
    else:
        print(ennemi.nom,"veut se battre!\n")

    """instauration du combat au tour par tour"""        
    while fighton==1: #tant que le combat dure
        choixfight=0
        print("Que voulez vous faire?\n")
        while choixfight!="attaquer" and choixfight!="ATTAQUER" and choixfight!="objets" and choixfight!="OBJETS" and choixfight!="menacer" and choixfight!="MENACER":    
            choixfight=input("- ATTAQUER -\n- OBJETS -\n- MENACER -\n_")
            if choixfight=="attaquer" or choixfight=="ATTAQUER":
                print("...")
    
            pass


"""
----------
PLOT
----------
"""




mc=personnage("Nom", "Spé", "Spé2", 0, 0, "arme", 20)

while a!="":
    a=input("PRESS START TO PLAY\n")
    if a=="":            
        while b!="": 
            b=input("blobloblo blebleble bloubloublou...\n utilise la touche START pour avancer dans le jeu...\n")
            if b=="":
                print("Tu te retrouves enfermé dans le lycée car à cause du proviseur, tout le monde est devenu fou...")
                print("\nUn conseil... ne te fies pas trop aux gens ils pourraient te traillir...")
                while u!="":
                    u=input("...")
                print("Dans ce jeu ton but sera de sortir du lycée... bonne chance à toi ...")
                while v!="":
                    v=input("")
                while d!="":
                    mc.nom=input("Ton nom: _")
                    print(mc.nom,"! Quel nom de merde! tant pis, on va faire avec.")
                    
                    print("Quelles sont tes spécialités ay lycée: ")
                    mc.spe1=input("Spé 1: _")
                    mc.spe2=input("Spé 2: _")
                    print(mc.spe1, mc.spe2, "? Tu comptes rater votre vie avec ça?")
                    
                    mc.pointure=int(input("Ta pointure: _"))
                    if mc.pointure>=40:
                        print(mc.pointure, "! C'est quoi ces pieds de salopard!")
                    else:
                        print(mc.pointure, "! ah ouaiss le petit poucet")
                    
                    mc.age=int(input("Ton âge: _"))
                    if mc.age>=17:
                        print("Oh le vieux croûton!")
                    else:
                        print("Un gros bébé cadum...")
                    d=""
                    
                while e!="":
                    e=input("...")
                while c!="Stylo" and c!="Clavier" and c!="Table" and c!="stylo" and c!="clavier" and c!="table":
                    print("Bonjour ",mc.nom,", Le jeu se déroule dans le lycée Monte Cristo.\nVous rencontrerez plusieurs ennemis que vous devrez affronter pour avancer.\n")
                    print("Tu apparais dans la salle P201.\nTu es accueilli par M. Arnaud qui te propose de choisir une arme pour te défendre:")
                    c=input("Tu as le choix entre:\n- Stylo -\n- Clavier -\n- Table -\nQuelle arme choisis-tu? _")
                    if c=="Stylo" or c=="stylo":
                        mc.arme="stylo"
                    elif c=="Clavier" or c=="clavier":
                        mc.arme="clavier"
                    elif c=="Table" or c=="table":
                        mc.arme="table"
                        
                    print("Tu as choisi",mc.arme,"! Excellent choix")
                while f!="":
                    f=input("...")
                while g!="":
                    g=input("Tu dois à présent sortir de la salle...")
                while fightportetuto!="":
                    fightportetuto=input("Une porte te barre la route! Prépares-toi au combat!")
                #bagarrh(porte)
                while h!="Gauche" and h!="Droite" and h!="Devant" and h!="gauche" and h!="droite" and h!="devant":
                    print("Tu viens de gagner ton premier combat un choix de direction s'offre à toi")
                    h=input("choisis entre :\n-Gauche-\n-Droite-\n-Devant-\n:_")
                    if h=="Gauche" or h=="gauche":
                        print("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _","\n","\nC'est un bon choix tu te retrouves dans un escalier, attention à toi, tu pourrais y croiser des gens qui ne te veulent pas forcément du bien")
                    elif h=="Droite" or h=="droite":
                        print("un choix un peu risqué tu es maintenant dans un ascenceur ")
                    elif h=="Devant" or h=="devant":
                        print("un choix un peu risqué tu es maintenant dans un ascenceur ")
                    while ac!="":
                        ac=input("...")
                    if h=="Gauche" or h=="gauche":
                        print("Tu descends les escaliers et te retrouve au Premier étage..." )
                        while j!="":
                            j=input("")
                        print("\naaaaaaaaaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAaaaaaaaaaaaaaaAAAAAAAAAAAhhhhhhhHHHHHHHHHHHHH y'a kelkun")
                        print("\nc koi tie ki ? ...")
                        while k!="":
                            k=input("")
                        print("ah non c'est Madame Eger :)\nElle te dropp un dictionnaire")
                        while l!="":
                            l=input("")
                        print("\ntu dois maintenant faire un choix entre garder ton arme qui est ", mc.arme, "ou accepter le disctionnaire")
                        while m!="":
                            m=input("")
                        i=input("tu prends le dictionnaire?\n-Oui-\n-Non-\nQue choisis tu?: _")
                        if i=="OUI" or i=="oui":
                            mc.arme="dictionaire"
                            print("Ta nouvelle arme est donc ",mc.arme)
                        else:
                            mc.arme=c
                            print("ton arme est donc toujours",mc.arme)
                        while n!="":
                            n=input("")
                        print("Apres avoir croisé Madame Eger tu continues ta route,","\ntu te retrouves au premier etage dans le batiment principal")
                        #check point
                        while r!="":
                            r=input("...")
                        print("\nTu arrives devant des toilettes veux-tu rentrer ou continuer ta route")
                        while p!="":
                            p=input("...")
                        while o!= "Oui je rentre" and o!="oui je rentre" and o!="oui" and o!="Oui" and o!="Non" and o!="non":
                            o=input("Tu rentres ????\n-Oui je rentre-\n-Non-\nQue choisi tu?:_")
                            if o=="Oui je rentre" or o=="oui je rentre" or o=="oui" or o=="Oui":
                                print("\nTu te retrouves maintenant contre un monstre caca prépares toi à combattre")
                                #bagarrh(Montre_caca)
                            else:
                                print("\nTu continues donc ta route et tu croises par hasard Jeremy maxi ora")
                                #bagarrh(Jeremy_maxi_ora)
                        print("Bravo tu as gagné ton combat contre tu ressors encore victorieux")#print le ne de l'enemie apres contre 
                    elif h=="Droite" or h=="droite" or h=="Devant" or "devant":
                        print(" Oh My Dog !!!!! l'ascenseur est plein, tu vas devoir te battre avec ceux qui sont arrivés avant toi pour espèrer avoir une place")
                        #bagarrh(bloes)
                        while q!="":
                            q=input("")
                        print("l'ascenseur a eu un probleme il t'as téléporté jusqu'au batiment scientifique ")
                        while s!="":
                            s=input("...")
                        print("\nApres avoir un peu marché dans le batiment scientifique tu vois une classe ouverte ")
                        print("je ne t'influence pas mais tu devrait rentrer")
                        while y!="":
                            y=input("...")
                        while t!= "Oui je vous écoute" and t!="oui vous écoute" and t!="oui" and t!="Oui" and t!="Non je m'en fous de ton avis" and o!="non je m'en fous de ton avis":
                            t=input("\nQue décide tu ??\n-Oui je vous écoute-\n-Non je m'en fous de ton avis-\ntu veux faire quoi??:_")
                            if t=="Oui je vous écoute" or t=="oui je vous écoute" or t=="Oui" or t=="oui":
                              print("tu rencontres un nouveau personnage prépares toi à combattre!!!!!\n c'est Mr Blanchard")
                              print("c'est un grand moment d'émotion")#bagarrh(Mr_Blanchard)(#mettre une phrase de victoire)
                            else:
                                t=="Non je m'en fou" or t=="non je m'en fou" or t=="Non" or t=="non"
                                print("dommage pour toi tu manques un vrai truc")
                                print("\nTu entends de la salle 'c'est un grand moment d'émotion")
                            while z!="":
                                z=input("...")
                            print("Tu continues donc ton chemin..")
                            print ("Tu vois une autre salle ouverte..")
                            while w!="":
                                w=input("...")
                            print("\nTu décides de rentrer tu te rends compte que dans la salle se trouve Noah de nsi...")
                            while aa!="":
                                aa=input("...")
                            print("\nIl te propse de faire un combat (il est vraiment pas fort tu devrais le faire c'est de l'exp facile)")
                            while ab!="":
                                ab=input("...")
                            while x!="Oui je prend ce combat" and x!="oui je prend le combat" and x!="Oui" and x!="oui" and x!="Non" and x!="non" and x!="Non je m'en fou j'ai deja assez d'exp" and x!="non je m'en fou j'ai deja assez d'exp" :
                                x=input("Que veux-tu faire??\n-Oui je prend ce combat-\n-Non je m'en fou j'ai deja assez d'exp-\nOn fait quoi??:_ ")
                                if x=="Oui je prend ce combat" or x=="oui je prend ce combat" or x=="Oui" or x=="oui":
                                    print("c'est d'accord prépares toi à combatre(comme je t'ai dit sa va être simple )")
                                    #bagarrh(Noah_de_nsi)
                                    #mettre un message de victoire 
                                else :
                                    x=="Non je m'en fou j'ai deja assez d'exp" or x=="non je m'en fou j'ai deja assez d'exp" or x=="Non" or x=="non"
                                    print("Tampis pour toi c'était pourtant trés simple de gagner")
                            print("\nAu loin tu arrives à distinger un escalier tu décides de t'y diriger")
                            while ad!="":
                                ad=input("...")
                            print("arrivé à l'escalier tu vois que c'est un toboggan tu les prends alors a fond")
                            print("\nArriver en bas du tobagan tu as perdu un peut de vie parce que tu est arriver trop vite...")
                            while ae!="":
                                ae=input("")
                            print("Tu est juste a coter de la cantine tu te dit que a l'interieur il y a peut etre des potion pour se régénerer...")
                            print("\nTu rentre dans la cantine tu vas jusqu'a la cuisine et tu vois de la nouriture tu commence a manger mais attention deriere toi....")
                            while af!="":
                                af=input("")
                            print("deriere toi il y a Mr burger il va tattaquer dans pas longtemps prepare toi vite!!!!!")
                            #bagarrh(Mr_Burger)
                        