#Ejemplo de diccionarios

#Create dictionary
alien_0 = {'color':'green','points':5}
print(alien_0)

#Adding new key-value pair
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#Modifying Values in a Dictionary
print("The alien is "+ alien_0['color']+ ".")

alien_0['color'] = 'yellow'
print("The alien is now" + alien_0['color'] + ".")

# Example 2 - MODIFYING VALUES 
alien_0['speed'] = 'medium' #creamos la clave speed

print("Original x-position: "+str(alien_0['x_position']))

#Move the alien to the rigth
#Determine how far to move the alien based on its current speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    #This must be a fast alien.
    x_increment = 3

#The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position is: "+str(alien_0['x_position']))

print(alien_0)

#Removing key-values Pairs
alien_test = {'color':'green','points':5}
print(alien_test)

del alien_test['points']
print(alien_test)

# A list of dictionaries
alien_0 = {}
alien_0 = {'color':'green','points':5}
alien_1 = {'color':'yellow','points':10}
alien_2 = {'color':'red','points':15}

aliens = [alien_0,alien_1,alien_2]

for alien in aliens:
    print(alien)


















