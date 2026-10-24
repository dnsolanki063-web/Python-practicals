#assignment pre_5

basket = ('Orange','Banana','Cherry','Kiwi')
basket = ('Mango',)+basket + ('Greps',)
if 'Mango' in basket:
    print("Mango is in the tuple")
else:
    print("Mango is not in the tuple")

print('length of tuple is:',len(basket))

print("First item of the tuple",basket[0])
print("second item of the tuple",basket[1])
print("third item of the tuple",basket[2])
print("fourth item of the tuple",basket[3])
print("fifth item of the tuple",basket[4])
print("last item of the tuple",basket[5])

print("\n\nsixth item of the tuple",basket[-1])
print("fifth item of the tuple",basket[-2])
print("fourth item of the tuple",basket[-3])
print("third item of the tuple",basket[-4])
print("second item of the tuple",basket[-5])
print("first item of the tuple",basket[-6])
