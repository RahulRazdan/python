names = ["Rahul","Razdan","testing"]

for name in names:
    print(name)
    
print(""" In 2009,
                    we starting testing our application and
                    it did not work out well.""")

for i in [1,2,3,4,5]:
    print(str(i))

value = input("Enter something")
print(value)

isNext = True
while isNext:
    userinput = input("do you want to continue")
    if userinput == "Yes":
        print("Good")
    else:
        isNext = False


        