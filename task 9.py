#pyhthon program to count number of uppercase characters in a string.
name=("jyothsna sunny")
count=0
for ch in name:
    if ch.isupper():
        count+=1
print("upper cases in name are:",count)
