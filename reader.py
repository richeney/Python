class User:
    first = ""
    last = ""
    age = int(0)
    height = int(0)

    def output(self):
        return("%s %s is %s years old." % (self.first,self.last,self.age))

users = []

f = open('./mydata.csv', 'r')

for myline in f.read().splitlines():
    u = User()
    [u.first, u.last, u.age, u.height]  = myline.split(',')

    users.append(u)

f.close()

print(len(users))

f = open("output.txt", "w")
f.write("This is the first line\n")
f.write("This is the second line\n")

for user in users:
    f.write(user.output())
    f.write("\n")

f.write("This is the last line\n")
f.close()