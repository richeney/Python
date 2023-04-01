x = 2
print(x == 2) # prints out True
print(x == 3) # prints out False
print(x < 3) # prints out True

name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")

name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")

statement = False
another_statement = True
if statement is True:
    # do something
    pass
elif another_statement is True: # else if
    # do something else
    pass
else:
    # do another thing
    pass

x = 2
if x == 2:
    print("x equals two!")
else:
    print("x does not equal to two.")

array = ["Hello", "World"]
if array:
    print("Array is not empty")

x = [1,2,3]
y = [1,2,3]
print(x == y) # Prints out True
print(x != y) # Prints out False
print(x is y) # Prints out False

print(not False) # Prints out True
print((not False) == (False)) # Prints out False

# change this code
number = 20
second_number = 0
first_array = [1,2,3]
second_array = [1,2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")

| Type | False | True |
|---|---|---|
| Boolean | False | True |
| Integer | 0 | Any other integer |
| Float | 0.0 | Any other float |
| String | "" | Any other string |
| List | [] | Any other list |
| Tuple | () | Any other tuple |
| Dictionary | {} | Any other dictionary |

x = 0
x = 0.0
x = ""
x = []

y = ["Hello", "World"]

if len(second_array):
    print("Hooray, my array is empty!")


second_number = 10
if second_number:
    print("Number is not zero")
