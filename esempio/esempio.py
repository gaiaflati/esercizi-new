reader = (open("files/esempio.txt", encoding="utf-8"))


try:
    
    reader.readline()
    print("sono nella try")
    raise Exception("eccezione")

except Exception:

    print("sono nella except")

finally:
    print("sono nella finally")
    reader.close()