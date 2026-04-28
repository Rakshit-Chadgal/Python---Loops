#Q1: Print "Hello" 5 times using a while loop.
'''count = 1
while count<=5:
    print("Hello")
    count+=1'''

#Q2: Print numbers from 1 to 100 using a while loop.
'''num = 1
while num<=100:
    print(num)
    num+=1'''

#Q3: Print numbers from 100 to 1 using a while loop.
'''num = 100
while num>=1:
    print(num)
    num-=1'''

#Q4: Print the elements of the list: [1, 4, 9, 16, 25, 36, 49, 64, 81,100] using a loop:
'''list = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
i = 0
while i<len(list):
    print(list[i])
    i+=1'''

#Q5: Search for a number x in this tuple using loop: [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
'''tup = (1, 4, 9, 16, 25, 36, 49, 64, 81,100)
x = int(input("Enter a number to search: "))
i = 0
found = False
while i<len(tup):
    if tup[i] == x:
        found = True
        print(x, "is found in the tuple.")
        break
    i+=1
if not found:
    print(x, "is not found in the tuple.")'''

#Q6