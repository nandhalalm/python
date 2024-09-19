a=int(input("enter the persons to create"))
dict={}
for i in range(a):
    dict1={}
    name=input("enter name")
    age=int(input("enter age"))
    address=input("enter address")
    dict1["name"]=name
    dict1["age"]=age
    dict1["address"]=address
    dict[i+1]=dict1
print("the dictionar",dict)


