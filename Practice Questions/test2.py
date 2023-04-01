class User:
    first_name = ""
    height = 0
    email = ""

    def print_info(self):
        print(self.first_name, self.height, self.email)

    def height_info(self):
        if self.height < 100:
            # inches
            return("%s is %d inches high" % (self.first_name, self.height))
        else:
            # cms
            return("%s is %dcm high" % (self.first_name, self.height))

def get_info():
    myuser = User()

    myuser.first_name = input("Enter your first name: ")
    myuser.email = input("Enter your email: ")
    myuser.height = input("Enter your height: ")

    # Does some checks here
    return(myuser)

# Main

userdb = []


# info and checks
new_user = get_info()

userdb.append(new_user)


for user in userdb:
    user.print_info()
