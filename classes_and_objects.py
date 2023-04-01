class PII:
    first = ""
    last = ""
    address = ["", "", "", ""]

    def fullname(self):
        return self.first + " " + self.last

markr = PII()
ronnier = PII()
richc = PII()



markr.first = "Mark"
markr.last = "Robinson"

ronnier.first = "Ronnie"
ronnier.last = "Robinson"

richc.first = "Rich"
richc.last = "Cheney"

for person in [markr, ronnier, richc]:
     print(person.fullname())