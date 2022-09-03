list = []
for num in range(10):
    print("Enter number",num+1,":")
    list.append(int(input()))

for i in range(len(list)): 

    if list[i-1] < list[i]  or  list[i-1] > list[i]:
        temp = True
        continue
    else:
        temp = False

if  temp == True:
        print("yes :)")
else:
        print("no :(")
