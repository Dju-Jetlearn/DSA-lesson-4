list = ["A","a","B","b","C","c","D","d","E","e","F","f","G","g","H","h","I","i","J","j","K","k","L","l","M","m","N","n","O","o","P","p","Q","q","R","r","S","s","T","t","U","u","V","v","W","w","X","x","Y","y","Z","z"]

print(list)

found = False

x = input("Hello there! Please choose a character, and we'll see if it's in the English alphabet! ")

for i in range(0,len(list)):
    if list[i] == x:
        print(x + " is indeed in the English alphabet! Good job!")
        found = True
        break

if found == False:
    print("Sorry, that isn't an English letter. Please try again buddy.")