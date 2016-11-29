from Classes.Carte  import *
from Classes.Client import *
from Classes.Imprumuturi import *
lista_carti=[]
lista_clienti=[]
lista_imprumuturi=[]
idCarte=1
idClient=1
idImprumut=1
def ExistaImprumut(n):
    """
        def: Verifica daca o carte este imprumutata si daca este sterge imprumutul
        in: id-ul cartii
        out: ----
    """
    global lista_imprumuturi
    global idImprumut
    for i in range(0,len(lista_imprumuturi)):
        if lista_imprumuturi[i-1].getidC()==n:
            lista_imprumuturi.remove(lista_imprumuturi[i-1])
            idImprumut=idImprumut-1
def ExistaImprumut2(n):
    """
        def: verifica daca un client a imprumutat vreo carte si sterge imprumutul in caz afirmativ
        in: id-ul clientului
        out:-------
    """
    global lista_imprumuturi
    global idImprumut
    for i in range(0,len(lista_imprumuturi)):
        if lista_imprumuturi[i-1].getidCl()==n:
            lista_imprumuturi.remove(lista_imprumuturi[i-1])
            idImprumut=idImprumut-1
def AdaugareCarte():
    """
        def: Primeste valori de la tastatura si creeaza un obiect de tip carte cu acele valori
        in: -----
        out: ----
    """
    global lista_carti
    global idCarte
    while True:
        try:
            t=input("Titlul cartii:")
            a=input("Autorul cartii:")
        except ValueError:
            print("O valoare nu este valida")
        else:
            if t=="" or a=="":
                print("O valoare este vida")
                continue
            else:
                break
    c=Carte(idCarte,t,a)
    idCarte=idCarte+1
    lista_carti.append(c)
def AdaugareClient():
    """
        def: Primeste valori de la tastatura si creeaza un obiect de tip client cu acele valori
        in: -----
        out: ----
    """
    global lista_clienti
    global idClient
    while True:
        try:
            n=input("Numele clientului:")
            p=input("Prenumele clientului:")
        except ValueError:
            print("O valoare nu este valida")
        else:
            if n=="" or p=="":
                print("O valoare este vida")
                continue
            else:
                break
    c=Client(idClient,n,p)
    idClient=idClient+1
    lista_clienti.append(c)
def AdaugareImprumut():
    """
        def: Primeste valori de la tastatura si creeaza un obiect de tip imprumut cu acele valori
        in: -----
        out: ----
    """
    global lista_imprumuturi
    global idImprumut
    print("Carti:")
    for i in range(0,len(lista_carti)):
        print(lista_carti[i])
    print("Clienti:")
    for j in range(0,len(lista_clienti)):
        print(lista_clienti[j])
    print("Alegeti cartea si clientul")
    while True:
        try:
            x=int(input("Cartea:"))
            y=int(input("Clientul:"))
            z=int(input("Ziua imprumutului:"))
            l=int(input("Luna imprumutului:"))
            a=int(input("Anul imprumutului:"))
        except ValueError:
            print("O valoare nu este valida")
            continue
        else:
            if(x<0 or x>len(lista_carti) or y<0 or y>len(lista_clienti) or z<0 or z>31 or l<0 or l>12 or a<0):
                print("O valoare nu este corecta")
                continue
            else:
                break
    d=str(z)+"/"+str(l)+"/"+str(a)
    id1=lista_carti[x-1].getId()
    id2=lista_clienti[y-1].getid()
    c=Imprumuturi(idImprumut,id1,id2,d)
    idImprumut=idImprumut+1
    lista_imprumuturi.append(c)
