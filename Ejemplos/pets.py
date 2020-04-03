#crear una lista de diccionarios

cuki = {'kind':'perro','owner':'milton'}
papa ={'kind':'perico','owner':'berta'}
pepper = {'kind':'perro','owner':'mimi'}

pets = []

pets.append(cuki)
pets.append(papa)
pets.append(pepper)

for pet in pets:
    print("Kind: "+pet['kind'])
    print("Owner: "+pet['owner'])
    print("\n")
