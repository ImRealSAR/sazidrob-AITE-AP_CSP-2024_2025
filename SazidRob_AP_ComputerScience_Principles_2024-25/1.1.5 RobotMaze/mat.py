a = [ 1, 2, 3, 4, 5, 6, 7]
s= 0
for i in range(len(a)):
    s *= a[i]
    print(f"Total is now {s}")


""" aList = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
for i in range(len(aList)-1, -1, -1):
    if len(aList[i]) < 5:
        #aList.remove(aList[i])
        aList.pop(i)
print(aList) """