#try to define a function named substract ouselves:
#it should take 2 parametres
#inside the function, it should substract the two
#then return the rsult
#After you defined it, call the function with some argument

def substract(x,y):
    return x-y
print(substract(4,7))

#è la stessa cosa di:
#out= substract(x,y)


#Write a function check_value(), which takes a number as an argument.
#Using if / else, the function should print whether the number is bigger, smaller, or equal to 5.

def check_value(x:int):
    if x>5:
        print("il numero è Maggiore a 5")
    elif x<5:   
        print("il numero è minore a 5")
    
    else:
        print("il numero è uguale a 5")

check_value(int(input("inserisci un numero")))

#Exercise 2
#Write a function check_length(), which takes a string as an argument.
#Using if / else, check if the length of the string is bigger, smaller, or equal to 10 characters

def check_length(x: str): 
    if len(x)>10:
        return ("la stringa è > di 10 caratteri")
    elif len(x)<10:
        return ("la stringa è < di 10 caratteri")
    else:
        return ("la stringa è = a 10 caratteri")
print(check_length(input("inserisci una stringa")))

#Exercise 3
#Write a function print_numbers(), which takes a list of numbers as argument.
#Using a for loop, print each number one by on

def print_numbers(list:list):
    for i in list:
        print(i)
print_numbers([2,5,7,3,8,10,4])

#Write a function check_each(), which takes a list of numbers as argument.
#Using a for loop, iterate through the list.
#For each number, print “bigger” if it’s bigger than 5, “smaller” if it’s smaller than 5,
#and “equal” if it’s equal to 5.

def check_each(numb: list):
    for i in numb:
        if i>5:
            print("bigger")
        elif i<5:
            print("smaller")
        else:
            print("equal")
out=check_each([3,8,6,5,9,1])

#Write a function add_one(). It takes an integer as argument. The function adds 1 to
#the integer and returns it.
#Write another function add_one_to_list(). It takes a list of integers as argument.
#Define a variable new_list in this function.
#Using a for loop, iterate through the argument list.
#Using add_one(), fill new_list with integers from the argument list incremented by 1.
#Print new_list.
#Example:
#add_one_to_list([1, 2, 3])
#>>> [2, 3, 4]

#prima funzione
def add_one(a: int):
    a +=1
    return a
print(add_one(3))

#seconda funzione con argomento lista di interi
def add_one_to_list (integers_list):
    new_list=[]
    for n in integers_list:
        new_list.append(add_one(n))
    print (new_list)
add_one_to_list([4,6,1,9])


#8-1. Message: Write a function called display_message() 
#that prints one sentence telling everyone what you are learning about in this chapter. 
#Call the function, and make sure the message displays correctly.

def display_message(x: str):
    return(x)
print(display_message("sto imparando a usare python"))

#8-2. Favorite Book: Write a function called favorite_book() that accepts one parameter, title. 
#The function should print a message, such as "One of my favorite books is Alice in Wonderland". 
#Call the function, making sure to include a book title as an argument in the function call.

def favorite_book(title: str): #->str
    return f"One of my favorite book is {title}"
print(favorite_book("Harry potter"))

#8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. 
#The function should print a sentence summarizing the size of the shirt and the message printed on it.
#Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.
def make_shirt(size: int, message: str, taglia: str="M", text: str="my shirt"): #-> str
    print(f"the size of the shirt is {size}, and the message that should be printed on it is: {message}.")
    print(f"the size oh the shirt is {taglia}, and the message that shoul be printed on it is: {text}.")
out=make_shirt(42, "la mia tshirt")

#8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. 
#Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.
def make_shirt(size: str, message: str, taglia: str="L", text: str="I love Python"): #-> str
    print (f"the size of the shirt is {taglia}, and the message that should be printed on it is: {text}.")
    print (f"the size of the shirt is {size}, and the message that should be printed on it is: {text}.")
    print (f"the size of the shirt is {size}, and the message that should be printed on it is: {message}.")
out=make_shirt("M", "Python is Beautiful")

#8-5. Cities: Write a function called describe_city() that accepts the name of a city and its country. 
#The function should print a simple sentence, such as Reykjavik is in Iceland. Give the parameter for the country a default value. 
#Call your function for three different cities, at least one of which is not in the default country.
def describe_city(city: str, country: str="Italy"): #->str
    print(f"{city} is in {country}.")
out=describe_city("Milan")
out=describe_city("Florence")
out=describe_city("New York")

