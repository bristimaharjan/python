capitals={"USA":"Washington D.C",
          "Nepal":"Kathmandu",
          "China":"Beijing"}
#print(dir(capitals))
#print(help(capitals))
#print(capitals.get("Nepal")) 
'''if capitals.get("Japan"):
    print("exist")
else:
    print("Doesn't exist")'''
'''capitals.update({"Germany":"Berlin"})
print(capitals)'''
'''capitals.update({"USA":"Detriot"})
print(capitals)'''
#capitals.pop("China")
#capitals.popitem()#remove the latest added
#capitals.clear()
#keys=capitals.keys()
#for key in capitals.keys():
 #print(key)
'''values=capitals.values()
for value in capitals.values():
    print(value)'''
items=capitals.items()
for key,value in capitals.items():
    print(f"{key}:{value}")

