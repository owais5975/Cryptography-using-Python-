# import the numpy module 
import numpy
# import the module
from numpy import random

Crypto = {"0": 27, "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13,
    "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23,"x": 24, "y": 25, "z": 26}

Cryptolist = list(Crypto)

message = input("Enter message to Encryt:\n")

message = message.replace(" ", "0")

message = message.lower()

j = 0
EmptyList = []

character = ""
for i in message:
    character = message[j]
    j = j + 1
    y = 0
    item = ""
    for x in Crypto:
        if(character == x):
            EmptyList.append(Crypto[x])
        y = y + 1

filledList = EmptyList

NewListLength = len(EmptyList)
Zeroslist = []
while(True):
    if(NewListLength%3 != 0):
        Zeroslist.append(27)
        NewListLength = NewListLength + 1
    else:
        break
NewList = EmptyList + Zeroslist 

listArray = numpy.array(NewList)

listArray1 = listArray.reshape(3, int(len(NewList)/3))

cipherarray = numpy.array([[-3, -3, -4],[0, 1, 1], [4, 3, 4]])
cipherarrayInverse = numpy.linalg.inv(cipherarray) 

encryptedmessage = numpy.dot(cipherarray, listArray1)
print(f"Encryted Message:\n{encryptedmessage}")

decryptedmessage = numpy.dot(cipherarrayInverse, encryptedmessage)

print(f"\nDecryted Message:\n{decryptedmessage}")

decryptedmessage = listArray.tolist()

key_list = list(Crypto.keys())
val_list = list(Crypto.values())
b = 0
position = 0
EmptyList1 = []
for a in decryptedmessage:
    b = b + 1
    k = 0
    for c in Crypto:
        if(a == Crypto[c]):
            value = val_list.index(Crypto[c])
            EmptyList1.append(key_list[value])
            k = k + 1


print("\nDecryted Message in plaintext:")
for plaintext in EmptyList1:
    if(plaintext == '0'):
        print(" ", end="")
    else:
        print(plaintext, end="")




