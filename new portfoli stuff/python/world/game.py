import random
from caracter.caracter import caracter
from map.forrest import location



player = caracter("player", "human")
forrest = location("forrest",10,"wolf")

player.caractercreation()

player.stats()

while player.health > 0:
    forrest.camp("player",player)