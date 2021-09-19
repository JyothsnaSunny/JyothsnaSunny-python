#python program to calculate the number of digits and letters in a string.
a=input("enter a string")
dcount=0
chcount=0
for ch in a:
    if ch.isdigit():
        dcount+=1
    elif ch.isalpha():
        chcount+=1
    else:
        pass
 print("no.of digits in string:",dcount)
 print("no.of charcters in string:",chcount)

            
            
