####################
# Océane Machado TD2 
# 22004369
#################################################################################################################################
#https://github.com/uvsq22004369/Projet_cryptanalyse.git
#################################################################################################################################
#Cryptanalyse

#Votre mission, si vous l'acceptez, est de déchiffrer 4 textes de difficulté croissante en vous aidant d'un programme 
#python que vous allez écrire.

#Les fichiers ont été cryptés avec des méthodes données en cours.
#Les fichiers chiffrés contiennent des textes en ASCII. Une fois déchiffrés ils vous donneront des informations.
#Vous devez vous baser sur les fréquences d'apparition des lettres en français (et des paires de lettres) pour casser les codes. 
#Faire une fonction de calcul pour vous aider.

#Penser à réutliser le code du td de cryptographie comme base de travail.

#Le code de votre programme doit être sur github et vous fournirez un lien vers votre projet github avec le code et le résultat 
#du décodage en le déposant sur Moodle avant le mercredi 12 mai.
#Une soutenance sera organisée le 17 mai.
################################################################################################################################
import tkinter as tk

texte1 = "kd oqnbgzhm ehbghdq ztqz tm bncd ozq rtarshstshnm zkogzadshptd: bgzptd kdssqd drs qdlokzbdd ozq tmd ztsqd. tshkhrdq kz eqdptdmbd cdr kdssqdr ontq cdbncdq kd ldrrzfd."
#pour dechifrer le texte1 copier coller le texte dans le label pour entrer le texte.
#entrer la clé : a
#cliquer sur dechifrer texte 1

#le prochain fichier aura un code par substitution alphabetique chaque lettre est remplacee par une autre: 
#utiliser la frequence des lettres pour decoder le message.

texte2 = "gx qosvlnkd wkvlkxo xiu vscx qno yd fsu cx qniix cx unkggx kdvsddyx xu vsdukxdu g'kdckvx. gxi gxuuoxi cy fsu cx qniix qxofxuuxdu cx cxvngxo gxi gxuuoxi cy fxiinmx sokmkdng fscygs 26. ixygxi gxi gxuuoxi cx n n a isdu vlkwwoxxi."
#pour dechifrer le texte2 copier coller le texte dans le label pour entrer le texte.
#il n'y a pas de clé a entré car il s'agit de substitution mais les lettres sont substituer ainsi :
#g=l, x=e, i=s, u=t, o=r, y=u, d=n, s=o, v=c, k=i, q=p, l=h, n=a, w=f, c=d, f=m, m=g, a=y
#cliquer sur dechifrer texte 2

#Le prochain fichier est codé par un mot de passe de taille inconnue et contient l'indice.
#Les lettres du mot de passe permettent dedécaler les lettres du message original modulo 26. 
# Seules les lettres de a à y sont chiffrées

texte3 = "dceuq e n'ehfp cg p'kyhhep uqfw cgiy citudm c gzudiq ni ezhd px c jhptv ep cggsht. kg hdtymdt xdzei gdx rzyq wir mvzxpw, cifcchdb znwd ccyw wy lkcsht, dp isgd uqfw wy ?"
#pour dechifrer le texte3 copier coller le texte dans le label pour entrer le texte.
#entrer la clé : xova
#les ' sont des z car celui-ci n'est pas coder
#cliquer sur dechifrer texte 3

#Bravo a l'aide de l'indice vous avez reussi a casser ce code et a finir ce devoir. 
#Le dernier texte est pour les braves, regardez vous dans un miroir, en etes vous un ?

texte4 = {"jeqeqecvnf suozvb jfk muj"
  "dfjr fmy rvuqsk ve"  
  "itajtd mifwz nnrt"  
  "imtrvp zuh srzmzbqz tepr zn"  
  "tmsnirt imtrvp nec hw"  
  "dzpqj tjf pdecpr zl jr"  
  "ptejnt ekpb iu b"  
  "iiuyu iy ijz surg rjs ttsn"  
  "votp ac hw rzpuen jozw"  
  "rvwdvx jbo nirscyjv fi"  
  "svmkyw ve iaflss yie te"  
  "teffvv'u riznxjzvv jfk"  
  "nelrhtjrk dh sivdvjvve"  
  "yi cvb à jffrds tdp"  
  "rvwdv sebr onvnqsy zvp"  
  "zuhjwiM le wmifo wiezib nec"  
  "triot qmjvr'c onrwz"  
  "memfqg srq wdaietsq vk"
}
#mettre le texte en mirroir : 

