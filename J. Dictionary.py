# Chapter 1
import datetime
import pprint
import bcrypt
import json

Password: str = "DefaultPassword"
Salt = Password.encode("utf-8")
Hash = bcrypt.gensalt()
User: dict = {
    "Id": 1,
    "FullName": "Muhamad Rizki Arif Fadillah",
    "Email": "muriarfad@gmail.com",
    "Adress": "Purwakarta, West Java, Indonesia",
    "Password": bcrypt.hashpw(Salt, Hash),
    "CreatedAt": datetime.datetime.now(),
    "UpdatedAt": datetime.datetime.now(),
}

print(User)

# Pretty print
pprint.pprint(User)

# Chapter 2

Users: dict = {
    "Id": 1,
    "FullName": "Muhamad Rizki",
    "Email": "muriarfad@gmail.com",
    "CreatedAt": str(datetime.datetime.now()),
    "UpdatedAt": str(datetime.datetime.now()),
}
print(Users)
pprint.pprint(Users)

Users = dict(
    set="Id",
    FullName="Kibo",
    Email="muriarfad@gmail.com",
    CreatedAt=datetime.datetime.now(),
    UpdatedAt=datetime.datetime.now(),
)
print(Users)
pprint.pprint(Users)

Users = dict([
    ('set', 'id'),
    ('FullName', 'Bokir'),
    ('Email', 'muriarfad@gmail.com'),
    ('CreatedAt', str(datetime.datetime.now())),
    ('UpdatedAt', str(datetime.datetime.now())), ]
)
print(Users)
Users = dict()
print(Users)
Users = {}
print(Users)

# Chapter 3
for key in User:
    print(f"{key}: {User[key]}")

# Chapter 4 Nested

Customers: dict = {
    "Id": 1,
    "FullName": "Kibo",
    "Hobies": ["Learning", "Taking videos", "Teaching"],
    "Email": "muriarfad@gmail.com",
    "Skills": ["Python Developer", "Pentester"],
    "IsFemale": False,
    "Affiliations": [
        {
            "Name": "Bokir",
            "Affiliation": "Twin"
        },
        {
            "Name": "Rizki",
            "Affiliation": "Same person"
        },
    ],
}
print(Customers)
for item in Customers["Affiliations"]:
    print(" -> %s (%s)" % (item["Name"], item["Affiliation"]))

# Chapter 4 Dictionary Mutability

Customers["Affiliations"][1]["Name"] = "Arif"
Customers["Affiliations"][1]["Affilitaion"] = "Midle of name"
pprint.pprint(Customers)

# Chapter 5: Dictionary Operation
# Access Dictionary
print(Customers['Id'])
# Change Dictionary
Customers['FullName'] = "Muhamad Rizki Arif Fadillah"
print(Customers['FullName'])
# Add Item
Customers["Password"] = bcrypt.hashpw(bytes("Kibo".encode("utf-8")), bcrypt.gensalt())
pprint.pprint(Customers)
# Delete key
Customers.pop("Password")
pprint.pprint(Customers)
# Access dictionary keys and value
Keys: list = list(Customers.keys())
Value: list = list(Customers.values())
print(f"Keys{Keys}\nValue{Value}")
Items: list = list(Customers.items())
print(Items)
# Copy Dictionary
Customers2 = Customers.copy()
print(Customers2)
# Clear Dictionary
Customers2.clear()
print("Customer 2 %a" % Customers2)