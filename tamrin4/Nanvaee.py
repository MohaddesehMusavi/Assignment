list = ["ali","atefe","reza","homa","amir","fateme"]
print(list)
for i in range(3) :
    name = input("Enter name "+str(i+1)+": ")
    num = int(input("Enter location"+str(i+1)+": "))
    list.insert(num-1,name)
print(list)
