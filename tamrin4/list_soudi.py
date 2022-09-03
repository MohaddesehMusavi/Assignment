list = []
for i in range(10):
    number = int(input("Enter number "+str(i+1)+": "))
    list.append(number)
print("first list  :",list)
for i in range(len(list)):
    for j in range(i+1,len(list)):
        if list[i] > list[j] :
            list[i],list[j] = list[j],list[i]
print("secend list :",list)
 