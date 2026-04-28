#Prints the multiplication table of a number 'n'
n = int(input("Enter a number: "))
print("Multiplication Table of", n, "is:")
i = 1
while i<=10:
    print(n, "x", i, "=", n*i)
    i+=1