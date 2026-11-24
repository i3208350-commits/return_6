
# תרגיל 1
# numbers =( 10, 20, 30, 40, 50)
# print(numbers)
# print(numbers[0],[-1])
# print(len(numbers))
# print(numbers[2])

# תרגיל 2
# numbers =( "itamar", "tehila", "aila", "david")
# for i in numbers:
#     print(i)
# if "dana" in numbers:
#     print("aaaa")
# print(len(numbers))

# תרגיל 3
# numbers =( 10, 20, 30, 40, 50)
# print(numbers[:3])
    
# print(numbers[2:])
    
# print (numbers[::-1])
    
# תרגיל 4
# prodakt=("mit",20,6,"food")


# תרגיל 5
# print(prodakt[0])
# print(prodakt[1])
# print(prodakt[2])
# print(prodakt[3])

# תרגיל 6
# numbers =( 10, 20, 30, 40, 50)
# total=0
# for i in numbers:
#     total+=i
# print(total)


# numbers =( 10, 20, 30, 40, 50)
# total=0
# examination=0
# for i in numbers:
#     if i%2==0:
#        examination+=1
#     if i>total:
#       total=i
# print(total)
# print(examination)

# תרגיל 7

# products = ("Laptop", "Mouse", "Keyboard", "Screen", "Printer")
# tuple_1=products[0:3]
# tuple_2=products[2:5]
# tuple_3=tuple_1+tuple_2
# print(tuple_1)
# print(tuple_2)
# print(tuple_3)

# תרגיל 8
# student = {    "name": "David",    "age": 22,    "grade": 95}print(student["name"])
# student["age"] = 23
# student["city"] = "Tel Aviv"
# print(student)

# # תרגיל 7
# student={"name": "itamar", "age" : 26, "grade": 100, "city": "elad"} 
# print(student["name"])
# print(student["age"])
# print(student["grade"])
# print(student["city"])

# תרגיל 8
# car={"brand" : "Mercedes", "model": "x6", "year": 2012, "price": 200000}
# car["price"]=300000
# car["year"]=2020
# car["color"]="red"
# print(car)

# # תרגיל 9
# salaries = {    "David": 12000,    "Moshe": 15000,    "Dana": 13500}
# for i,k in salaries.items():
#     print(k)
# salaries["Dana"]=13000
# salaries["ana"]=10000
# print(salaries)

# # תרגיל 10
# prodakts={"mit":100, "bread":12, "water":8}
# prodakt=input("Enter a product name")
# if prodakt in prodakts:
#     print(prodakts[prodakt])
# else:
#     print("eror")

# תרגיל 11

# Student = {    "David": 90,    "Moshe": 75,    "Dana": 100,    "Noa": 55,    "Avi": 82}
# for i,k in Student.items():
#     print(i,k)
    

# # תרגיל 12
# total=0
# total_max=0
# total_name=0
# grades = {    "David": 90,    "Moshe": 75,    "Dana": 100,    "Noa": 55,    "Avi": 82}
# for i,k in grades.items():
#     if k>=80:
#         print(i)

#     if k<60:
#         total+=1
#     if k>total_max:
#         total_max=k
#         total_name=i

# print(total_name,total_max)
# print(total)

# # תרגיל 13
# prodakts={"mit":100, "bread":12, "water":8}
# pridakt=input("Enter a product name")
# if pridakt not in prodakts:
#    price=int(input("Enter a price there"))
#    prodakts[pridakt]=price
# else:
#    print("eror")
# print(prodakts)

# # תרגיל 14 
# total=0
# maxi=0
# total_name=0
# students = [    {"name": "David", "age": 20, "grade": 90},    {"name": "Moshe", "age": 22, "grade": 75},    {"name": "Dana", "age": 21, "grade": 100},    {"name": "Noa", "age": 19, "grade": 55},    {"name": "Avi", "age": 23, "grade": 82}]
# for i in students:
#     print (i["name"])
#     print(i["grade"])
#     if i["grade"]>80:
#         print(i["name"])
#     if i["grade"]>total:
#         total=i["grade"]
#         total_name=i["name"]
#         maxi+=i["grade"]
    
# print(total_name)
# print(maxi/len(students))
  
# תרגיל 15

# students = [    {"name": "David", "age": 20, "grade": 90},    {"name": "Moshe", "age": 22, "grade": 75},    {"name": "Dana", "age": 21, "grade": 100},    {"name": "Noa", "age": 19, "grade": 55},    {"name": "Avi", "age": 23, "grade": 82}]
# students.append({"name":"itamar","age":26,"grade":100})
# print(students)

