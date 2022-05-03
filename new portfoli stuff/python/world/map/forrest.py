
from caracter.caracter import caracter
import random
class location:
    def __init__(self,name, residents, race):
        self.name = name 
        self.residents = residents 
        self.race = race
        self.name += "of the" + self.race

    def ambush(self):
        numberoatk = random.randint(1,5)
        print(numberoatk)
        attackers = []
        while numberoatk >0 :
            wolf = caracter("wolf","wolf", "male","npc")
            attackers.append(wolf)
            numberoatk -= 1
        print(attackers[0])
        attackers[0].stats()

    def camp(self,player,carac):
        if player == "player":
            print("1.rest")
            print("2.train")
            print("3.check stats")
            print("4.fight")
            choser = input("chose action")
            try:
                choser = int(choser)
                if choser == 1:
                    carac.rest()
                elif choser == 2:
                    carac.training()
                elif choser == 3:
                    carac.stats()
                elif choser == 4:
                    print("test")
                    wolf = caracter("npc","wolf")
                    wolf.caractercreation()
                    wolf.stats()
                    carac.fight(wolf)
            except:
                return


        