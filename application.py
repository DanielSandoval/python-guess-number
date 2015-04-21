# Aqui escribe tu codigo
import random
numero_random = random.randrange(1,21)
numero_ingresado = int(raw_input("Adivina el numero entre 1 y 20: "))
if numero_ingresado > numero_random:
	print "you guessed to high, please try again"
print numero_random