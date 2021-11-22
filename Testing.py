import math

print("Enter the first list")
a = str(input("Enter the a: "))
b = str(input("Enter the b: "))
c = str(input("Enter the c: "))

list1 = [a, b, c]
print("The list are ",list1)

print("\nEnter the second list")
d = str(input("Enter the d: "))
e = str(input("Enter the e: "))
f = str(input("Enter the f: "))

list2 = [d, e, f]
print("The list are ",list2)

selection = input("\nDoes both of the list correct ?(yes or no): ")
list1.extend(list2)
Total_list = list1

if selection == 'yes':
  print(Total_list)
else:
  x = int(input("Enter the alphabet to change: "))
  y = str(input("Enter the change value: "))
  Total_list[x] = y
  print(Total_list)
