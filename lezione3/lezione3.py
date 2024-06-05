import copy
#4-1. Pizzas: Think of at least three kinds of your favorite pizza. 
#Store these pizza names in a list, and then use a for loop to print the name of each pizza.
#• Modify your for loop to print a sentence using the name of the pizza, instead of printing just the name of the pizza. 
#For each pizza, you should have one line of output containing a simple statement like I like pepperoni pizza.
#• Add a line at the end of your program, outside the for loop, that states how much you like pizza. 
#The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, 
#such as I really love pizza!

pizza : list = ["margherita","capricciosa", "marinara"]

for i in pizza:
    print(f"i like {i} pizza.")
print("i really love pizza!")

#4-2. Animals: Think of at least three different animals that have a common characteristic. 
#Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
#• Modify your program to print a statement about each animal, such as A dog would make a great pet.
#• Add a line at the end of your program, stating what these animals have in common. 
#You could print a sentence, such as Any of these animals would make a great pet!

animals: list = ["dog","cat","horse"]

for i in animals:
    print(f"{i} would make a great pet.")
print("Any of these animals would make a great pet!")

#4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.
for number in range (1,21):
    print(number)

#4-4. One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers. 
#(If the output is taking too long, stop it by pressing CTRL-C or by closing the output window.)
lista_1mln: list = list(range(1,1000001))
print(lista_1mln)

#4-5. Summing a Million: Make a list of the numbers from one to one million, and then use min() and max() 
#to make sure your list actually starts at one and ends at one million. 
#Also, use the sum() function to see how quickly Python can add a million numbers.

print(min(lista_1mln),max(lista_1mln))
print(sum(lista_1mln))

#4-6. Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. 
#Use a for loop to print each number.
odd_numbers: list = []
for x in range(1,21,2):
    odd_numbers.append(x)
print(odd_numbers)

#4-7. Threes: Make a list of the multiples of 3, from 3 to 30. Use a for loop to print the numbers in your list.

multipli_tre: list =[]
for x in range (3,31,3):
    multipli_tre.append(x)
print(multipli_tre)

#4-8. Cubes: A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python. 
#Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), 
#and use a for loop to print out the value of each cube.

cube: list = []
for x in range(1,10):
    y = x**3
    cube.append(y)
print(cube)

#4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.
cubes: list= [x**3 for x in range(1,11)]
print(cubes)

#4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
#• Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
#• Print the message Three items from the middle of the list are:. Then use a slice to print three items from the middle of the list.
#• Print the message The last three items in the list are:. Then use a slice to print the last three items in the list.

print("the first three items in the list are: ",odd_numbers[:3])
print("The last three items in the list are: ",odd_numbers[-3:])

middle = len(odd_numbers) // 2
print("Three items from the middle of the list are: ",odd_numbers[middle-1],odd_numbers[middle],odd_numbers[middle+1])

#4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1. Make a copy of the list of pizzas, and call it friend_pizzas. 
#Then, do the following:
#• Add a new pizza to the original list.
#• Add a different pizza to the list friend_pizzas.
#• Prove that you have two separate lists. Print the message My favorite pizzas are:, and then use a for loop to print the first list. 
#Print the message My friend’s favorite pizzas are:, and then use a for loop to print the second list.
#Make sure each new pizza is stored in the appropriate list.

#4-12. More Loops: All versions of foods.py in this section have avoided using for loops when printing, to save space. 
#Choose a version of foods.py, and write two for loops to print each list of foods.

friend_pizzas : list = copy.deepcopy(pizza)
pizza.append("pepperoni")
friend_pizzas.append("vegetariana")
print(f"my favorite pizzas are {pizza}")
print(f"my favorite pizzas are {friend_pizzas}")

[print(f"my favorite pizzas are {i}") for i in pizza]
[print(f"my favorite pizzas are {i}") for i in friend_pizzas]

