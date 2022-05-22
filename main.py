import random as r

count = int(input("Count for how many numbers you need: "))
commaQ = input("Use random commas - Y / N: ")
startingNumber = int(input("Starting number: "))
endingNumber = int(input("Ending number: "))

def classic():
    for i in range(count):
        rand = r.randint(startingNumber, endingNumber)
        print(rand)

def Commas():
    for i in range(count):
        comma = r.randint(1, 9)
        rand = r.randint(startingNumber, endingNumber)
        print("%s,%s"%(rand, comma))

if commaQ == "N" or "n":
    classic()
elif commaQ == "Y" or "y":
    Commas()
else:
    print("Error! You have to enter a number!")