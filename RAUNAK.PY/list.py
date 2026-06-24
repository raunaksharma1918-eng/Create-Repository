#print positive and negative elements of an list.
l = [10,-9,20,30,-12,-15]
neg = []
pos = []

for i in l:
    if i < 0:
        neg.append(i)
    else:
        pos.append(i)
print(neg)
print(pos)

