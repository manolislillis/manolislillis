def checknum(x):
    if (x.isalpha()):
        return True
    else:
        return False

def kainourgia(x):
    from string import ascii_letters

    if set(x).difference(ascii_letters):
        return True
    else:
        return False
    

keimeno=open("keimeno.txt","r")
j=0
k=0
for word in keimeno.read().split():
    j=0
    k=0
    proto=word[0]
    teleutaio=word[-1]
    if(kainourgia(proto)):
        word=word.replace(proto,"")

    if(kainourgia(teleutaio)):
        word=word.replace(teleutaio,"")

    if (checknum(word)):
        for i in word:
           if (i=="f" or i=="c" or i=="k" or i=="r"):
               j=j+1
           else:
               k=k+1

        if (j>=k):
            print("Η λέξη ",word,"είναι κακιά!")
        else:
            print("Η λέξη ",word,"είναι καλή!")
           
