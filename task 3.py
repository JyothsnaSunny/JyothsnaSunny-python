#phython program to count the number of vowels in a string.
a=input("enter a string")#jyothsna
count=0
for ch in a:
    if (ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
        count+=1
print("no.of vowels in a given string are:",count)
