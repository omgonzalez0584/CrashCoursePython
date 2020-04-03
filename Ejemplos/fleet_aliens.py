#make an empty list for storing alien
aliens = []

#Make 30 green aliens
for alien_number in range(30):
    new_alien = {
        'color':'green',
        'points':5,
        'speed':'slow'
        }
    aliens.append(new_alien)

#Cambiar los 3 primeros aliens a amarillo
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10


#show the  first 5 aliens
for alien in aliens[:5]:
    print(alien)
print(".....")

#show how many alien have been created
print("Total number of alien: "+str(len(aliens)))
