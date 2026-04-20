# person registration without menu or input

profile = {"name": "tiago", "email": "castelantiago@gmail.com", "age": 23}
print(f"Name: {profile['name']} Email: {profile['email']} Age: {profile['age']}")

profile.update({"email": "castelantiago2@gmail.com", "age": 24})
print(f"Name: {profile['name']} Email: {profile['email']} Age: {profile['age']}")

profile["phone"] = "(11) 99938-0440"
if profile.get("phone"):
    print(f"Name: {profile['name']} Email: {profile['email']} Age: {profile['age']} Phone: {profile['phone']}")

del profile["phone"]
print(f"Name: {profile['name']} Email: {profile['email']} Age: {profile['age']}", end=" ")
print(f"Phone: {profile.get('phone', 'N/A')}")
