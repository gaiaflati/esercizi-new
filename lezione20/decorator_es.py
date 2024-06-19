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


def decorator(func):

    def wrapper(*args):
        import time

        start = time.time()

        func(*args)

        print(f"Time elapsed {time.time()} - {start}")

    return wrapper

def ciao():

    print(f"ciao!")

ciao= decorator(ciao)

ciao()