#5-1. Conditional Tests: Write a series of conditional tests. Print a statement
#describing each test and your prediction for the results of each test. Your code
#should look something like this:
#car = 'subaru'
#print("Is car == 'subaru'? I predict True.")
#print(car == 'subaru')
#print("\nIs car == 'audi'? I predict False.")
#print(car == 'audi')
#• Look closely at your results, and make sure you understand why each line
#evaluates to True or False.
#• Create at least 10 tests. Have at least 5 tests evaluate to True and another
#5 tests evaluate to False.

cat : str = "Aaron"
dog : str = "golden retriever"
car : str = "Panda"
city : str = "Paris"
book : str = "Harry potter"
print("Is cat=='Aaron'? I predict True")
print(cat=="Aaron")
print("Is cat=='Panda'? I predict False")
print(cat=="Panda")
print("Is dog=='golden retriever'? i predict True")
print(dog=="golden retriever")
print("is dog=='Harry potter'? I predict False")
print(dog=='Harry potter')
print("is car=='Panda'? I predict True")
print(car=="Panda")
print("Is car=='Paris'?I predict False")
print(car=='Paris')
print("is city=='Paris'? I predict True")
print(city=="Paris")
print("Is city=='Aaron? I predict False")
print(city=="Aaron")
print("Is book=='Harry potter? I predict True")
print(book=="Harry potter")
print("Is book=='golden retriever'? I predict False")
print(book=="golden retriever")

#5-2. More Conditional Tests: You don’t have to limit the number of tests you 
#create to 10. If you want to try more comparisons, write more tests and add them
#to conditional_tests.py. Have at least one True and one False result for each of
#the following:
#• Tests for equality and inequality with strings
#• Tests using the lower() method
#• Numerical tests involving equality and inequality, greater than and less
#than, greater than or equal to, and less than or equal to
#• Tests using the and keyword and the or keyword
#• Test whether an item is in a list
#• Test whether an item is not in a list

str1 : str = "hello world"
str2 : str = "HELLO WORLD"
print("is str1==str2?I predict False")
print(str1==str2)
print("is str1==str2(lower)?I predict True")
print(str1==str2.lower())

num1 : int = 10
num2 : int = 8
print("is num1==num2?I predict False")
print(num1==num2)
print("is num1<num2? i predict False")
print(num1<num2)
print("is num1>num2? i predict True")
print(num1>num2)

a: bool=True
b: bool=False
print("a and b i predict is False")
print(a and b)
print("a or b i predict is True")
print(a or b)

lista : list = [3,6,9,12,15]
print("number 3 is in 'lista' i predict")
print(3 in lista)
print("number 5 isn't in 'lista' i predict")
print(5 in lista)

#5-3. Alien Colors #1: Imagine an alien was just shot down in a game.
#Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
#• Write an if statement to test whether the alien’s color is green. If it is, print a message that the player just earned 5 points.
#• Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)
alien_color : str = input("choose a color between 'green', 'yellow or 'red : ->")
if alien_color == "green":
    print("you earned 5 points ")


#5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.
#• If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
#• If the alien’s color isn’t green, print a statement that the player just earned 10 points.
#• Write one version of this program that runs the if block and another that runs the else block.
alien_color : str = input("choose a color between 'green', 'yellow or 'red : ->")
if alien_color == "green":
    print("you earned 5 points ")
else:
    print("you earned 10 points")

#5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.
#• If the alien is green, print a message that the player earned 5 points.
#• If the alien is yellow, print a message that the player earned 10 points.
#• If the alien is red, print a message that the player earned 15 points.
#• Write three versions of this program, making sure each message is printed for the appropriate color alien.

alien_color : str = input("choose a color between 'green', 'yellow or 'red : ->")
if alien_color == "green":
    print("you earned 5 points ")
elif alien_color == "yellow":
    print("you earned 10 points")
elif alien_color == "red":
    print("you earned 15 points")

