#Define a function caesarCipher that takes string and key(number), whuch returns encrypted string

def caesarCipher(string,key):
    i1=''
    for i in string:
        if i == ' ':
            i1= i1 + i
        elif i.isupper():
            i1 = i1 + chr((ord(i)+ key - 65) %  26 + 65)
        else:
            i1 = i1 + chr((ord(i)+ key - 97) %  26 + 97)
    print(i1)
    return i1
    #print(encstring)
#print(len(A))
text = input("Enter string to be encrypted: ")
key = int(input("Enter shift: "))
Message = ("You entered {0} and shift value equal to {1}, the encrypted sting is: {2}")
print(Message.format(text,key,caesarCipher(text,key)))

