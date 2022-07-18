# Python progarm to return function 
# by default
print("This program is to return function by default")

def function():
    return ()

print()

# program to return the maximum numbers

num_lst = []

for i in range(3):
    num = input("Enter number{}: ".format(i + 1))
    num_lst.append(int(num))

# Assigning the result to max_num

max_num = max(num_lst)
print(max_num)

