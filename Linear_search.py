list = [0,1,2,3,4,5,6,7,8,9,10,11]

print(list)

found = False

x = int(input("Hello there! please choose a number, and we'll see if its' in our list! "))

for i in range(0,len(list)):
    if list[i] == x:
        print("That number is indeed in our list!")
        found = True
        break

if found == False:
    print("Sorry, that isn't available at this moment.")