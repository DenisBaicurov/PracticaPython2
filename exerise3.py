def Input_Values():
    while type:
            input_number = input("Введите положительное целое число,кроме 196: ")
            try:
                input_number=int(input_number)
            except ValueError:
                print('Неверный ввод числа!')
                continue
            except TypeError :
                print('Неверный ввод числа!') 
                continue
            if input_number<0:
                print("Введите положиельное число")
                continue
            elif input_number==196:
                print('Число не должно равняться 196')
                continue
            break        
           
    return int (input_number)

def Flipping_Number(num):
    str_num=str(num)
    list_num=list(str_num)
    get_list_num=[]
    print(list_num)
    i=len(list_num)-1
    while i>-1:
       # print(i)
        get_list_num.append(list_num[i]) 
        i-=1 
     
  #  print(get_list_num)
    get_list_num1=0
    for i in range(0,len(get_list_num)):
        if(i==0):
            get_list_num1=int(get_list_num[i])
         #   print(get_list_num1)
        else:   
            get_list_num1=(get_list_num1)*10+int(get_list_num[i])
           
    print(get_list_num1)   
    return get_list_num1

 

def Get_Palindrome(num):
    get_num=num
    num1=Flipping_Number(num)
    i=0
    while num!=num1:
        num+=num1
        num1=Flipping_Number(num) 
        i+=1
    print(f'Число {num} является палиндромом числа {get_num} - {i}й ступени') 
   

    return num

Get_Palindrome(Input_Values())    

# Оставил выводы строк для понимания, откуда они