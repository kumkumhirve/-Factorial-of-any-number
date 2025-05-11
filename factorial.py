
'''Q11: Write a program to calculate Factorial of any number.'''

num = int(input("enter the number :"))
fact = 1

for i in range (1,num):
    fact = fact * num
    num-=1
    print(fact)


