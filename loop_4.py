#name=input("Enter your name :")
#while name ==" ":
 #   print("You didnot write the name")
  #  name=input("Enter your name :")
   # print(f"Hello{name}")
"""
age=int(input("enter your age :"))
while age>18:
    print(f"You can vote as your age is {age} ")
else:
    print("you cannot vote ")"""
"""
food=input("Enter the food you want")
while not food =="q":
    print(f"You like {food}")
    food=input("enter another food you like (q to quit): ")
    print("bye")"""
"""

num=int(input("Enter a number between 1-10"))
while num<1 or num>10:
    print(f"{num} is not valid")
    num=int(input("Enter a number between 1-10"))
    print(f"Your number is {num}")"""
"""
for x in range(1,5):
    print(x)

for x in reversed(range(1,5)):
    print(x)

for x in reversed(range(1,5,2)):
 print(x)"""
"""
credit_card ="12345-678-9103"
for x in credit_card:
   print(x)
 """
for x in range (1,21):
    if x==13:
        continue
    else:
        print(x)