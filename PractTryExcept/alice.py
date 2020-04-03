#Handling the FileNotFoundErrorException

filename = 'alice.txt'

try:
    with open(filename) as file:
        contents = file.read()

except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)

else:
    #Count the aproximate number of words in the file
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")


#
