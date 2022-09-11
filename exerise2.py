def Set_OF_Factorials():
        while type:
            input_number = input("Введите число: ")
            try:
                input_number=int(input_number)
            except ValueError:
                print('Неверный ввод числа!')
                continue
            except TypeError :
                print('Неверный ввод числа!') 
                continue
          
            break        
        for i in range(input_number):
            if(i==0):
                fact=[1]
            else:    
               fact.append(fact[i-1]*(i+1))
        print ( f"Набор произведений ={fact}")
Set_OF_Factorials()            