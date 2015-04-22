# Aqui escribe tu codigo
import random

numero_random = random.randrange(1,21)

turno = 4
for turnoNumero in range(1,turno+1):
	print "Vas en el turno:", turnoNumero
	if turnoNumero < 5:
		numero_ingresado = int(raw_input("Adivina el numero entre 1 y 20: "))
		if numero_ingresado == numero_random:
			print "you win!"
			break
		elif numero_ingresado != numero_random and turnoNumero < 5:
			if numero_ingresado > numero_random:
				print "you guessed to high, please try again"
			elif numero_ingresado < numero_random:
				print "you guessed to low, please try again"
			turnoNumero += 1
		if turnoNumero == 5:
				print "Game Over"

print "Este era el numero generado:", numero_random