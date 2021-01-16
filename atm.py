class Atm (object) :

    def __init__(self , cardnumber , pinnumber):
        self.cardnumber = cardnumber
        self.pinnumber = pinnumber

    def start(self):
        print("started")

    def stop(self):
        print("stoped")


atm1 = Atm(6554654534766543,8765)

print(atm1.cardnumber)
print(atm1.pinnumber)

        