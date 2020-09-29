def Fibonaccizahlen():                                                                                                                       #Erstellung der Funktion
    a = int(input("Bitte geben Sie an, bis zur welchen Stelle die Liste geführt werden soll (die angegeben Zahl muss größer drei sein.): ")) #Abfrage der Variable
    while a < 3:                                                                                                                             #Prüfung der Variable
       a = int(input("Bitte geben Sie eine Zahl ein, die größer ist als zwei: "))                                                            #Abfrage der Variable bei einem Fehler
    Liste = [int(1), int(1)]                                                                                                                 #Erstellung einer Liste mit den Zahlen 1 und 1
    while a > 2:
        a = a - 1                                                                                                                            #Counter für die letzte Stelle der Liste
        p_liste = [int(Liste[-1]) + int(Liste[-2])]                                                                                          #Erstellung einer Liste, welche sich aus der Summe der zwei letzten Variablen der vorherigen Liste zusammen setzt
        Liste = Liste + p_liste                                                                                                              #die letzte Liste wird an die erste Liste angehängt
    print(Liste)                                                                                                                             #die vollständige Liste wird ausgegeben

Fibonaccizahlen()                                                                                                                            #die Funktion wird aufgrufen