class Carte():
    def __init__(self,idC,t,a):
        self.__id=idC
        self.__titlu=t
        self.__autor=a
    def setid(self,id1):
        self.__id=id1
    def settitlu(self,t):
        self.__titlu=t
    def setautor(self,a):
        self.__autor=a
    def getId(self):
        return self.__id
    def gettitlu(self):
        return self.__titlu
    def getautor(self):
        return self.__autor
    def __str__(self):
        return str(self.__id)+". "+self.__titlu+" de "+self.__autor
    def __repr__(self):
        return str(self)
    def strimp(self):
        return self.__titlu+" de "+self.__autor