
i = 3
j = 5
k = 7


if i < j:
    if j < k:
        i = j
    else:
        j = k
else:
    if j < k:
        j = i
    else:
                 	i = k
print(i,j,k)