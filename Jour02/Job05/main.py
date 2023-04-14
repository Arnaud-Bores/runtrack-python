def calcule(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2 
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    elif operator == '%':
        return num1 % num2
    else:
        print("operateur non valide")

resultat = calcule("le resulta est"+ str(8),'+',str(18))
print(resultat)
    





    
    

        

