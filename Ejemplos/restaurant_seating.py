#Validar numero de personas para una mesa

cantidad_personas = input("Cuantos invitados vendran a cenar?: ")
cantidad_personas = int(cantidad_personas)

if cantidad_personas > 8:
    print("Tienen que esperar por una mesa.")
else:
    print("Su mesa esta lista.")
