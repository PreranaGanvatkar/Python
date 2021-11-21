while True:
    print("Who are you?")
    name=input()
    if name!="abc":
        continue
    print("Hello,abc.What is the password")
    password=input()
    if password=="xyz":
        break
print("Access granted")