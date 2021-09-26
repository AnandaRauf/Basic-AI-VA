import pyttsx3

mesin = pyttsx3.init()

def menu():
    print("Menu Basic AI\n")
    print
    print("1.VoiceTxt")
    print("2.Voice")

def VoiceTxt():
    file = open("TestAI.txt")
    bacafile = file.readlines()
    bacabaris = bacafile[0]
    bicara = mesin.say(bacabaris)
    bicara = mesin.runAndWait()
    print(bicara)

def Voice():
    berbicara = mesin.say("Test")
    berbicara = mesin.runAndWait()
    print(berbicara)

menu()
pilihmenu = int(input("Pilih menu Basic AI:"))
if pilihmenu == 1:
    VoiceTxt()
elif pilihmenu == 2:
    Voice()






