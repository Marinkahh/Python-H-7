print( "Это телефонная книга") 
 
# creating a .txt file to store contact details 
filename = "myphonebook.txt" 
myfile = open(filename, "a+") 
myfile.close 
 
# defining main menu 
def main_menu(): 
    print( "\nГлавное меню\n") 
    print( "1. Показать все существующие контакты") 
    print( "2. Добавить новый контакт") 
    print( "3. Выполните поиск по существующему контакту") 
    print( "4. Выход") 
    choice = input("Введите пункт меню: ") 
    if choice == "1": 
        myfile = open(filename, "r+") 
        filecontents = myfile.read() 
        if len(filecontents) == 0: 
            print( "В телефонной книге нет контакта.") 
        else: 
            print(filecontents) 
        myfile.close 
        enter = input("Нажмите Enter, чтобы продолжить ...") 
        main_menu() 
    elif choice == "2": 
        newcontact() 
        enter = input("Нажмите Enter, чтобы продолжить ...") 
        main_menu() 
    elif choice == "3": 
        searchcontact() 
        enter = input("Нажмите Enter, чтобы продолжить ...") 
        main_menu() 
    elif choice == "4": 
        print("Рада была помочь!") 
    else: 
        print( "Что-то пошло не так, введите верные данные!\n") 
        enter = input( "Нажмите Enter, чтобы продолжить ...") 
        main_menu() 
 
# defining search function         
def searchcontact(): 
    searchname = input( "Введите имя для поиска контактной записи: ") 
    remname = searchname[1:] 
    firstchar = searchname[0] 
    searchname = firstchar.upper() + remname 
    myfile = open(filename, "r+") 
    filecontents = myfile.readlines() 
      
    found = False 
    for line in filecontents: 
        if searchname in line: 
            print( "Кажется вы искали:", end = " ") 
            print( line) 
            found = True 
            break 
    if found == False: 
        print( "Такого контакта я не нашла", searchname) 
 
# first name 
def input_firstname(): 
    first = input( "Введите имя ") 
    remfname = first[1:] 
    firstchar = first[0] 
    return firstchar.upper() + remfname 
 
# last name 
def input_lastname(): 
    last = input( "Введите фамилию: ") 
    remlname = last[1:] 
    firstchar = last[0] 
    return firstchar.upper() + remlname 
 
# storing the new contact details 
def newcontact(): 
    firstname = input_firstname() 
    lastname = input_lastname() 
    phoneNum = input( "Введите номер телефона: ") 
    emailID = input( "Введите адрес электронной почты: ") 
    contactDetails =("[" + firstname + " " + lastname + ", " + phoneNum + ", " + emailID +  "]\n") 
    myfile = open(filename, "a") 
    myfile.write(contactDetails) 
    print( "Контактные данные:\n " + contactDetails + "\nбыли успешно соххранены!") 
 
main_menu() 