import time


def funzione_decoratore(funzione_parametro):
    def wrapper():
        """ nome convenzionale - wrapper significa 'incarto, confezione' """
        print("... codice da eseguire prima di 'funzione_parametro' ...")
        funzione_parametro()
        print("... codice da eseguire dopo di 'funzione_parametro' ...")
    return wrapper







def mia_funzione():
    print("Hello World!")


mia_funzione = funzione_decoratore(mia_funzione)
mia_funzione()







def ciao(name: str):

    return f"Ciao {name}"

def saluta_bob(func):
   
    return func("Bob")

print(saluta_bob(ciao))


def parent():
    print("sono in parent")

    def child():
        print("sono in child")

    return child

   
print(parent())





def decorator(func):

    def wrapper():
        print(f"prima di func")

        func()

        print(f"dopo func")

    return wrapper

def ciao():

    print(f"ciao!")

ciao= decorator(ciao)

ciao()






class Timer:
    
    def __enter__(self):
        
        self.time = time.time()
        
    def __exit__(self, exc_type, exc_value, traceback):
        
        print(f"Time Elapsed: {time.time() - self.time}")
        
        return False


def decorator(func):

    def wrapper(*args):
        import time

        start = time.time()

        func(*args)

        print(f"Time elapsed {time.time() - start}")

    return wrapper

def ciao():

    print(f"ciao!")

ciao= decorator(ciao)

ciao()

@decorator
def area_cerchio(raggio: float):
    
    return 3.14*(raggio**2)







def generatore():

    yield "A"
    yield "B"
    yield "C"

prova_generatore = generatore()

print(next(prova_generatore))

                                

                
                

                
                

import time
    

def funzione(id: int):
    import time
    import random
    
    sleep_time: int = random.randint(1, 10)
    print(f"{id=} time {time.time()}")
    time.sleep(sleep_time)
    print(f"{id=} time {time.time()}")
    
if __name__ == "__main__":
    
    import threading
    from concurrent.futures import ThreadPoolExecutor
    
    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(funzione, range(100))
   
                

                
                

                
                


