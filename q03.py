alt = float(input("Enter altitude in m: "))
print("Boiling temperature at %dm is %dC" % (alt // 300 * 300, 100 - (alt // 300)))