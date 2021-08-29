from itertools import permutations
def combined(list):
    output = []
    for i in permutations(list, len(list)):
        output.append("".join(map(str,i)))
    return max(output)

list = []
n = int(input("Enter how many ELEMENTS you want in the LIST : "))

for i in range(0, n):
    element = int(input("Enter the number  into list : "))
    list.append(element)
    
print("The largest possible combined number is : ", combined(list))

