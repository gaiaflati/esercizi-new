"""
    Dato un inero col_number, resttuire i suo corrispondente
    titolo di colonna come ad esempio compare su un foglio Excel

    Esempio 1:
    col_number=1 -> restituisce "A"
    col_number=2 -> restituisce "B"
    col number=26 -> restituisce "Z"

    Esempio 2:
    col_number=27 -> restituisce AA

"""
def convert_to_title(col_number: int):
    result: str= ""
    while col_number > 0:
        resto= (col_number-1) % 26  #questo mi da il resto
        result= chr(resto+ ord("A"))+ result
        col_number = (col_number-1) // 26   
    return result


   


        

