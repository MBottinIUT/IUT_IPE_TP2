class De_a_jouer :# Rem : un nom de classe commence par une majuscule
				# contrairement a une variable
	
	# La methode __init__ permet de definir
	# les attributs de l'objet lors de son instanciation
	def __init__(self) :
		self.valeur = '1'
        
	# La methode 'lancer_de' simule le lancer de de
	def lancer_de(self) :
		self.valeur = random.randint(1,6)
		return self.valeur
        
	# La methode 'affichage_de' affiche dans le terminal la face du de
	def affichage_de(self, valeur='1') :
		for ligne in range(len(Valeurs_de['1'])):
			print(Valeurs_de[str(self.valeur)][ligne])

			
			