# תרגיל 16
# classroom = {    "Class A": ["David", "Moshe", "Dana"],    "Class B": ["Noa", "Avi", "Michael"],    "Class C": ["Daniel", "Shir", "Yossi"]}
# for i,k in classroom.items():
#     print(i)
#     if i=="Class A":
#         print(k)
#     if i=="Class B":
#         k.append("mmm")
#     if i=="Class C":
#         k.pop()
#     print(len(k))
# print(classroom)

# # תרגיל 17
# products = {    "Laptop": {        "price": 4500,        "stock": 10    },    "Mouse": {        "price": 80,        "stock": 50    },    "Keyboard": {        "price": 150,        "stock": 20    }}
# for k,v in products.items():
#     print(v["price"])
#     print(k,v["stock"])
#     if k=="Laptop":
#         v["stock"]=90
#     if v["price"]>100:
#         print(k)
# products["ppp"]={"price": 4500,"stock": 10}
# print(products)


# תרגיל 18
# total=0
# maxi=0
# employees = [    ("David", "Development", 15000),    ("Moshe", "Marketing", 12000),    ("Dana", "Development", 18000),    ("Noa", "HR", 11000)]
# for i in employees:
#     print(i[0])
#     if i[1]=="Development":
#         print(i[0])
#     if i[2]>total:
#         total=i[2]
#     maxi+=i[2]
# print(maxi/len(employees))

# # תרגיל 19
# inventory = {    "Laptop": 10,    "Mouse": 50,    "Keyboard": 20}
# a=input("prodakt")
# b=int(input("stook"))
# if a not in inventory:
#         print("uuu")
# for k,v in inventory.items():   
#     if k==a:
#         if b>v:
#             print("Large quantity from stock") 
#         else:
#             v-=b
    
# תרגיל 20
# votes = {    "David": 0,    "Moshe": 0,    "Dana": 0}
# while True:
#     name=input("name")
#     if name=="stop":
#         print(max(votes))
#         break

#     if name not in votes:
#        votes[name]=1
#     else:
#         for i in votes:
#             if name ==i:
#                 votes[i]+=1
# print(votes)

# # תרגיל 21
# contacts={"A":"101",
#               "b":"102",
#               "c":"103"}
# while True:
    
#     print("""1. Add a contact.
# 2. Search for a contact.
# 3.  Update a phone number.
# 4.  Delete a contact.
# 5.  View all contacts.
# 6.  Exit.""")
#     choice=input("choice")
#     if choice=="1":
#         contact=input("contact")
#         number=input("number")
#         contacts[contact]=number
#         print(contacts)
#     if choice=="2":
#         contact=input("contact")
#         for i in contacts:
#             if i==contact:
#                 print(i,contacts[i])
#     if choice=="3":
#         contact=input("contact")
#         for i in contacts:
#             if i==contact:
#                   number=input("number")
#                   contacts[i]=number
#             print(contacts)
#     if choice=="4":
#         contact=input("contact")              
#         if contact in contacts:
#             print("uuu")
#             contacts.pop(contact)
                    
#     if choice=="5":
#          print(contacts)
#     if choice=="6":
#         break

# תרגול מסכם
products = [    {"name": "Laptop", "price": 4, "stock": 10},    {"name": "Mouse", "price": 80, "stock": 5},    {"name": "Keyboard", "price": 150, "stock": 20},    {"name": "Screen", "price": 900, "stock": 15}]
print("""===== Store Management =====

1. Show all products
2. Add product
3. Search product
4. Update product price
5. Update product stock
6. Sell product
7. Show products by price
8. Show products with low stock
9. Show total inventory value
0. Exit""")
choice=input("choice")
for i in products:
    if choice=="1":
        print(i["name"],i["price"],i["stock"])
    if choice=="2":
        name=input("name")
        price=int(input("price"))
        stock=int(input("stock"))
        n={"name":name, "price":price, "stock":stock}
        products.append(n)
        print(products)
    if choice=="3":
        name=input("name")
        if i["name"]==name:
            print(i)
    if choice=="4":
        
        name=input("name")
        if i["name"]==name:
            price=int(input("price"))
            print("oooo")
            i["price"]=price
            
            print(products)
    if choice=="5":
        name=input("name")
        if i["name"]==name:
            stock=int(input("stock"))
            print("oooo")
            i["stock"]=stock
            
            print(products)
    if choice=="6":
        name=input("name")
        if i["name"]==name:
            stock=int(input("stock"))
            print("oooo")
            if i["stock"]>stock:
                i["stock"]-=stock

            
            print(products)
    if choice=="7":
          price=int(input("price"))
          for i in products:
          
            print(price)
            
            if i["price"]>price:
                print(i["name"])
    if choice=="8":
        
        
        for i in products:
        
            if i["stock"]<10:
               
                print(i["name"])

            
        