def EliminareCarte():
    """
        def: Elimina o carte la alegerea utilizatorului
        in:-----
        out:-----
    """
    global idCarte
    global lista_carti
    global lista_imprumuturi
    print(lista_carti)
    print("Ce carte doriti sa eliminati:")
    while True:
        try:
            n=int(input("Alegeti id cartii de eliminat:"))
        except ValueError:
            print("Id nu este valid")
            continue
        else:
            if(n>idCarte or n<0):
                print("Id-ul nu exista")
                continue
            else:
                break
    for i in range(0,len(lista_carti)):
        if lista_carti[i-1].getId()==n:
            ExistaImprumut(n)
            lista_carti.remove(lista_carti[i-1])
            idCarte=idCarte-1
    newId=1
    for i in range(0,len(lista_carti)):
        if(newId != idCarte):
            lista_carti[i].setid(newId)
            newId+=1
        else:
            break
    print("Eliminat cu succes!")
def EliminareClient():
    """
        def: Elimina un client la alegerea utilizatorului
        in:-----
        out:-----
    """
    global idClient
    global lista_clienti
    print(lista_clienti)
    print("Ce client doriti sa eliminati:")
    while True:
        try:
            n=int(input("Alegeti id clientului de eliminat:"))
        except ValueError:
            print("Id nu este valid")
            continue
        else:
            if(n>idClient or n<0):
                print("Id-ul nu exista")
                continue
            else:
                break
    for i in range(0,len(lista_clienti)):
        if lista_clienti[i-1].getid()==n:
            ExistaImprumut2(n)
            lista_clienti.remove(lista_clienti[i-1])
            idClient=idClient-1
    newId=1
    for i in range(0,len(lista_clienti)):
        if(newId != idClient):
            lista_clienti[i].setid(newId)
            newId+=1
        else:
            break
    print("Eliminat cu succes!")
def EliminareImprumut():
    """
        def: Elimina un imprumut la alegerea utilizatorului
        in:-----
        out:-----
    """
    global idImprumut
    global lista_imprumuturi
    print(lista_imprumuturi)
    print("Ce imprumut doriti sa eliminati:")
    while True:
        try:
            n=int(input("Alegeti id imprumut de eliminat:"))
        except ValueError:
            print("Id nu este valid")
            continue
        else:
            if(n>idImprumut or n<0):
                print("Id-ul nu exista")
                continue
            else:
                break
    for i in range(0,len(lista_imprumuturi)):
        if lista_imprumuturi[i-1].getid()==n:
            lista_imprumuturi.remove(lista_imprumuturi[i-1])
            idImprumut=idImprumut-1
    newId=1
    for i in range(0,len(lista_imprumuturi)):
        if(newId != idImprumut):
            lista_imprumuturi[i].setid(newId)
            newId+=1
        else:
            break
    print("Eliminat cu succes!")
def UpdateCarte():
    """
        def: Actualizeaza una dintre valorile unui obiect de tip carte
        in: -----
        in: -----
    """
    global idCarte
    global lista_carti
    print(lista_carti)
    print("Ce carte doriti sa actualizati:")
    while True:
        try:
            n=int(input("Alegeti id:"))
        except ValueError:
            print("Id invalid")
            continue
        else:
            if(n>idCarte or n<0):
                print("Id invalid")
                continue
            else:
                break
    print("Ce doriti sa actualizati:")
    print("1. Titlul")
    print("2. Autorul")
    print("3. Ambele")
    while True:
        try:
            m=int(input("Alegeti optiunea:"))
        except ValueError:
            print("Optiune invalida")
            continue
        else:
            if(m<1 or m>3):
                print("Optiune invalida")
                continue
            else:
                break
    if m==1:
        while True:
            try:
                t=input("Introduceti titlul nou:")
            except ValueError:
                print("Titlu invalid")
                continue
            else:
                if(t==""):
                    print("Titlul nu poate fi vid")
                    continue
                else:
                    break
        for i in range(0,len(lista_carti)):
            if lista_carti[i-1].getId()==n:
                lista_carti[i-1].settitlu(t)
        print("Titlu actualizat cu succes.")
    elif m==2:
        while True:
            try:
                t=input("Introduceti autorul nou:")
            except ValueError:
                print("Autor invalid")
                continue
            else:
                if(t==""):
                    print("Autorul nu poate fi vid")
                    continue
                else:
                    break
        for j in range(0,len(lista_carti)):
            if lista_carti[j-1].getId()==n:
                lista_carti[j-1].setautor(t)
        print("Autor actualizat cu succes.")
    elif m==3:
        while True:
            try:
                t=input("Introduceti titlul nou:")
                a=input("Introduceti autor nou:")
            except ValueError:
                print("Titlu sau autor invalid")
                continue
            else:
                if(t=="" or a==""):
                    print("Titlul si autorul nu pot fi vide")
                    continue
                else:
                    break
        for p in range(0,len(lista_carti)):
            if lista_carti[p-1].getId()==n:
                lista_carti[p-1].settitlu(t)
                lista_carti[p-1].setautor(a)
        print("Titlu si autor actualizate cu succes.")
