#!/usr/bin/python
# coding=utf-8

from gpiozero import LED

class Vumetre :
    """ Classe gérant un vumètre à LEDs
    (utilise la librairie GPIO ZERO 1.5)"""
    
    def __init__(self) :
        self.broches = [20, 16, 26, 19, 13, 6, 5, 22, 4, 23]
        self.leds = [LED(self.broches[0]),LED(self.broches[1]),LED(self.broches[2]),
                LED(self.broches[3]),LED(self.broches[4]),LED(self.broches[5]),
                LED(self.broches[6]),LED(self.broches[7]),LED(self.broches[8]),
                LED(self.broches[9])]
    
    def eteindre(self) :
        for x in range(len(self.leds)) :
            self.leds[x].off()
    
    def afficher(self,niveau=0) :
        # Extinction de toutes les LEDs d'abord
        for x in range(len(self.leds)) :
            self.leds[x].off()
        # Allume ensuite uniquement les LEDs concernées par la valeur de 'niveau'
        for x in range(niveau) :
            self.leds[x].on()
    
    def lire(self) :
        niveau = 0
        for x in range(len(self.leds)) :
            if self.leds[x].value == 1 :
                niveau = x +1    # car l'indice démarre à 0
        return niveau
    
    def inverser(self) :
        for x in range(len(self.leds)) :
            self.leds[x].toggle()