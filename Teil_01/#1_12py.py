from random import shuffle

liste = "amazing blazing stunning bold tremendous fantastic phenomenal delightful \
         ambitious exciting staggering outstanding smarter gorgeous best massive \
         incredible spectacular magical revolutionary intuitive profound screaming fast \
         beautiful jaw-dropping".upper().split()

shuffle(liste)

# Von der innersten Schleife anfange zu lesen!
# Innerste: viermal "SPAM" in eine Zeile mit Leerschritt, danach mit print() in die nächste Zeile
# Mitlere: die nachfolgende Schleife = eine Zeile zweimal
# Erste: nach den beiden Schleifen ein Zeile anhängen mit Wörtern aus der Liste.
# "liste.pop()" nimmt gibt die Liste um einen Eintrag reduziert  zurück.
for strophe in range(5): 
    for n in range(2):  
        for i in range(4):
            print("SPAM", end =" ") 
        print()
    
    el1 = liste.pop()
    el2 = liste.pop()
    
    print("{} SPAM, {} SPAM".format(el1,el2))
    print()