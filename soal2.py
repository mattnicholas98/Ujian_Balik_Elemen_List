def balikPosisi(x):
    # bkin empty list buat di append
    mylist = []

    # hitung lengthnya x (which is the list)
    length = len(x)

    # pake loop function
    for item in range(length):
        mylist.append(x[(length-item-1)])
    return mylist

# testing out results
print(balikPosisi([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(balikPosisi(['A', 'B', 'C', 'D', 'E', 'F', 'G']))
print(balikPosisi(['Messi', 'Suarez', 'Coutinho', 'Dembele', 'Rakitic']))