
ordinal_numbers = list(range(1,10))

for ordinal in ordinal_numbers:
    if ordinal == 1:
        print(str(ordinal)+"st")
    elif ordinal == 2:
        print(str(ordinal)+"nd")
    elif ordinal == 3:
        print(str(ordinal)+"rd")
    else:
        print(str(ordinal)+"th")


