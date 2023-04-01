# Modify this function to return a list of strings as defined above
def list_benefits():
    return [
        "More organized code",
        "More readable code",
        "Easier code reuse",
        "Allowing programmers to share and connect code together"
        ]

def build_sentence(info):
    return info + " is a benefit of functions!"


# Main function
mylist = list_benefits()

for benefit in list_benefits():
    mystr = build_sentence(benefit)
    print(mystr)