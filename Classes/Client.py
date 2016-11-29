class Client():
    def __init__(self,id1,nume,prenume):
        self.__id=id1
        self.__nume=nume
        self.__prenume=prenume
    def setid(self,id1):
        self.__id=id1
    def setnume(self,n):
        self.__nume=n
    def setprenume(self,p):
        self.__prenume=p
    def getid(self):
        return self.__id
    def getnume(self):
        return self.__nume
    def getprenume(self):
        return self.__prenume
    def __str__(self):
        return str(self.__id)+". "+self.__nume+" "+self.__prenume
    def __repr__(self):
        return str(self)
    def strimp(self):
        return self.__nume+" "+self.__prenume
    