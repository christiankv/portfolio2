import time
import random

class caracter:
    def __init__(self,player,race):
        # caracter card
        self.name = ""
        self.race = race
        self.gender = "" 
        self.player = player
        # caracter stats
        self.health = 50
        self.attack = 5
        self.defence = 2
        self.defencebonus = 1.1
        self.attackbonus = 1.1
        # caracter levels
        self.level = 1
        self.skin =1
        self.muscles = 1
        self.attackskill = 1
        self.defenceskill = 1
        self.trainingslot = 10
        # EXP area
        self.baseXP = 0
        self.musclesXP = 0
        self.attackskillexp = 0
        self.defenceskillexp = 0
        self.skinXP = 0

    def stats(self):
        print(self.name, " ", self.race)
        print("level: ", self.level, "exp: ", self.baseXP)
        print("health: ",self.health,"defence: ", self.defence,"attack: ", self.attack)
        print("defenceskill ",self.defenceskill,"attackskill: ", self.attackskill)
        print("muscles: ", self.muscles, "musclesXP: ", self.musclesXP,)
        print("skin: ", self.skin, "skinXP: ", self.skinXP)
        print("training available:", self.trainingslot)

    def caractercreation(self):
        if self.player == "player":
            self.name = input("your name:")
            print("chose your gender")
            print("1: male, 2: female")
            choser = input("choice)")
        else:
            if self.race == "human":
                self.name= self.race + "bandit"

            elif self.race == "wolf":
                self.name = self.race + "hunter"
            choser = random.randint(1,2)
        try:
            choser= int(choser)
            if choser == 1:
                self.gender = "male"
            elif choser == 2:
                self.gender = "female"
        except:
            self.gender = "male"


    

    def rest(self):                   
        wait =10
        while wait > 0:  
            print(wait)  
            time.sleep(1)   
            wait -=1
        self.health = 50*self.level

    def levelup(self, stat, value):
        if stat == "skin":
            self.skinXP += value
            self.baseXP += value/4
            if self.skinXP >= 100 :
                self.skinXP = self.skinXP % 100
                self.skin += 1
                self.defence = 2*self.skin
                print("skin level up")
                self.levelup("skin", 0)
                

        elif stat == "muscle":
            self.musclesXP += value
            self.baseXP += value/4
            if self.musclesXP >= 100 :
                self.musclesXP = self.musclesXP % 100
                self.muscles += 1
                self.attack = 5*self.muscles
                print("muscles level up")
                self.levelup("skin", 0)
                return
        elif stat == "skill":
            if self.defenceskillexp >= 100:
                self.defenceskillexp = self.defenceskillexp % 100
                self.defenceskill += 1
                self.defencebonus+= 0.1
                
                print("defence skill level up")
                self.levelup("skill", 0)
            elif self.attackskillexp >= 100:
                self.attackskillexp = self.defenceskillexp % 100
                self.attackskill += 1
                self.attackbonus+= 0.1
                print("attack skill level up")
                self.levelup("skill", 0)

        else: return
        if self.baseXP >= 100 :
                self.baseXP = self.baseXP % 100
                self.level += 1
                self.health = 50*self.level
                print("skin level up")       

    def training(self):
        if self.trainingslot >0:
            print("1. train skin")
            print ("2 train muscles")
            if self.player == "player":
                choser = input("chose")
            else:
                choser = random.randint(1,2)

            try:
                choser =int(choser)
                if choser == 1 :

                    wait =2

                    while wait > 0:  
                        print(wait)  
                        time.sleep(1)   
                        wait -=1

                    self.trainingslot -= 1
                    value = 0.1*self.skin
                    exp = int(10/ value)
                        # print(value)
                        # print(exp)
                    print("gained "+ str(exp)  +" skin XP")
                    self.levelup("skin",exp)

                elif choser == 2 :
                    wait =2
                    while wait > 0:  
                        print(wait)
                        time.sleep(1)   
                        wait -=1
                    self.trainingslot -= 1
                    value = 0.1*self.muscles
                    exp = int(10/ value)
                        # print(value)
                        # print(exp)
                    print("gained "+ str(exp)  +" muscle XP")
                    self.levelup("muscle",exp)
            except: 
                print("failed")
                pass
        else: 
            print("cant train more go fight more monsters")

    def fight(self, target):
        while self.health > 0 and target.health > 0:
            print("player health", self.health, "enemy health", target.health)
            print("1. attack")
            print("2. defend")
            choser = input("chose:")
            try:
                choser = int(choser)
                if choser == 1:
                    dmg = self.attack * self.attackskill - target.defence
                    target.health -= dmg
                    self.health -= target.attack * target.attackskill -target.defence
                    value = 0.05*dmg*self.attackskill
                    exp = int(10/ value)
                    self.attackskillexp+= exp
                elif choser == 2:
                    defence = self.defence*self.defenceskill
                    self.health -= target.attack * target.attackskill - defence
                    value = 0.05*defence*self.defenceskill
                    exp = int(10/ value)
                    self.defenceskillexp+= exp

                    

            except:
                return
        self.levelup("skill",0)

















