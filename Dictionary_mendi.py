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

