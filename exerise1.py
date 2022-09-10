
def Input_Values():
    while type:
            input_number = input("Введите число: ")
            try:
                input_number=float(input_number)
            except ValueError:
                print('Неверный ввод числа!')
                continue
            except TypeError :
                print('Неверный ввод числа!') 
                continue
          
            break        
           
    return float (input_number)


def Sum_number(num):
  #  print (type(num))
    get_num=num
    get_num=abs(float(get_num))
    num_str=str(get_num)
    num_list=list(num_str)
    sum=0
    for i in range(0,len(num_str)):
        if (num_list[i]!='.'):
             sum+=int(num_list[i])  
    return print (f'Сумма цифр числа {num} равняется {sum}') 
    
Sum_number(Input_Values())          

        