#5-6. Stages of Life: Write an if-elif-else chain that determines a person’s stage of life. Set a value for the variable age, and then:
#• If the person is less than 2 years old, print a message that the person is a baby.
#• If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
#• If the person is at least 4 years old but less than 13, print a message that the person is a kid.
#• If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
#• If the person is at least 20 years old but less than 65, print a message that the person is an adult.
#• If the person is age 65 or older, print a message that the person is an elder.

age : str = int(input("inserisci età: -"))


age: int=23
if age < 2:
    print("the person is a baby")
elif 2 <= age < 4:
    print("the person is a toddler")
elif 4 <= age < 13:
    print("the person is a kid")
elif 13 <= age < 20:
    print("the person is a teenager")
elif 20 <= age < 65:
    print("the person is an adult")
else:
    print("the person is an elder")

#5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of independent 
#if statements that check for certain fruits in your list.
#• Make a list of your three favorite fruits and call it favorite_fruits.
#• Write five if statements. Each should check whether a certain kind of fruit is in your list. 
#If the fruit is in your list, the if block should print a statement, such as You really like Apples!

favorite_fruits: list = ['apple', 'watermelon', 'banana']

if 'apple' in favorite_fruits:
    print("You really like Apples!")
if 'banana' in favorite_fruits:
    print("You really like Bananas!")
if 'watermelon' in favorite_fruits:
    print("You really like Watermelons!")
if 'mango' in favorite_fruits:
    print("You really like Mangos!")
if 'strawberry' in favorite_fruits:
    print("You really like Strawberries!") 

#5-8. Hello Admin: Make a list of five or more usernames, including the name 'admin'. 
#Imagine you are writing code that will print a greeting to each user after they log in to a website. 
#Loop through the list, and print a greeting to each user.
#• If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
#• Otherwise, print a generic greeting, such as Hello Jaden, thank you for logging in again.
usernames : list = ["Admin","gaia","pinco","pallino"]
for name in usernames:
    if name == "Admin":
            print("Hello Admin, would you like to see a status report?")
    else:
            print(f"Hello {name}, thank you for logging in again") 
           
            
#5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is not empty.
#• If the list is empty, print the message We need to find some users!
#• Remove all of the usernames from your list, and make sure the correct message is printed.
usernames : list = ["Admin","gaia","pinco","pallino"]
names=copy.deepcopy (usernames)
for name in names:
      usernames.remove(name)
print(usernames)
if len(usernames) == 0:
        print("We need to find some users!")

#5-10. Checking Usernames: Do the following to create a program that simulates how websites ensure that everyone has a unique username.
#• Make a list of five or more usernames called current_users.
#• Make another list of five usernames called new_users. Make sure one or two of the new usernames are also in the current_users list.
#• Loop through the new_users list to see if each new username has already been used. 
#If it has, print a message that the person will need to enter a new username. If a username has not been used, 
#print a message saying that the username is available.
#• Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted. 
#(To do this, you’ll need to make a copy of current_users containing the lowercase versions of all existing users.)

current_users : list = ["Gaia","Pinco","Pallino","Leonardo"]
new_users : list = ["Roberta","Clara","PINCO","Gaia"]

current_users : list = [i.lower() for i in current_users]
new_users : list = [i.lower() for i in new_users]

for i in current_users:
    if i in new_users:
        print(f"choose another username, {i} already exist.")
    else:
        print(f"That's ok. {i} is available.")

#5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such as 1st or 2nd. 
#Most ordinal numbers end in th, except 1, 2, and 3.
#• Store the numbers 1 through 9 in a list.
#• Loop through the list.
#• Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number. 
#Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result should be on a separate line.

ordinal_numbers : list = [1,2,3,4,5,6,7,8,9]

for i in ordinal_numbers:
    if i == 1:
        print("1st")
    elif i == 2:
        print("2nd")
    elif i == 3:
        print("3rd")
    elif i == 4:
        print("4th")
    elif i == 5:
        print("5th")
    elif i == 6:
        print("6th")
    elif i == 7:
        print("7th")
    elif i == 8:
        print("8th")
    elif i == 9:
        print("9th")
        