def UpdateClient():
    """
        def: Actualizeaza una dintre valorile unui obiect de tip client
        in: -----
        in: -----
    """
    global idClient
    global lista_clienti
    print(lista_clienti)
    print("Ce client doriti sa actualizati:")
    while True:
        try:
            n=int(input("Alegeti id:"))
        except ValueError:
            print("Id invalid")
            continue
        else:
            if(n>idClient or n<0):
                print("Id invalid")
                continue
            else:
                break
    print("Ce doriti sa actualizati:")
    print("1. Numele")
    print("2. Prenumele")
    print("3. Ambele")
    while True:
        try:
            m=int(input("Alegeti optiunea:"))
        except ValueError:
            print("Optiune invalida")
            continue
        else:
            if(m<1 or m>3):
                print("Optiune invalida")
                continue
            else:
                break
    if m==1:
        while True:
            try:
                t=input("Introduceti nume nou:")
            except ValueError:
                print("Nume invalid")
                continue
            else:
                if(t==""):
                    print("Numele nu poate fi vid")
                    continue
                else:
                    break
        for i in range(0,len(lista_clienti)):
            if lista_clienti[i-1].getid()==n:
                lista_clienti[i-1].setnume(t)
        print("Nume actualizat cu succes.")
    elif m==2:
        while True:
            try:
                t=input("Introduceti prenumele nou:")
            except ValueError:
                print("Prenume invalid")
                continue
            else:
                if(t==""):
                    print("Prenumele nu poate fi vid")
                    continue
                else:
                    break
        for j in range(0,len(lista_clienti)):
            if lista_clienti[j-1].getid()==n:
                lista_clienti[j-1].setprenume(t)
        print("Prenume actualizat cu succes.")
    elif m==3:
        while True:
            try:
                t=input("Introduceti nume nou:")
                a=input("Introduceti prenume nou:")
            except ValueError:
                print("Nume sau prenume invalid")
                continue
            else:
                if(t=="" or a==""):
                    print("Numele si prenumele nu pot fi vide")
                    continue
                else:
                    break
        for p in range(0,len(lista_clienti)):
            if lista_clienti[p-1].getid()==n:
                lista_clienti[p-1].setnume(t)
                lista_clienti[p-1].setprenume(a)
        print("Nume si prenume actualizate cu succes.")
