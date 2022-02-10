A = 1
B = 2

# if
if A == 1:
    print(True)
else:
    print(False)

if A == 1:
    print(True)
    if B == 2:
        print("Yes")
elif A == 2:
    print("Es igual a 2")
else:
    print(False)

# while
while A <= 10:
    print(A)
    A = A + 1
    A += 1

array = [1,2,3,4,5,6,7,100,76]
print("El array es igual a: ", array)
for i in array:
    print("Originalmente era: ", i)
    print("Luego: ", i*10)