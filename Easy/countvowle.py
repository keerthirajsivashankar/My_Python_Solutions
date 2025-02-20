s = input("Enter the string : ")
v = {'a','e','i','o','u'}
sym = {'!','@','~','`','#','$','%','^','&','*',',','.','<','>','/','|'}
con = "bcdfghjklmnpqrstvwxyz"
num = '1234567890'
num = set(num)
con = set(con)
countv = 0
countc = 0
counts = 0
countn = 0
for c in s:
    if c in sym:
        counts += 1
    elif c.lower() in v:
        countv += 1
    elif c.lower() in con:
        countc += 1
    elif c in num:
        countn += 1
print(f"The Number of Vowels : {countv}")
print(f"The Number of consonants : {countc}")
print(f"The Number of symbols : {counts}")
print(f"The Number of Numbers : {countn}")