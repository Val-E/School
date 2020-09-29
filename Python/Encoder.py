###Braucht python3.7!!!
def Encoder():
    phrase = input("Bitte geben Sie die zu verschlüsselende Nachricht ein (ggf. bitte keine Sondernzeichen, Umlaute oder Zahlen verwenden, da diese normal ausgegeben werden): ")

    for i in phrase:
        if i == " ":
            print(":")
        elif i == "a" or i == "A":
            print("*,7,4,2,6,9,#,7,8,9;")
        elif i == "b" or i == "B":
            print("1,4,7,*,1,2,5,4,4,5,6,9,',0,*;")
        elif i == "c" or i == "C":
            print("3,2,1,4,7,8,9;")
        elif i == "d" or i == "D":
            print("1,4,7,*,1,2,6,9,0,*;")
        elif i == "e" or i == "E":
            print("7,8,6,3,2,1,4,7,*,0,#;")
        elif i == "f" or i == "F":
            print("1,4,7,*,1,2,3,7,8;")
        elif i == "g" or i == "G":
            print("3,2,1,4,7,*,0,#,9,8;")
        elif i == "h" or i == "H":
            print("1,4,7,4,5,6,3,6,9;")
        elif i == "i" or i == "I":
            print("2,5,8,0;")
        elif i == "j" or i == "J":
            print("1,2,3,6,9,#,0,*,7;")
        elif i == "k" or i == "K":
            print("1,4,7,*,7,5,3,8,#;")
        elif i == "l" or i == "L":
            print("1,4,5,*,0;")
        elif i == "m" or i == "M":
            print("1,4,7,*,1,5,3,6,9,#;")
        elif i == "n" or i == "N":
            print("1,4,7,*,1,5,9,#,9,6,3;")
        elif i == "o" or i == "O":
            print("1,4,7,8,9,6,3,2,1;")
        elif i == "p" or i == "P":
            print("1,4,7,*,1,2,3,6,9,8,7;")
        elif i == "q" or i == "Q":
            print("1,4,7,*,0,9,6,3,2,1,8,#;")
        elif i == "r" or i == "R":
            print("1,4,7,*,1,2,3,6,8,#;")
        elif i == "s" or i == "S":
            print("3,2,1,4,5,6,9,#,0,*;")
        elif i == "t" or i == "T":
            print("1,2,3,2,5,8,0;")
        elif i == "u" or i == "U":
            print("1,4,7,8,9,6,3;")
        elif i == "v" or i == "V":
            print("1,4,8,6,3;")
        elif i == "w" or i == "W":
            print("1,4,7,5,9,6,3;")
        elif i == "x" or i == "X":
            print("1,5,9,7,5,3;")
        elif i == "y" or i == "Y":
            print("1,5,3,5,8,0;")
        elif i == "z" or i == "Z":
            print("1,2,3,5,7,8,9;")
        else:
            print(i)
Encoder()
