count = int(input("Enter a number : "))
list = []
List = []
for num in range (count) :
    print("Enter name "  ,num+1 ,": ")
    list.append(input())
print("list =",list)
for name in list :
    if not name in List :
        List.append(name)
    else :
        continue 

for name in List :
    temp = 0
    for Name in list :
        if name == Name :
            temp += 1
    print (name," number in list =",temp)