def UpdateImprumut():
    """
        def: Actualizeaza una dintre valorile unui obiect de tip imprumut
        in: -----
    """
    global idImprumut
    global lista_imprumuturi
    print(lista_imprumuturi)
    print("Ce imprumut doriti sa actualizati:")
    while True:
        try:
            n=int(input("Alegeti id:"))
        except ValueError:
            print("Id invalid")
            continue
        else:
            if(n>idCarte or n<0):
                print("Id invalid")
                continue
            else:
                break
    print("Ce doriti sa actualizati:")
    print("1. Cartea")
    print("2. Clientul")
    print("3. Data")
    print("4. Toate 3")
    while True:
        try:
            m=int(input("Alegeti optiunea:"))
        except ValueError:
            print("Optiune invalida")
            continue
        else:
            if(m<1 or m>4):
                print("Optiune invalida")
                continue
            else:
                break
    if m==1:
        print(lista_carti)
        while True:
            try:
                t=int(input("Alegeti id-ul cartii:"))
            except ValueError:
                print("id invalid")
                continue
            else:
                if(t<0 or t>idCarte):
                    print("id invalid")
                    continue
                else:
                    break
        for i in range(0,len(lista_imprumuturi)):
            if lista_imprumuturi[i-1].getid()==n:
                lista_imprumuturi[i-1].setidCarte(t)
        print("Carte actualizata cu succes.")
    elif m==2:
        print(lista_clienti)
        while True:
            try:
                t=int(input("Alegeti id-ul clientului:"))
            except ValueError:
                print("Id invalid")
                continue
            else:
                if(t<0 or t>idClient):
                    print("Id invalid")
                    continue
                else:
                    break
        for j in range(0,len(lista_imprumuturi)):
            if lista_imprumuturi[j-1].getid()==n:
                lista_imprumuturi[j-1].setidClient(t)
        print("Client actualizat cu succes.")
    elif m==3:
        while True:
            try:
                z=int(input("Introduceti ziua noua:"))
                l=int(input("Introduceti luna noua:"))
                a=int(input("Introduceti anul nou:"))
            except ValueError:
                print("Valoare invalida")
                continue
            else:
                if(z<0 or z>31 or l<0 or l>12 or a<0):
                    print("Valoare invalida")
                    continue
                else:
                    break
        d=str(z)+"/"+str(l)+"/"+str(a)
        for p in range(0,len(lista_imprumuturi)):
            if lista_imprumuturi[p-1].getid()==n:
                lista_imprumuturi[p-1].setData(d)
        print("Data actualizata cu succes.")
    elif m==4:
        print(lista_carti)
        print(lista_clienti)
        while True:
            try:
                t=int(input("Alegeti id-ul cartii:"))
                o=int(input("Alegeti id-ul clientului:"))
                z=int(input("Introduceti ziua noua:"))
                l=int(input("Introduceti luna noua:"))
                a=int(input("Introduceti anul nou:"))
            except ValueError:
                print("Valoare invalida")
                continue
            else:
                if t<0 or t>idCarte or o<0 or o>idClient or z<0 or z>31 or l<0 or l>12 or a<0:
                    print("Valoare invalida")
                    continue
                else:
                    break
        d=str(z)+"/"+str(l)+"/"+str(a)
        for i in range(0,len(lista_imprumuturi)):
            if lista_imprumuturi[i-1].getid()==n:
                lista_imprumuturi[i-1].setidCarte(t)
                lista_imprumuturi[i-1].setidClient(o)
                lista_imprumuturi[i-1].setData(d)
        print("Valori actualizate cu succes")
def CautareCarte():
    """
        def:Cauta o carte dupa o anumita valoare primita de la tastatura
        in:-----
        out:-----
    """
    global lista_carti
    print("Dupa ce criteriu vreti sa cautati:")
    print("1. Titlu")
    print("2. Autor")
    while True:
        try:
            n=int(input("Alegeti optiunea:"))
        except ValueError:
            print("Optiunea nu este valida")
            continue
        else:
            if(n<0 or n>2):
                print("Optiunea nu este valida")
                continue
            else:
                break
    if n==1:
        while True:
            try:
                t=input("Titlu de cautat:")
            except ValueError:
                print("Titlu invalid")
                continue
            else:
                if(t==""):
                    print("Titlu invalid")
                    continue
                else:
                    break
    
        for i in range(0,len(lista_carti)):
            if lista_carti[i-1].gettitlu()==t:
                print(lista_carti[i-1])
        else:
            print("Nu exista carte cu titlul dat.")
    elif n==2:
        while True:
            try:
                a=input("Autor de cautat:")
            except ValueError:
                print("Autor invalid")
                continue
            else:
                if(a==""):
                    print("Autor invalid")
                    continue
                else:
                    break
        for i in range(0,len(lista_carti)):
            if lista_carti[i-1].getautor()==a:
                print(lista_carti[i-1])
        else:
            print("Nu exista carte cu autorul dat.")