#8-6. City Names: Write a function called city_country() that takes in the name of a city and its country. 
#The function should return a string formatted like this: "Santiago, Chile". 
#Call your function with at least three city-country pairs, and print the values that are returned.

def city_country(city: str, country: str): #->str
    print(f"{city}, {country}.")
city_country("Krakow","Poland")
city_country("Malaga","Spain")
city_country("Lisboa","Portugal")

#8-7. Album: Write a function called make_album() that builds a dictionary describing a music album. 
#The function should take in an artist name and an album title, 
#and it should return a dictionary containing these two pieces of information. 
#Use the function to make three dictionaries representing different albums. 
#Print each return value to show that the  dictionaries are storing the album information correctly. 
#Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. 
#If the calling line includes a value for the number of songs, add that value to the album’s dictionary.
#Make at least one new function call that includes the number of songs on an album.

def make_album(artist: str, title: str, songs): #->dict
    if songs==None:
        album: dict={artist:title}
    else:
         album: dict={artist: {title: {"number of songs":songs}}}
    print(album)
make_album("Gazzelle","Idem",None)
make_album("Queen", "Innuendo", None)
make_album("Rihanna", "Loud", None)
make_album("Blink182","California", 16)

#8-8. User Albums: Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album’s artist and title.
#Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. 
#Be sure to include a quit value in the while loop.
def make_album2(artist: str, title: str, songs): #->dict
    if songs==None:
        album: dict={artist:title}
    else:
        album: dict={artist: {title: {"number of songs":songs}}}
        print(album)
while True:
    artist=str(input("inserisci artista o 'esci' per uscire: "))
    if artist=="esci":
        break
    title=str(input("inserisci titolo o 'esci' per uscire: "))
    if title=="esci":
        break  
    print(make_album(artist,title,8))

#8-9. Messages: Make a list containing a series of short text messages. 
#Pass the list to a function called show_messages(), which prints each text message.

messages: list=["hello world", "my pen is balck","think outside the box"]
def show_messages(messages_list: list):
    for i in messages_list:
        print(i)
    return messages   
out=show_messages(messages)

#8-10. Sending Messages: Start with a copy of your program from Exercise 8-9. 
#Write a function called send_messages() that prints each text message and moves each message 
#to a new list called sent_messages as it’s printed. After calling the function,
#print both of your lists to make sure the messages were moved correctly.


def send_messages(text_messages):
    sent_messages=[]
    for i in text_messages:
        sent_messages.append(i)
    print(text_messages)
    print(sent_messages)
out=send_messages(messages)

#8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. 
#The function should have one parameter that collects as many items as the function call provides, 
#and it should print a summary of the sandwich that’s being ordered. 
#Call the function three times, using a different number of arguments each time.
def sandwiches(ingredients: list):
    print (f"nel sandwich deve esserci: {ingredients}")
out=sandwiches(["cipolla", "pomodoro","cheddar"])
out=sandwiches(["cetriolini", "senape", "bacon"])
out=sandwiches(["insalata", "ketchup", "maionese"])

#8-13. User Profile:  Build a profile of yourself by calling build_profile(), 
#using your first and last names and three other key-value pairs that describe you. 
#All the values must be passed to the function as parameters. 
#The function then must return a string such as "Eric Crow, age 45, hair brown, weight 67"
profile={"Gaia": "Flati", "hair":"brown","eyes": "brown","age": 23,"city": "ladispoli"}
def build_profile(values: dict): #->str
    for key in values:
        print(f"{key},{values.get(key)}")
         
out=build_profile(profile)

def build_profile(first_name, last_name, age, hair, city):
    profile=f"{first_name} {last_name}, age {age}, hair {hair}, city {city}"
    return profile
me=build_profile("Gaia","Flati",23,"Brown","Ladispoli")

#8-14. Cars: Write a function that stores information about a car in a dictionary. 
#The function should always receive a manufacturer and a model name. 
#It should then accept an arbitrary number of keyword arguments. 
#Call the function with the required information and two other name-value pairs, such as a color or an optional feature. 
#Your function should work for a call like this one: car = make_car('subaru', 'outback', color='blue', tow_package=True) 
#Print the dictionary that’s returned to make sure all the information was stored correctly. 

def make_car(manufacturer, model, color=None, fuel=None): #->dict
    return{"manufacturer": manufacturer,"model":model,"color": color,"fuel":fuel}
car=print(make_car('Fiat','Panda',"blue","Diesel"))


#8-15. Printing Models: Put the functions for the example printing_models.py in a separate file called printing_functions.py.
# Write an import statement at the top of printing_models.py, and modify the file to use the imported functions.






    







    





    

        





