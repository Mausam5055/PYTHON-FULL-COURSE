t = list(range(2,21,2))
v = [10, 18, 25, 29, 32, 20, 11, 5, 2, 0]

dist = 0
t[-1] = 0
for i in range(len(t)):
    dist += v[i]*(t[i]-t[i-1])

print(dist)
