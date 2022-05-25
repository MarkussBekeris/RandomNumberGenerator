import random as r

def classic():
    count = int(input("Count for how many numbers you need: "))

    startingNumber = int(input("Starting number: "))
    endingNumber = int(input("Ending number: "))
    for i in range(count):
        rand = r.randint(startingNumber, endingNumber)
        print(rand)

def Commas():
    count = int(input("Count for how many numbers you need: "))

    startingNumber = int(input("Starting number: "))
    endingNumber = int(input("Ending number: "))
    for i in range(count):
        comma = r.randint(1, 9)
        rand = r.randint(startingNumber, endingNumber)
        print("%s,%s"%(rand, comma))

commaQ = input("Use random commas - Y / N: ")

if commaQ == "N":
    classic()
elif commaQ == "Y":
    Commas()
else:
    print("Error! You have to enter Y or N, with caps!")