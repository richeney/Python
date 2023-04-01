def myinfofunction(userinfo):
    print("User %s lives at %s." % (userinfo["first_name"], userinfo["address"]["postcode"]))
    print("%s is %dcm high" % (userinfo["first_name"], userinfo["height"]))

details = {
    "rpjcheney@gmail.com": {
        "first_name": "Richard",
        "last_name": "Cheney",
        "age": 51,
        "height": 73,
        "email": "rpjcheney@gmail.com",
        "address": {
            "first_line": "1 Main Street",
            "second_line": "",
            "town": "Manchester",
            "postcode": "B1 1AA"
        }
    },
    "ronnielsrobinson@gmail.com": {
        "first_name": "Ronnie",
        "last_name": "Robinson",
        "age": 51,
        "height": 192,
        "email": "ronnielsrobinson@gmail.com",
        "address": {
            "first_line": "1 Main Street",
            "second_line": "",
            "town": "Birmingham",
            "postcode": "B1 1AA"
        }
    }
}

for email_key, user_object in details.items():
    myinfofunction(user_object)