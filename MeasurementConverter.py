#miles
#uses km m yd ft in cm
def MileConvert():
    question = input("\nWhat is given? km, m, yd, ft, in, cm? ")
    if question.lower() == "km":
        ask = float(input("What is given in Km? " ))
        answer = ask * 1.609
        print(answer)
    elif question.lower() == "m":
        ask = float(input("What is given in m? "))
        answer = ask * 1609.344
        print(answer)
    elif question.lower() == "yd":
        ask = float(input("What is given in yd? "))
        answer = ask * 1760
        print(answer)
    elif question.lower() == "ft":
        ask = float(input("What is given in ft? "))
        answer = ask * 5280
        print(answer)
    elif question.lower() == "in":
        ask = float(input("What is given in in? "))
        answer = ask * 63360
        print(answer)
    elif question.lower() == "cm":
        ask = float(input("What is given in cm? " ))
        answer = ask * 160934
        print(answer)
    else:
        print("That is an invalid option")
        FirstQuestion()

#kilometers
#uses mi m yd ft in cm
def KiloConvert():
    question = input("\nWhat is given? mi, m, yd, ft, in, cm? ")
    if question.lower() == "mi":
        ask = float(input("What is given in mi?" ))
        answer = ask * 0.621371
        print(answer)
    elif question.lower() == "m":
        ask = float(input("What is given in m?" ))
        answer = ask * 1000
        print(answer)
    elif question.lower() == "yd":
        ask = float(input("What is given in yd?" ))
        answer = ask * 1093.61
        print(answer)
    elif question.lower() == "ft":
        ask = float(input("What is given in ft?" ))
        answer = ask * 3280.84
        print(answer)
    elif question.lower() == "in":
        ask = float(input("What is given in in?" ))
        answer = ask * 39370.1
        print(answer)
    elif question.lower() == "cm":
        ask = float(input("What is given in cm?" ))
        answer = ask * 100000
        print(answer)
    else:
        print("That is an invalid option")
        FirstQuestion()

#update the math from here to below
#meters
#uses mi km yd ft in cm
def MeterConvert():
    question = input("\nWhat is given? mi, km, yd, ft, in, cm? ")
    if question.lower() == "mi":
        ask = float(input("What is given in mi?" ))
        answer = ask * 0.000621
        print(answer)
    elif question.lower() == "km":
        ask = float(input("What is given in km?" ))
        answer = ask * 0.001
        print(answer)
    elif question.lower() == "yd":
        ask = float(input("What is given in yd?" ))
        answer = ask * 1.09361
        print(answer)
    elif question.lower() == "ft":
        ask = float(input("What is given in ft?" ))
        answer = ask * 3.28084
        print(answer)
    elif question.lower() == "in":
        ask = float(input("What is given in in?" ))
        answer = ask * 39.3701
        print(answer)
    elif question.lower() == "cm":
        ask = float(input("What is given in cm?" ))
        answer = ask * 100
        print(answer)
    else:
        print("That is an invalid option")
        FirstQuestion()
#yards
#uses mi km m ft in cm
def YardConvert():
    question = input("\nWhat is given? mi, m, yd, ft, in, cm? ")
    if question.lower() == "mi":
        ask = float(input("What is given in mi?" ))
        answer = ask / 1760
        print(answer)
    elif question.lower() == "km":
        ask = float(input("What is given in km?" ))
        answer = ask / 1094
        print(answer)
    elif question.lower() == "m":
        ask = float(input("What is given in m?" ))
        answer = ask / 1.094
        print(answer)
    elif question.lower() == "ft":
        ask = float(input("What is given in ft?" ))
        answer = ask * 3
        print(answer)
    elif question.lower() == "in":
        ask = float(input("What is given in in?" ))
        answer = ask * 36
        print(answer)
    elif question.lower() == "cm":
        ask = float(input("What is given in cm?" ))
        answer = ask * 91.44
        print(answer)
    else:
        print("That is an invalid option")
        FirstQuestion()
#feet
#uses mi km m yd in cm
def FeetConvert():
    question = input("\nWhat is given? mi, m, yd, ft, in, cm? ")
    if question.lower() == "mi":
        ask = float(input("What is given in mi?" ))
        answer = ask / 5280
        print(answer)
    elif question.lower() == "km":
        ask = float(input("What is given in km?" ))
        answer = ask / 3281
        print(answer)
    elif question.lower() == "m":
        ask = float(input("What is given in m?" ))
        answer = ask / 3.281
        print(answer)
    elif question.lower() == "yd":
        ask = float(input("What is given in yd?" ))
        answer = ask / 3
        print(answer)
    elif question.lower() == "in":
        ask = float(input("What is given in in?" ))
        answer = ask * 12
        print(answer)
    elif question.lower() == "cm":
        ask = float(input("What is given in cm?" ))
        answer = ask * 30.48
        print(answer)
    else:
        print("That is an invalid option")
        FirstQuestion()
#inches 
#uses mi km m yd ft cm
def InchConvert():
    question = input("\nWhat is given? mi, m, yd, ft, in, cm? ")
    if question.lower() == "mi":
        ask = float(input("What is given in mi?" ))
        answer = ask / 63360
        print(answer)
    elif question.lower() == "km":
        ask = float(input("What is given in km?" ))
        answer = ask / 39370
        print(answer)
    elif question.lower() == "m":
        ask = float(input("What is given in m?" ))
        answer = ask / 39.37
        print(answer)
    elif question.lower() == "yd":
        ask = float(input("What is given in yd?" ))
        answer = ask / 36
        print(answer)
    elif question.lower() == "ft":
        ask = float(input("What is given in ft?" ))
        answer = ask / 12
        print(answer)
    elif question.lower() == "cm":
        ask = float(input("What is given in cm?" ))
        answer = ask * 2.54
        print(answer)
    else:
        print("That is an invalid option")
        FirstQuestion()
#centimeters
def CentiConvert():
    question = input("\nWhat is given? mi, m, yd, ft, in, cm? ")
    if question.lower() == "mi":
        ask = float(input("What is given in mi?" ))
        answer = ask / 160934
        print(answer)
    elif question.lower() == "km":
        ask = float(input("What is given in km?" ))
        answer = ask / 100000
        print(answer)
    elif question.lower() == "m":
        ask = float(input("What is given in m?" ))
        answer = ask / 100
        print(answer)
    elif question.lower() == "yd":
        ask = float(input("What is given in yd?" ))
        answer = ask / 91.44
        print(answer)
    elif question.lower() == "ft":
        ask = float(input("What is given in ft?" ))
        answer = ask / 30.48
        print(answer)
    elif question.lower() == "in":
        ask = float(input("What is given in in?" ))
        answer = ask / 2.54
        print(answer)
    else:
        print("That is an invalid option")
        FirstQuestion()

print("Welcome to the Measurement Conveter Beta")

print("\nThis will be used to conver Miles, Kilometers, Meters, Yards, Feet, Inches, and Centimeters to any conversion between any of these")

FirstQuestion = input("\nWhat does it need to be converted to? Mi, Km, M, Yd, Ft, In, Cm? ")

if FirstQuestion.lower() == "mi":
    MileConvert()
elif FirstQuestion.lower() == "km":
    KiloConvert()
elif FirstQuestion.lower() == "m":
    MeterConvert()
elif FirstQuestion.lower() == "yd":
    YardConvert()
elif FirstQuestion.lower() == "ft":
    FeetConvert()
elif FirstQuestion.lower() == "in":
    InchConvert()
elif FirstQuestion.lower() == "cm":
    CentiConvert()
else:
    print("That is an invalid option")