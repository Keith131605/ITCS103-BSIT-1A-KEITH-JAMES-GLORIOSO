w = input("please enter a word -> ")
length = len(w)

l = []

for i in range(1,7):
    num = eval(input(f"Enter a Number {i}:"))

    l.append(num)
apple = sum(l)
banana = len(l)
car = apple/banana

print(l)
print("the length of the word is:",length)
print("the avarage of the number is",car)
if apple > length:
    print("The length of the word",w,"is greater than the avarage.")
elif apple < length:
    print("The length of the word",w,"is less than the avarage.")
else:
    print("The length of the word",w,"is equal than the avarage.")