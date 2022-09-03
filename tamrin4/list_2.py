import random
number=int(input("Enter number in list : "))
list=[]
count = 0
while number > count :
        Number=random.randint(0,1000)
        if not Number in list :
             list.append(Number)
             count += 1  
print(list)