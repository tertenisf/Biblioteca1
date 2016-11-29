class Imprumuturi:
    def __init__(self,idI,idC,idCl,Data):
        self.__id=idI
        self.__idCarte=idC
        self.__idClient=idCl
        self.__Data=Data
    def setid(self,id1):
        self.__id=id1
    def setidCarte(self,idC):
        self.__idCarte=idC
    def setidClient(self,idCl):
        self.__idClient=idCl
    def setData(self,d):
        self.__Data=d
    def getid(self):
        return self.__id
    def getidC(self):
        return self.__idCarte
    def getidCl(self):
        return self.__idClient
    def getData(self):
        return self.__Data
    def __str__(self):
        from Operations.Operations import lista_carti
        from Operations.Operations import lista_clienti
        c=" "
        cl=" "
        for i in range(0,len(lista_carti)):
            if lista_carti[i].getId()==self.__idCarte:
                c=lista_carti[i].strimp()
        for j in range(0,len(lista_clienti)):
            if lista_clienti[j].getid()==self.__idClient:
                cl=lista_clienti[j].strimp()
            return str(self.__id)+". "+c+" imprumutata de "+cl+" in data de "+self.__Data
    def __repr__(self):
        return str(self)
    