def CautareClient():
    """
        def:Cauta un client dupa o anumita valoare primita de la tastatura
        in:-----
        out:-----
    """
    global lista_clienti
    print("Dupa ce criteriu vreti sa cautati:")
    print("1. Nume")
    print("2. Prenume")
    while True:
        try:
            n=int(input("Alegeti optiunea:"))
        except ValueError:
            print("Optiunea nu este valida")
            continue
        else:
            if(n<0 or n>2):
                print("Optiunea nu este valida")
                continue
            else:
                break
    if n==1:
        while True:
            try:
                t=input("Nume de cautat:")
            except ValueError:
                print("Nume invalid")
                continue
            else:
                if(t==""):
                    print("Nume invalid")
                    continue
                else:
                    break
    
        for i in range(0,len(lista_clienti)):
            if lista_clienti[i-1].getnume()==t:
                print(lista_clienti[i-1])
        else:
            print("Nu exista client cu numele dat.")
    elif n==2:
        while True:
            try:
                a=input("Prenume de cautat:")
            except ValueError:
                print("Prenume invalid")
                continue
            else:
                if(a==""):
                    print("Prenume invalid")
                    continue
                else:
                    break
        for i in range(0,len(lista_clienti)):
            if lista_clienti[i-1].getprenume()==a:
                print(lista_clienti[i-1])
        else:
            print("Nu exista client cu prenumele dat.")
def Cautare(l,n):
    """
        def: Cauta o valoare intr-o lista
        in:lista si valoarea de cautat
        out: True in cazul in care gaseste valoarea in lista, False otherwise
    """
    for i in range(0,len(l)):
        if l[i]==n:
            return True
    else:
        return False
def ToateCarti():
    """
        def: Verifica cate carti de la acelasi autor se afla in biblioteca
        in: -----
        out: -----
    """
    print("Alegeti autorul:")
    j=1
    lista_autori=[]
    for i in range (0,len(lista_carti)):
        k=lista_carti[i].getautor()
        if(Cautare(lista_autori,k)==False):
            lista_autori.append(k)
    for i in range(0,len(lista_autori)):
        print(j,". ",lista_autori[i])
        j+=1
    while True:
        try:
            n=int(input("Alegeti autorul:"))
        except ValueError:
            print("optiune invalida")
            continue
        else:
            if(n<0 or n>j):
                print("Optiune invalida")
                continue
            else:
                break
    a=lista_carti[n-1].getautor()
    j=0
    for i in range (0,len(lista_carti)):
        if lista_carti[i].getautor()==a:
            j+=1
    print("Autorul ",a," are ",j," carti in biblioteca")
def ToateClienti():
    """
        def: Verifica cate carti sunt imprumutate de cate un anumit client
        in: -----
        out: -----
    """
    print("Alegeti clientul:")
    j=1
    clienti=[]
    for i in range (0,len(lista_clienti)):
        k=lista_clienti[i].getnume()
        if(Cautare(clienti,k)==False):
            clienti.append(k)
    for i in range(0,len(clienti)):
        print(j,". ",clienti[i])
        j+=1
    while True:
        try:
            n=int(input("Alegeti clientul:"))
        except ValueError:
            print("optiune invalida")
            continue
        else:
            if(n<0 or n>j):
                print("Optiune invalida")
                continue
            else:
                break
    a=lista_clienti[n-1].getid()
    j=0
    for i in range(0,len(lista_imprumuturi)):
        if lista_imprumuturi[i].getidCl()==a:
            j+=1
    print("Clientul ",a," are ",j," carti imprumutate")
    