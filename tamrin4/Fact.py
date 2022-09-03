fact = int(input("Please Enter a  number : "))
for num in range(1,fact-1):
    fact //= num
    if fact == 1:
        temp = True
        break
    else:
        temp = False
if temp == True:
    print("Yes ")
else:
    print("No ")



