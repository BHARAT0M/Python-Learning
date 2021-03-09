# Caesar cipher
import os
from art import logo
shiftNumber = ""
catalog = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
           'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '#', '$', '%', '&', '(', ')', '*', '+', '?', '.', ',', ':',
           ';', '-', '<', '>', '=', '[', ']', '{', '}', '\\', '/', '\'', '"', '@', '£', '|', 'ä', 'ö', 'å', 'Ä', 'Ö', 'Å', '§', '½', ' ']
catalogSize = len(catalog)


def clear():
    os.system('cls')


def printCaesar():
    print(logo)


def decode():
    messageLength = len(message)
    decodedIndexed = []
    decoded = ""
    for index in range(messageLength):
        catalogIndex = catalog.index(message[index])
        catalogIndex -= shiftNumber
        catalogIndex = overflowNegative(catalogIndex)
        decodedIndexed.append(catalogIndex)
    for number in decodedIndexed:
        decoded += catalog[number]
    return decoded


def encode():
    messageLength = len(message)
    encodedIndexed = []
    encoded = ""
    for index in range(messageLength):
        catalogIndex = catalog.index(message[index])
        catalogIndex += shiftNumber
        catalogIndex = overflowPositive(catalogIndex)
        encodedIndexed.append(catalogIndex)
    for number in encodedIndexed:
        encoded += catalog[number]
    return encoded


def overflowNegative(catalogIndex):
    returnIndex = catalogIndex
    while returnIndex < 0:
        returnIndex += catalogSize
    return returnIndex


def overflowPositive(catalogIndex):
    returnIndex = catalogIndex
    while returnIndex > catalogSize:
        returnIndex -= catalogSize
    return returnIndex


while True:
    clear()
    printCaesar()
    encodeDecode = input("\n Type 'e' to encrypt, 'd' to decrypt: \n ")
    message = input(" \n Type your message: \n ")
    try:
        shiftNumber = int(input("\n Type the shift number: \n "))
    except:
        print("\n*****   Shift number has to be an integer, please try again.  *****\n")
        quit = input(" Press ENTER to continue, q to quit.\n ")
        if quit == 'q':
            print("\n\n Program finished. Have a nice day :=)\n\n")
            break
        else:
            continue
    if shiftNumber < 1 or shiftNumber > 100000000:
        print("\n*****   Shift number cannot be less than 1 or more than 100 000 000, please try again.  *****\n")
        quit = input(" Press ENTER to continue, q to quit.\n ")
        if quit == 'q':
            print("\n\n Program finished. Have a nice day :=)\n\n")
            break
        else:
            continue
    if encodeDecode == "e":
        encoded = encode()
        print(f"\n Here's the encoded result: \n {encoded}")
    elif encodeDecode == "d":
        decoded = decode()
        print(f"\n Here's the decoded result: \n {decoded}")
    else:
        print("\n*****  Bad input, please try again.  *****\n")
        quit = input(" Press ENTER to continue, q to quit.\n ")
        if quit == 'q':
            print("\n\n Program finished. Have a nice day :=)\n\n")
            break
        else:
            continue
    again = input("\n Type 'y' if you want to continue, 'n' if you don't: \n ")
    if again == "y":
        continue
    elif again == "n":
        print("\n\n Program finished. Have a nice day :=)\n\n")
        break
    else:
        print("\n*****  Bad input, please try again.  *****\n")
        quit = input(" Press ENTER to continue, q to quit.\n ")
        if quit == 'q':
            print("\n\n Program finished. Have a nice day :=)\n\n")
            break
        else:
            continue
