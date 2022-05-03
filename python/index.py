# 1. lag en variabel som er global og en variabel med det samme navnet som er lokal.
a=2
print(a)
def math(a):
    a=int(3)
    a= a+2
    print(a)
math(a)
print(a)


# 2. lag et par variabler og se om du kan finne en list som inneholder disse variabelnavnene.

isalive = True
age = 30
needscoffee = True

print(dir())

# 3. finn en liste med alle dine globale variabler.
print(globals())

# 4. lag en klasse som har fem eller flere funksjoner i seg.


# 5. lag en instance av denne klassen.

# 6. lag en funksjon som spawner/lager flere instances.

# 7. bruk dine nye instancer og lag et lite tekstbasert spill ut av det. Noen idéer: random int, trilling av terninger, equipment som modifiserer variabler (list append), bekjempe instances.

# Husk å kommentere koden.

import random
# variable zone
kills = 0

baseatk = 1
basehp = 40
basehit= 1
basedefe = 1

#class zone
class Player:
    def __init__(self, name, atk, hp, hit, defe):
        self.name = name
        self.atk = atk
        self.hp = hp
        self.hit = hit
        self.defe = defe
    def stats(self):
        print("name:", self.name,"atk", self.atk, "hp:", self.hp, "hit:", self.hit )

#caracter generation

you = Player("you",baseatk+(random.randint(4,9)),basehp+(random.randint(4,9)), basehit+(random.randint(1,9)),basedefe+(random.randint(1,4)),)


enemy = Player("enemy",baseatk+(random.randint(4,9)),basehp+(random.randint(4,9)), basehit+(random.randint(1,9)),basedefe+(random.randint(1,4)))


def fight(player, you, enemy,):
        if (enemy.hit > you.hit):
            you.hp = you.hp - (enemy.atk - you.defe)
            enemy.hit =enemy.hit - 1
            print("your hp",you.hp)
            if (you.hp < 0):
                print("you died")
                isalive= False
                return you.hp
        elif (you.hit > enemy.hit):
            enemy.hp = enemy.hp - (you.atk - enemy.defe)
            you.hit = you.hit - 1
            print("enemys hp", enemy.hp)
            if (enemy.hp < 0 ):
                print("you won")
                return you.hp
        else:
            if(enemy.atk > you.atk):
                you.hp = you.hp - (enemy.atk - you.defe)
                enemy.hit =enemy.hit - 1
                print("your hp",you.hp)
                if (you.hp < 0):
                    print("you died")
                    isalive= False
                    return you.hp
            elif(you.atk > enemy.atk)&you.hit>0:
                enemy.hp = enemy.hp - (you.atk - enemy.defe)
                you.hit = you.hit - 1
                print("enemys hp", enemy.hp)
                if (enemy.hp < 0 ):
                    print("you won")
                    return you.hp
            else:
                you.hit = you.hit +(random.randint(1,9))
                enemy.hit = enemy.hit +(random.randint(1,9))
                return you.hp, enemy.hp

        





fight(Player, you, enemy,)

you.stats

while you.hp > 0 :
    you.stats()
    # action=input
    if enemy.hp <=0:
        enemy = Player("enemy",baseatk+(random.randint(4,9)),basehp+(random.randint(4,9)), basehit+(random.randint(1,9)),basedefe+(random.randint(1,4)))
    else:
        fight(Player, you, enemy,)



import random



# classes
class wepon:
    def __init__(self,name,attack,defence,health):
        self.name=name
        self.attack= attack
        self.defence = defence
        self.health = health

    def stats(self):
         print("name: ", self.name,)
         print("attack: ", self.attack,)
         print("defence: ", self.defence)
         print("health: ", self.health,)

class creature:
    def __init__(self,name, race, gender, attack, defence, health,):
        self.name = name
        self.race = race
        self.gender = gender
        self.attack = attack
        self.defence = defence
        self.health = health

    def stats(self):
         print("name: ", self.name,)
         print("race: ", self.race,)
         print("gender: ", self.gender,)
         print("attack: ", self.attack,)
         print("defence: ", self.defence)
         print("health: ", self.health,)


#  creatures
wolflvl1 = creature("wolf","wolf","male", 10, 5, 50)
# wepons
knife=wepon("knife",5,0,0)
melee=wepon("melee",0,0,0)
sword=wepon("sword",10,0,0)
# armor

# amulets

# variables
equipedwepon = melee.name
gold= int(100)


# lists/dictionary
inventory = {melee.name : melee.attack,}
wepons = [melee.name, knife.name, sword.name]

def equipwepon():
    if equipedwepon == "knife":
        return knife.attack + player.attack
    elif equipedwepon == "sword":
        return sword.attack + player.attack
    else:
        return melee.attack + player.attack

def shop (gold):
    print("gold: ", gold)
    choser=input("1. wepons  2. armor    3. amulets")
    if choser=="1":
        print("buy wepon")
        print("1. knife:",knife.stats())
        print("2. sword: ",sword.stats())
        choser=input("0. none 1. knife 2. sword")
        if (choser == "1" and gold >= 10):
            return "knife"
        elif (choser == "2" and gold>=50):
            return "sword"
        else:
            return
    elif choser=="2":
        return



caractername=input("enter your name")
caractergender="male"

print("chose gender")
print("1. male 2. female)")
choser = input("Choice")
if choser == "1":
    caractergender = "male"
elif choser == "2":
    caractergender = "female"

player = creature(caractername,"human",caractergender,10,10,50)
player_attack = player.attack + melee.attack
player.stats()


        


def forrest(player_attack,):
     while player.health >=0:
        print(player.stats, wolflvl1.stats)
        choser=input("1. attack 2. defece")
        if choser==1:
            wolflvl1.health= wolflvl1.health - player_attack 



while player.health>0:
    print("action")
    choser=input("1. go to shop 2. check inventory 3. equip")
    if choser== "1":
        bought =shop(gold)
        if bought == "knife":
            gold= gold-10
            inventory[knife.name] = knife.attack
        elif bought== "sword":
            inventory[sword.name] =sword.attack
            gold=gold-50
    elif choser== "2":
        print(inventory)
        choser=input( "write item name")
        if choser in wepons:
            equipedwepon= choser
            player_attack= equipwepon()
    elif choser == "4":
        player.stats()
        print("gold: ", gold)
        print(" attack: ", player_attack )
            

        
            
    elif choser=="3":
        print(equipedwepon)
    else:
        break
    



# wolflvl2 = creature("wolf","wolf","male", 15, 10, 60)

# banditlvl1 = creature("bandit", "human", "male", 10, (random.randint(5,10)), 40)
# banditlvl2 = creature("bandit", "human", "male", 10, (random.randint(10,15)), 60)

