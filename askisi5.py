
def kainourgia(x):
    from string import ascii_letters

    if set(x).difference(ascii_letters):
        return True
    else:
        return False
        
def checknum(x):
    if (x.isalpha()):
        return True
    else:
        return False
       
    

keimeno=open("keimeno.txt","r")
for word in keimeno.read().split():
    proto=word[0]
    telos=word[-1]
    if(kainourgia(proto)):
        word=word.replace(proto,"")

    if(kainourgia(telos)):
        word=word.replace(telos,"")

    
    if(checknum(word)):
        if (len(word)>3):
            proto=word[0]
            new=word.replace(proto,"")+proto+"ay"
            print(new)
