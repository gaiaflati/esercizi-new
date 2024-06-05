
class Animal: 
    
    def __init__(self, specie: str, age: int) -> None:
        
        self.specie=specie
        self.age=age
    
    def __str__(self) -> str:
        f" {self.__class__.__name__}(name={self.name}, età={self.age}, specie={self.specie})"

    
    
class Person(Animal): 
    
    def __init__(self, age: int, cf: str, name: str, surname: str, specie: str,) -> None:
        super().__init__(specie, age)

        self.cf=cf
        self.name= name
        self.surname= surname

    def speak(self) -> str:
        return f" Ciao mi chiamo {self.name} {self.surname} e ho {self.age} anni."

    def __str__(self) -> str:
        s: str= super().__str__()[:-1]
        s += f", surname={self.surname}, cf={self.cf}"
        return s
        


class Cat(Animal):
        
    def __init__(self, age: int, name: str, specie="Felidae") -> None:
        super().__init__(specie, age,)
        self.name=name

    def __str__(self) -> str:
        return f"Cat--> (nome={self.name}, age={self.age}, specie={self.specie} )"
    
class Rabbit(Animal):
    
    def __init__(self, age: int, name: str) -> None:
        super().__init__("Leporidae", age)
        self.name=name





p= Person(name="Gaia", surname="Flati", cf="FLTGAI01C53H5010", age=23)
a=Animal(specie="balena", age=26)



def symmetric(tree: list[int]) -> bool:
    destra=[]
    i=0
    for i in range(len(tree)):
        destra.append[tree[2*i+1]]
        i+=1
    sinistra=[]
    i=0
    while i<= len(tree):
        sinistra.append[tree[2*(i+1)]]
        i+=1
    if destra==sinistra:
        return True
    else:
        return False
    
print(symmetric([1,2,2,3,4,4,3]))
 

def symmetric(tree: list[int]) -> bool:
    i=0
    destra=[]
    for i in range(len(tree)):
        if tree[2*i+1] == tree [2*(i+1)]:
            i=5
            return True
        else:
            return False
        
def calcola_stipendio(ore_lavorate: int) -> float:
    # cancella pass e scrivi il tuo codice
    if ore_lavorate<=40.00:
        stipendio=ore_lavorate*10.00
    else:
        stipendio=400.00+ (ore_lavorate-40.00)*15.00
    
    return ore_lavorate


def seconds_since_noon(ore: int, minuti: int, secondi: int) -> int:
   
        secondi_=ore*3600+minuti*60+secondi
        return secondi_
seconds_since_noon(1,0,0)
        
def time_difference(ore, minuti, secondi, ore_2, minuti_2, secondi_2):
    orario_1=seconds_since_noon(ore, minuti, secondi)
    orario_2=seconds_since_noon(ore_2, minuti_2, secondi_2)
    print (orario_1, orario_2)
    time= orario_2-orario_1
    return time
print(time_difference(1, 0, 0, 3, 15, 30))



class LinkedList:
   
    def __init__(self, Node: str) -> None:
        self.Node=Node

        
def is_palindrome(head: Node) -> list[int]:

def merge(nums1, m, nums2, n):
    for i in nums2:
        nums1.append[i]
    if len(nums1)!=m+n:
        nums1.remove(0)
    return nums1

merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
print(nums1)  

 #- push(x: int) -> None: Pushes element x to the top of the stack.
# pop() -> None Removes the element on the top of the stack and returns it.
# top() -> None Returns the element on the top of the stack.
# empty() -> None Returns true if the stack is empty, false otherwise.

class MyStack:
    def __init__(self, elements=[]):
        self.elements=elements
        
    def push(self, x: int) ->None:
        for i in self.elements:
            if i==x:
                self.elements.append(x)

    def pop(self):
        return self.elements.pop(-1)
        
    def top(self):
        return self.elements[-1]
    
    def empty(self):
        if len(self.elements)==0:
            return True
        else:
            False


def rimbalzo() -> None:
    
    t: int = 0
    altezza: float = 0.0
    velocita: float = 100.0
    rimbalzi: int = 0
    
    
    #dopo ogni secondo -># altezza = altezza + velocità
                        #velocità = velocità - 96.
    #Se il nuovo valore che si ottiene per l'altezza è inferiore a 0,
    #si deve moltiplicare altezza e velocità per -0.5 per 
    #simulare il rimbalzo. Dunque, per il rimbalzo, si avrà che
    #altezza= altezza*-0,5 
    #velocità=velocità*-0,5.
    



    altezza= altezza+velocita
    velocita= velocita - 96
    print(f"Tempo: {t} Altezza: {altezza}")
    if altezza<0:
        altezza*= -0.5
        velocita*= -0.5
        rimbalzo+=1
        print(f"Tempo: {t} Rimbalzo!")
        t+=1
    else:
        altezza= altezza+velocita
        velocita= velocita - 96
        print(f"Tempo: {t} Altezza: {altezza}")
        t+=1



        def rimbalzo() -> None:
    
    t: int = 0
    altezza: float = 0.0
    velocita: float = 100.0
    rimbalzi: int = 0
    #dopo ogni secondo -># altezza = altezza + velocità
                        #velocità = velocità - 96.
    #Se il nuovo valore che si ottiene per l'altezza è inferiore a 0,
    #si deve moltiplicare altezza e velocità per -0.5 per 
    #simulare il rimbalzo. Dunque, per il rimbalzo, si avrà che
    #altezza= altezza*-0,5 
    #velocità=velocità*-0,5.
    print(f"Tempo: {t} Altezza: {altezza}")
    rimbalzo=0
    while rimbalzo<=5:
        altezza= altezza+velocita
        velocita= velocita - 96
        


        if altezza<0:
            altezza*= -0.5
            velocita*= -0.5
            rimbalzo+=1
            t+=1
            print(f"Tempo: {t} Rimbalzo!")
        else:
            altezza= altezza+velocita
            velocita= velocita - 96
            print(f"Tempo: {t} Altezza: {altezza}")
            t+=1


            def rimbalzo() -> None:
    
    t: int = 0
    h: float = 0.0
    v: float = 100.0
    r: int = 0
    
    print(f"Tempo: {t} Altezza: {h}")
    while r<5:
        t+=1    
        h= h+v
        v= v - 96
        
        if h<0:
            print(f"Tempo: {t} Rimbalzo!")
            h=h* -0.5
            v= v*-0.5
            r+=1

            t+=1
            print(f"Tempo: {t} Altezza: {h}")
            
        else:
            print(f"Tempo: {t} Altezza: {h}")


"""
memorizza_file([1100, 20000, 1048576, 512, 5000])
File di 1100 byte compresso in 880.0 byte e memorizzato. Blocchi usati: 2. Blocchi rimanenti: 998.
File di 20000 byte compresso in 16000.0 byte e memorizzato. Blocchi usati: 31. Blocchi rimanenti: 967.
Non è possibile memorizzare il file di 1048576 byte. Spazio insufficiente.
"""