#jum kfj bvzous fnvceqeqej
#ev ksquvr ymf rjfd
#trnn zwfim dtjati
#nz rpet zqbzmzrs huz pvrtmi
#wh cen pvrtmi trinsmt
#rj lz rpcedp fjt jqpzd 
#b ui bpke tnjetp
#nstt sjr grus zji yi uyuii
#wzoj neupzr wh ca ptov
#if vjycsrin obj xvdwvr
#et eiy sslfai ev wykmvs
#kfj vvzjxnzir u'vvffet
#evvjvdvis hd krjthrlen
#pdt sdrffj à bvc iy
#pvz ysqnvno rbes vdwvr
#cen bizeiw ofimw el Miwjhuz
#zwrno c'rvjmq toirt
#kv qsteiadw qrs gqfmem  
    


alphabet=[]

def alphabet_vide():
    for i in range(97, 122) :
       alphabet.append([chr(i),0.0])

def vide():
    for x in alphabet :
        x[1]=0.0


alphabet_vide()



def rang(lettre) :
    return ord(lettre)-96

def decalage(lettre_message,lettre_cle):
    if  (97 <= ord(lettre_message)<= 122):
        return chr((rang(lettre_message) + rang(lettre_cle))%26 + 96)
    else:
        return lettre_message



def dec_texte(texte,cle):
    taille_cle = len(cle)
    res = ""
    for i in range(len(texte)):
        res+= decalage(texte[i],cle[i%taille_cle])
    return res


def dechiffre():
    resultat.delete(0, tk.END)
    if entree_texte.get() == "" or entree_cle.get() == "":
      resultat.insert(0, "Il manque quelque chose en entrée :/")
    resultat.insert(0, dec_texte(entree_texte.get(), entree_cle.get()))


def chiffre_xor(lettre_message,lettre_cle):
    return (chr(ord(lettre_message) ^ ord(lettre_cle)))


def decodage_substitution(texte):
    resultat.delete(0, tk.END)
    specialChars = "!#$%^&*()" 
    for specialChar in specialChars:
       texte = texte.replace(specialChar, "")
    print(texte) # A,Quick,brown,fox,jumped,over,the,lazy,dog
    texte = texte.replace(",", " ")
    print(texte) # A Quick brown fox jumped over the lazy dog
    for c in texte : 
       str.replace('x','e')
       str.replace('g','l')
       str.replace('i','s')
       str.replace('o','r')
       str.replace('u','t')
       str.replace('y','u')
       str.replace('d','n')
       str.replace('s','o')
       str.replace('v','c')
       str.replace('k','i')
       str.replace('q','p')
       str.replace('l','h')
       str.replace('n','a')
       str.replace('w','f')
       str.replace('c','d')
       str.replace('f','m')
       str.replace('m','g')
       str.replace('a','z')
    resultat.insert(0, dec_texte(entree_texte.get()))





racine=tk.Tk()
racine.title("Cryptographie")

entree_texte = tk.Entry(racine, width = 50, font = ("helvetica", "20"))
entree_texte.grid(row = 0, column = 0)

entree_cle = tk.Entry(racine, width = 50, font = ("helvetica", "20"))
entree_cle.grid(row = 1, column = 0)

label_texte = tk.Label(racine,font = ("helvetica", "20"), text = "Entrer le message ici.")
label_texte.grid(row = 0, column = 1)

label_cle = tk.Label(racine,font = ("helvetica", "20"), text = "Entrer la clé ici.")
label_cle.grid(row = 1, column = 1)

bouton_coder1=tk.Button(racine, text="dechiffrer texte 1",fg="black", width=15, command=dechiffre)
bouton_coder1.grid(row=2, column=0)

bouton_coder2=tk.Button(racine, text="dechiffrer texte 2",fg="black", width=15, command=decodage_substitution)
bouton_coder2.grid(row=3, column=0)

bouton_coder3=tk.Button(racine, text="dechiffrer texte 3",fg="black", width=15, command=dechiffre)
bouton_coder3.grid(row=4, column=0)

bouton_coder4=tk.Button(racine, text="dechiffrer texte 4",fg="black", width=15, command=dechiffre)
bouton_coder4.grid(row=5, column=0)

resultat=tk.Entry(racine,width = 50, font = ("helvetica", "20"))
resultat.grid(row=6,column=0)

label_res=tk.Label(racine,font = ("helvetica", "20"), text="Déchiffement ici.")
label_res.grid(row = 6, column=1)

racine.mainloop()