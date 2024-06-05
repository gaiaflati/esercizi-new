import random


def posizione():
    pass

def mossa_tarta():
    pass
  
    


def mossa_lepre():
    pass



#Riposo (20% di probabilità): non si muove.
#Grande balzo (20% di probabilità): avanza di 9 quadrati.
#Grande scivolata (10% di probabilità): arretra di 12 quadrati. Non può andare sotto il quadrato 1.
#Piccolo balzo (30% di probabilità): avanza di 1 quadrato.
#Piccola scivolata (20% di probabilità): arretra di 2 quadrati. Non può andare sotto il quadrato 1.


#Passo_veloce=(50% di probabilità): avanza di 3 quadrati.
#Scivolata =(20% di probabilità): arretra di 6 quadrati. Non può andare sotto il quadrato 1.
#Passo_lento =(30% di probabilità): avanza di 1 quadrato.


posizione=["_"]*70
post=1
posl=1
while post < 69 and posl < 69:
    i=random.randint(1,10)
    #posizione tarta
    if 1<=i<=5:
        post+=3
        
    elif 6 <= i <= 7:
        post-=6
        if post<1:
            post=1
        
    elif 8 <= i <= 10:
        post+=1
        
    i=random.randint(1,10)
    #posizione lepre
    if 1<= i <=2:
        posl=posl
    elif 3<= i <= 4:
        posl+=9
        
    elif i==5:
        posl-=12
        if posl < 1:
            posl=1
        
    elif 6 <= i <= 8:
        posl+=1
        
    elif 9<= i <= 10:
        posl-=2
        if posl<1:
            posl=1

    if posl>=69 and post>=69: #se sono entrambi arrivati alla vittoria
        print("".join(posizione))
        print("IT'S A TIE.")
        break
    
    elif post>=69:  #se ha vinto la tarta
        post=69
        posizione[post]="T"
        posizione[posl]="H"
        print("".join(posizione))
        print("TORTOISE WINS! || VAY!!!")
        break

    elif posl>=69:  #se ha vinto la lepre
        posl=69
        posizione[post]="T"
        posizione[posl]="H"
        print("".join(posizione))
        print("HARE WINS || YUCH!!!")
        break

       
    if post==posl:    #se si trovano nella stessa posizione
        posizione[post]="OUCH!!!"
    else:
        posizione[post]="T"
        posizione[posl]="H"

    print("".join(posizione))
    posizione[posl]="_"
    posizione[post]="_"
    
    



    
