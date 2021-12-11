#indexing value


spam=['hello','hi','howdy','heyas']
print(spam.index('hello'))
print(spam.index('heyas'))
#print(spam.index('howdy howdy howdy'))

#append() and insert()

spam=['cat','dog','bat']
spam.append('moose')
print(spam)

spam=['cat','dog','bat']
spam.insert(1,'chicken')
print(spam)

spam=['cat','dog','bat']
spam.insert(4,'chicken')
spam.insert(3,'dog1')
print(spam)