
def printing_models(unprinted_designs, completed_models):
    #Loop while imprimiendo los designs que estan en la lista
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing Model: "+current_design)
        completed_models.append(current_design)

#Muestra los designs ya impresos
def show_completed_models(completed_models):
    print("\nThe Following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

#Cuerpo principal del programa
unprinted_designs = ['iphones case', 'robot pendant','dodecahedron']
completed_models = [] #Lista vacia que guarda los modelos impresos

#Llamada a las funciones 
printing_models(unprinted_designs[:], completed_models) #[:] Esta enviando una copia de la lista
print(unprinted_designs)
show_completed_models(completed_models)




