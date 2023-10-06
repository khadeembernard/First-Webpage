# sum = 0
# numbers = range(1,11)
# for i in numbers:
#     sum += i
# print(sum)
# name= 100 < 4
# print(name)

#Python Common Data Types
'''import os --> os.system('cls') Clear the cmd

While loop repeat a process

For loop Sequencely repeat a process 


'''
food = ['tacos','mangos','stawberry milk','pasta']
print(len(food)) #lenght of list
print(sorted(food)) #sorted list
food.sort() #sort
food.reverse() #reverse
food = ['tacos','mangos','stawberry milk','pasta']
food.append("popcorn")# added to the end of the list
food.index('mangos') # returns index of the item in the list
del food[2] #delete the item from the list
print(food)

#Dictionaries - Key value pairs Like a dictionary and definition
favFoods = {'Matt':"oranges","Taylor":"ribs","Austin":"Elote","Derek":"Tres Leches Cake","Elaine":"Tuxedo Cake"}
print(favFoods) #the printed order does not match the entered order because they do not matter to this structure
print(len(favFoods)) #length of dictionary
print(favFoods['Elaine'])
print(favFoods.keys()) #all the keys of the dictionary
print(favFoods.values()) #all the values of the dictionary
#Two print he value and keys in order 
for name in favFoods.keys():
    print(name + " loves " + favFoods[name])
#You can also use the get method
print(favFoods.get("Derek"))
#Change a key
favFoods['Matt'] = ["UpsideDown Cake", "4-Cheese Tortellini","Salmon"]
#Add a new key pair
favFoods['Fredrick']='donuts'
print(favFoods)
#delete key pair
favFoods.pop('Fredrick')

