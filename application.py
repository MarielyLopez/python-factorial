# Aqui escribe tu codigo

#print "Hello World"

def insert_number():
    number = raw_input("Insert a number: ")
    a = verific_number(number)
    if a == True:
        print "numero valido"
    else:
        print "no es nunero"
    return number

def verific_number(number):
    answer_u = True
    while answer_u == True:
        try:
            if True == number.isdigit():
                return True
            else:
                return False
        except ValueError:
            print "Try again"



"""Para el range en el insert_number imprimir cada elemento""" 
if __name__ == '__main__':
    insert_number()
