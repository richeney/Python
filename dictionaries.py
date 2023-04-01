phonebook = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}
# del phonebook["John"]
for name, number in phonebook.items():
    print("Phone number is %d for %s" % (number, name))

# testing code
if "Jake" in phonebook:
    print("Jake is listed in the phonebook.")

if "Jill" not in phonebook:
    print("Jill is not listed in the phonebook.")

print(phonebook)

phonebook = {
    "John" : {
      "Surname" : "Smith",
      "Middle Name" : "James",
      "Phone" : 938477566,
    },
    "Jill" : {
      "Surname" : "Swill",
      "Phone" : 938477565,
    },
}

print(phonebook)
print(phonebook["John"])
print(phonebook["John"]["Surname"])
