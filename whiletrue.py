i=1
while True:
     print("1 register \n 2 exit ")
     n=input("enter options")
     if n=="1":
           a=int(input("enter the persons to create"))
           dict={}
          
           dict1={}
           name=input("enter name")
           age=int(input("enter age"))
           address=input("enter address")
           dict1["name"]=name
           dict1["age"]=age
           dict1["address"]=address
           dict[i]=dict1
           i=i+1
           print("the dictionar",dict)
     elif n=="2":
          break
     else:
          print("invalid choice")
       

