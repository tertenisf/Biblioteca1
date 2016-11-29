from Classes.Carte import Carte
from Classes.Client import Client
from Classes.Imprumuturi import Imprumuturi
def TestCarte():
    c=Carte(1,"Ion","Liviu Rebreanu")
    assert c.getId()==1
    assert c.gettitlu()=="Ion"
    assert c.getautor()=="Liviu Rebreanu"
    c.setid(2)
    c.settitlu("Flori de mucigai")
    c.setautor("Tudor Arghezi")
    assert c.getId()==2
    assert c.gettitlu()=="Flori de mucigai"
    assert c.getautor()=="Tudor Arghezi"
def TestClient():
    c=Client(1,"Buia","Catalin")
    assert c.getid()==1
    assert c.getnume()=="Buia"
    assert c.getprenume()=="Catalin"
    c.setid(2)
    c.setnume("Flori de mucigai")
    c.setprenume("Tudor Arghezi")
    assert c.getid()==2
    assert c.getnume()=="Flori de mucigai"
    assert c.getprenume()=="Tudor Arghezi"
def TestImprumuturi():
    c=Imprumuturi(1,1,1,10/10/2010)
    assert c.getid()==1
    assert c.getidC()==1
    assert c.getidCl()==1
    assert c.getData()==10/10/2010
    c.setid(2)
    c.setidCarte(2)
    c.setidClient(2)
    c.setData(11/11/2011)
    assert c.getid()==2
    assert c.getidC()==2
    assert c.getidCl()==2
    assert c.getData()==11/11/2011
TestCarte()
TestClient()
TestImprumuturi()