from Operations.Operations import *
def run():
    """
        def: Meniul principal, apeleaza celelalte meniuri
        in: ----
        out: ----
    """
    print("Ce doriti sa faceti:")
    print("1.Adaugare")
    print("2.Cautare")
    print("3.Statistici")
    print("4.Afisare")
    while True:
        try:
            n=int(input("Alegeti optiunea:"))
        except ValueError:
            print("optiunea nu este valida")
            continue
        else:
            if(n<1 or n>4):
                print("Aceasta nu este o optiune")
                continue
            else:
                break
    if n==1:
        MeniuAdaugare()
    elif n==2:
        MeniuCautare()
    elif n==3:
        MeniuStatistici()
    elif n==4:
        Afisare()
def MeniuAdaugare():
    """
        def: Meniul optiunilor de adaugare
        in:-----
        out:-----
    """
    print("Ce doriti sa faceti:")
    print("1.Adaugare")
    print("2.Eliminare")
    print("3.Actualizare")
    print("4.Intoarce-te")
    while True:
        try:
            n=int(input("Alegeti optiunea:"))
        except ValueError:
            print("optiunea nu este valida")
            continue
        else:
            if(n<1 or n>4):
                print("Aceasta nu este o optiune")
                continue
            else:
                break
    if(n==1):
        print("Ce doriti sa adaugati:")
        print("1.Carte")
        print("2.Client")
        print("3.Imprumut")
        print("4.Intoarce-te")
        while True:
            try:
                n=int(input("Alegeti optiunea:"))
            except ValueError:
                print("optiune nu este valida")
                continue
            else:
                if(n<1 or n>4):
                    print("Aceasta nu este o optiune")
                else:
                    break
        if n==1:
            AdaugareCarte()
            MeniuAdaugare()
        elif n==2:
            AdaugareClient()
            MeniuAdaugare()
        elif n==3:
            AdaugareImprumut()
            MeniuAdaugare()
        elif n==4:
            MeniuAdaugare()
    elif(n==2):
        print("Ce doriti sa eliminati:")
        print("1.Carte")
        print("2.Client")
        print("3.Imprumut")
        print("4.Intoarce-te")
        while True:
            try:
                n=int(input("Alegeti optiunea:"))
            except ValueError:
                print("optiune nu este valida")
                continue
            else:
                if(n<1 or n>4):
                    print("Aceasta nu este o optiune")
                else:
                    break
        if n==1:
            EliminareCarte()
            MeniuAdaugare()
        elif n==2:
            EliminareClient()
            MeniuAdaugare()
        elif n==3:
            EliminareImprumut()
            MeniuAdaugare()
        elif n==4:
            MeniuAdaugare()
    elif(n==3):
        print("Ce doriti sa actualizati:")
        print("1.Carte")
        print("2.Client")
        print("3.Imprumut")
        print("4.Intoarce-te")
        while True:
            try:
                n=int(input("Alegeti optiunea:"))
            except ValueError:
                print("optiunea nu este valida")
                continue
            else:
                if(n<1 or n>4):
                    print("Aceasta nu este o optiune")
                else:
                    break
        if n==1:
            UpdateCarte()
            MeniuAdaugare()
        elif n==2:
            UpdateClient()
            MeniuAdaugare()
        elif n==3:
            UpdateImprumut()
            MeniuAdaugare()
        elif n==4:
            MeniuAdaugare()
    elif(n==4):
        run()
def MeniuCautare():
    """
        def:Meniul optiunilor de cautare
        in:-----
        out:----
    """
    print("Ce doriti sa cautati:")
    print("1.Carte")
    print("2.Client")
    print("3.Intoarce-te")
    while True:
            try:
                n=int(input("Alegeti optiunea:"))
            except ValueError:
                print("optiunea nu este valida")
                continue
            else:
                if(n<1 or n>3):
                    print("Aceasta nu este o optiune")
                    continue
                else:
                    break
    if n==1:
        CautareCarte()
        MeniuCautare()
    elif n==2:
        CautareClient()
        MeniuCautare()
    elif n==3:
        run()
def MeniuStatistici():
    """
        def: Meniul optiunilor de statistici
        in: ----
        out: ----
    """
    print("Ce statistici doriti sa vedeti:")
    print("1. Toate cartile de un anumit autor")
    print("2. Toate cartile imprumutate de un anumit client")
    print("3. Intoarce-te")
    while True:
        try:
            n=int(input("Alegeti optiunea:"))
        except ValueError:
            print("Optiunea nu este valida")
            continue
        else:
            if(n<1 or n>3):
                print("Aceasta nu este o optiune ")
                continue
            else:
                break
    if n==1:
        ToateCarti()
        MeniuStatistici()
    elif n==2:
        ToateClienti()
        MeniuStatistici()
    elif n==3:
        run()
def Afisare():
    """
        def: Afisarea listelor de carti, clienti si imprumuturi
        in: ----
        out: ----
    """
    global lista_carti
    global lista_clienti
    global lista_imprumuturi
    print(lista_carti)
    print(lista_clienti)
    print(lista_imprumuturi)
    run()
run()