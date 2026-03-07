
person = {
    "name": "mendi",
    "age": 23,
    "course": "Python",
    "job" : "Developer",
    "salary" : "15000",
    "city" : "Tel aviv"
}

person["age"] = 35
print("Update age:", person["age"] )

person["job"] = "Senior Developer"
print("Update job:", person["job"])

person["salary"] = "20000"
print("Update salary:", person["salary"])

person["city"] = "Haifa"
print("The new city:", person["city"])      

# בדיקת קיום של מפתח במילון
if "age" in person:
    print("Age is in the dictionary.")
else:    print("Age is not in the dictionary.") 

if "phone" in person:
    print("Phone is in the dictionary.")        
else:    print("Phone is not in the dictionary.") 

for key, value in person.items():    
    print(f" {key} : {value}")     

server = {
    "hostname":"mylinux",
    "ip" : "127.0.0.1",
    "os" : "Ubuntu",
    "cpu_cores" : "100%cpu",
    "status" : "running",
}

print(server["status"])

users = [
    {"name": "David", "age": 30},
    {"name": "Moshe", "age": 16},
    {"name": "Noa", "age": 49},
    
]

# for i in users:
#     if i ["age"] > 30:
#      print(f"User over 30: {i["name"]} age: {i["age"]}")

users.append({"name": "Noa", "age": 22},)

# print("---Updated User List ---")
# for user in users:
#     print(user)

for i in users:
    print(f"{i["name"]} is {i["age"]} years old")

inventory = {
    "name" : "banana",
    "price" : 3500,
    "quantity" : 3,
}

total_price = inventory["price"] * inventory["quantity"]

print(f"The total price for {inventory['name']} : {total_price}")
