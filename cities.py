#Uso de while con sentencia break

prompt = "\n Please enter the name of a city you have visitied"
prompt += "\n(Enter 'quit' when you are finished): "

while True:
    city  = input(prompt)

    if city == 'quit':
        break
    else:
        print("I'd love to go to "+city.title()+"!" )
