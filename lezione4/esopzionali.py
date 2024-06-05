import random
#1. School Grading System:
#Create a function that takes a student's name and their scores in different subjects as input.
#The function calculates the average score and prints the student's name, average,
#and a message indicating whether the student passed the exam (average >= 60) or failed.
#Create a for loop to iterate over a list of students and scores, calling the function for each student.
"""
students=["gaia","lorenzo","oussama", "marco"]
voti_gaia=[30,60,100,80,75]
voti_lorenzo=[20,55,86,98]
voti_oussama=[73,62,54,81]
voti_marco=[10,15,84,53]
def students_score(name: str,marks: list): #-> str 
    average= sum(marks)/len(marks)
    if average >= 60:
        print(f"the student passed the exam with an average of {average}, congratulations {name}!! ")
    else:
        print(f"you failed the exam. your average is of {average}, try again next year, {name}.")       
    
for i in students:
    if i=="gaia":
        students_score(i,voti_gaia)
    elif i=="lorenzo":
        students_score(i,voti_lorenzo)
    elif i=="oussama":
        students_score(i,voti_oussama)
    elif i=="marco":
        students_score(i,voti_marco)

#2. Guess the Number Game:
#Create a function that generates a random number within a range specified by the user.
#Prompt the user to guess the number within a specified maximum number of attempts.
#Provide feedback to the user after each guess, indicating whether their guess is too high, too low, or correct.
#Terminate the loop when the user guesses the number correctly or reaches the maximum number of attempts.
range__number=int(input("inserisci un range per il numero da indovinare: "))
def random_number(range_number):
    number=random.randint(0,range_number)
    guess_number=int(input("indovina il numero, hai al massimo 3 tentativi. "))
    i=1
    while i<=3:
        if guess_number==number:
            print("hai vinto")
            break
        elif guess_number < number:
            guess_number= int(input("hai sbagliato, prova un numero più grande"))
        elif guess_number > number:
            guess_number= int(input("hai sbagliato, prova con un numero più piccolo"))   
        i+=1
        
out=random_number(range__number)

#3. E-commerce Shopping Cart:
#Create a function that defines a product with a name, price, and quantity.
#Create a function that manages the shopping cart, allowing the user to add, remove, and view products in the cart.
#The function should calculate the cart total and apply any discounts or taxes.
#Implement a for loop to iterate over the items in the cart and print detailed information about each product and the total.

def shopping_cart(x):
    shirt_item= {"name": "shirt", "price": 19.99, "quantity": 1 }
    skirt_item={"name": "skirt", "price": 9.99, "quantity": 1}
    trousers_item={"name": "trousers", "price": 25, "quantity": 1}
    item= input("scegli un articolo tra 'shirt', 'skirt' e 'trousers'. ")
    add=input("inserisci la quantità")
    
    product=[]   #fatto una lista con i prodotti
    if item=="shirt":
        product.append(item)
        shirt_item["quantity"]= add
    elif item=="skirt":
        product.append(item)
        skirt_item["quantity"]= add
    elif item=="trousers":
        product.append(item)
        trousers_item["quantity"]= add
    
    prices=[]    #fatto una lista con i prezzi moltiplicati per le quantità
    if item=="shirt":
        prices.append(shirt_item["price"])
        if add!= 1:
            prices.append(shirt_item["price"*add])
    elif item=="skirt":
        prices.append(skirt_item["price"])
        if add!= 1:
            prices.append(skirt_item["price"*add])
    elif item=="trousers":
        prices.append(trousers_item["price"])
        if add!= 1:
            prices.append(trousers_item["price"*add])


#4. Text Analysis:
#Create a function that reads a text file and counts the number of occurrences of each word.
#The function should print a report showing the most frequent words and their number of occurrences.
#You can use a for loop to iterate over the words in the text and a dictionary to store the occurrences.
#Implement error handling to handle missing files or other input issues.


#6. Password Generator:
#Create a function that generates a random password with a specified length and desired character types (lowercase letters, uppercase letters, numbers, symbols).
#Allow the user to specify the password length and desired character types.
#Generate and return a random password that meets the user's criteria.
#lenght=int(input("inserisci un valore per la lunghezza della assword: "))
#character=str(input("iserisci un carattere tra lowercase, uppercase, numeri e simboli"))

#def random_password(lenght: int, character: str):



#blackjack
def blackjack(hand: list[int]):
    total_sum: int= sum(hand)
    num_aces: int= hand.count(1)

    while total_sum > 21 and num_aces !=0:
        total_sum -= 10
        num_aces -= 1
    return total_sum

#Uno sviluppatore web deve sapere come progettare le dimensioni di una pagina web. Pertanto, data l'area specifica di una pagina Web rettangolare, il tuo compito ora è progettare una pagina Web rettangolare, la cui lunghezza L e larghezza W soddisfino i seguenti requisiti:
#1. L'area della pagina web rettangolare che hai progettato deve essere uguale all'area di destinazione specificata.
#2. La larghezza W non deve essere maggiore della lunghezza L, il che significa L >= W.
#3. La differenza tra la lunghezza L e la larghezza W dovrebbe essere la minima possibile.
#Restituisce una lista [L, W] dove L e W sono la lunghezza e la larghezza della pagina web che hai progettato in sequenza.
#Esempio:
#construct_rectangle(4)
#L'area target è 4 e tutti i modi possibili per costruirla sono [1,4], [2,2], [4,1].
#Ma secondo il requisito 2, [1,4] è illegale; secondo il requisito 3, [4,1] non è ottimale rispetto a [2,2]. Quindi la lunghezza L è 2 e la larghezza W è 2.

def construct_rectangle(area: float) -> list[float]:
    result: list[int]= [0,0]
    for i in range (1,area+1):
        for j in range(1, area+1):
            if i >= j and i*j==area:
                result.append([i,j])
    
    diff_min: float= float("inf")
    index: int= 0
    for i in range(len(result)):
        curr_diff: float =result[i][0] - result[i][1]
        if curr_diff<= diff_min:
            diff_min=curr_diff
            index=i
    return result[index]

def construct_rectangle(area: float) -> list[float]:
    sqrt_area= int (area** 0,5)
    for width in range(sqrt_area, 0, -1):
        if area % width == 0:
            height = area // width
"""

#def visit_tree(d: dict[int, list[int]]):
    #left_child, right_child=

##ree={1:[2,3], 2:[4,5],2:[None,None], 4:[None,None],5:[None,None]}

def visiting_tree_iterative(tree: dict[int, list[int]], root: int):
    result={}
    stack: list[int] = [root]
    
    while stack: # while len(stack) != 0
        curr_node = stack.pop(0)
        if curr_node:
            left_child, right_child =tree[curr_node]
            if left_child:
                stack.append(left_child)
            if right_child:
                stack.append(right_child)
    return result

print(visiting_tree_iterative({1:[2,3],2:[4,5],4:[None,None],3:[None,None]},1))






