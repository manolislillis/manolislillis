num=input("Δώστε ενα νουμέρο:")
a=True
while (a):
    if (num.isdigit()):
        a=False
    else:
        num=input("Κάνατε κάποιο λάθος!Δώστε πάλι νούμερο:")

x=int(num)
x=(x*3)+1
check=True
if (x<10 and x>-10):
    print ("Ο αριθμός σας τριπλασιασμενός αυξημένος κατά ένα και με προσθεμενα τα ψηφία του μέχρι να γίνει μονοψήφιος ειναι:",x)
else:
    while (x>=10 or x<=-10):
        if (check):
            y=str(x)
            sumary=0
            for i in range (len(y)):
                sumary=sumary + int(y[i])

            x=sumary
            check=False
        else:
            x=(x*3)+1
            y=str(x)
            sumary=0
            for i in range (len(y)):
                sumary=sumary + int(y[i])

            x=sumary

print("Ο αριθμός σας τριπλασιασμενός αυξημένος κατά ένα και με προσθεμενα τα ψηφία του μέχρι να γίνει μονοψήφιος ειναι:",x)
