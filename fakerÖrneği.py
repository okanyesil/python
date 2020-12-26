from faker import Faker

fake = Faker()

print("Name   :", fake.name())
print("Email  :", fake.email())
print("Country:", fake.country())
print("Text   :", fake.text())
print("Url    :", fake.url())
