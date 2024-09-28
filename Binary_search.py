list = [0,1,2,3,4,5,6,7,8,9,10,11]

x = int(input("Hello! Please state the number you wish to search! "))

start = 0

end = len(list) - 1

found = False

while start <= end:
    mid = (start + end) // 2
    if x == list[mid]:
        print("The number is indeed in our database!")
        found = True
        break
    elif x < list[mid]:
        end = mid - 1
    else:
        start = mid +1
if found == False:
    print("Sorry, we are out of that number.")