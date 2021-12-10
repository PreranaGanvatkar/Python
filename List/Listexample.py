#List Data type

# catName1='Zophie'
catName2='Pooka'
catName3='Simon'
catName4='Lady Macbeth'
catName5='Fat-tail'
catName6='Miss Cleo'


#(OR)
print("Enter the name of cat 1:")
catName1=input()
print("Enter the name of cat 2:")
catName2=input()
print("Enter the name of cat 3:")
catName3=input()
print("Enter the name of cat 4:")
catName4=input()
print("Enter the name of cat 5:")
catName5=input()
print("Enter the name of cat 6:")
catName6=input()

print("The cat names are:")
print(catName1+" "+catName2+" "+catName3+" "+catName4+" "+catName5+" "+catName6)

#Using while loop

catName=[]
while True:
    print("Enter the name of cat "+str(len(catName)+1)+"(or enter nothing to stop.)")
    name=input()
    if name=="":
        break
    catName=catName +[name]
print("The cat names are: ")
for name in catName:
    print(" "+name)

#Using For loop

supplies=['pens','staplers','flame-throws','binders']
for i in range(len(supplies)):
    print('Index '+str(i)+' in suplies is: '+supplies[i])


#in and not operator

myPets=['Zophie','Pooka','Fat-tail']
print("Enter a pet name:")
name=input()
if name not in myPets:
    print("I do not have a pet named "+name)
else:
    print(name +" is my pet.")

#Multiple assignment tricks

cat=['fat','black','loud']
size,color,disposition=cat
print("size of a cat "+size)
print("color of a cat "+color)
print("disposition is "+disposition)

#Assignment operator

spam=["Pooka"]
spam*=3
print(spam)