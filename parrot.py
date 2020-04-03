#How the imput function work!
#Uso de while con un Flag para detener la ejecucion del programa

prompt = "\n Tell me something, and I will repeat it back to you"
prompt += "\n Enter 'quit' to end the program: "

active  = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)


    
