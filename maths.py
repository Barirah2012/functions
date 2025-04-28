def add(p,q):
    return p+q
def sub(p,q):
    return p-q
def mul(p,q):
    return p*q
def div(p,q):
    return p/q
print("plz sellect operation")
print("a.add")
print("b.sub")
print("c.mul")
print("d.div")
choice = input("plz enteryour choice (a/b/c/d)")
num_1 = int (input("plz enter first num :"))
num_2 = int (input("plz enter second num :"))
if choice == 'a':
    print(num_1,"+",num_2,"=",add(num_1,num_2))
elif choice == 'b':
    print(num_1,"-",num_2,"=", sub(num_1,num_2))
elif choice == 'c':
    print(num_1,"*",num_2,"=",mul(num_1,num_2))
elif choice == 'd':
    print(num_1,"/",num_2,"=",div(num_1,num_2))
else:
    print("invalid choice")
