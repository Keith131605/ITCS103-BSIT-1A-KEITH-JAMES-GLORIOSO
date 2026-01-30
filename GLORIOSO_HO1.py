w = input("please enter a word -> ")
length = len(w)

l = []

for i in range(length):
    num = eval(input(f"Enter a Number {i + 1}:"))
    l.append(num)

def average(num):
    return sum(num) / len(num)

def compare(length, average, w):
    if length > average:
        result = "greater than"
    elif length < average:
        result = "less than"
    else:
        result = "equal to"

    print(f"The length of the word '{w}' is {result} the average.")

average = average(l)

print(l)
print("the length of the word is:",length)
print("the avarage of the number is",average)

compare(length, average, w)