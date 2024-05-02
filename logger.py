from data_create import name_data, surname_data, phone_data, address_data


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате записать данные\n\n"
    f"1 Вариант: \n"
    f"{name}\n{surname}\n{phone}\n{address}\n\n"
    f"2 Вариант: \n "
    f"{name};{surname};{phone};{address} \n"
    f"Выберите вариант: "))
    
    while var != 1 and var != 2:
        print("Неправильный ввод")
        var = int(input('Введите число: ')) 
        
    if var == 1:
        with open('data1variant.csv', 'a', encoding='utf-8')  as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address} \n\n")     
    
    elif var == 2:
        with open('data2variant.csv', 'a', encoding='utf-8')  as f:
            f.write(f"{name};{surname};{phone};{address} \n\n")  
            
            
def print_data():
    print('Вывожу данные из 1 файла: \n')
    with open('data1variant.csv', 'r', encoding='utf-8')  as f:
        data1 = f.readlines()# для начала читаем все наши строки
        data1_list = []#создадим переменную которая будет хранить итоговый результат
        j = 0
        for i in range(len (data1)):
            if data1[i] == '\n' or i == len (data1) - 1:#мы проверяем есть ли у нас какая то запись, она есть
                data1_list.append(''.join(data1[j:i+1]))#мы в наш файл добаляем нашу первую запись, потом i = 1, а значит  j=i=1
                j = i
        print(''.join(data1_list))        
    print('Вывожу данные из 2 файла: \n')
    with open('data2variant.csv', 'r', encoding='utf-8')  as f:            
        data2 = f.readlines()# для начала читаем все наши строки
        print(''.join(data2)) 
        
#print_data()          