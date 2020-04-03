#Manejar listas con while loops

#Star with users that need to be verified,
#and  a empty list  to hold confirmed users.

unconfirmed_users = ['alice','brian','candace']
confirmed_users = []

#Verify each user until there are no more unconfirmed user.
#Move each verified user into the list of confirmed user.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying user:  "+current_user.title())
    confirmed_users.append(current_user)

#Display all confirmed users.
print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())





