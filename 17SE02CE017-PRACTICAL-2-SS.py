#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Entry:
    def __init__(self ,label,symbol,value): #data_type ,#, hash_key,
        #self.hash_key = hash_key
        self.label = label
        self.symbol = symbol
        self.value =value

symbol_table = []

# check if the symbol table is empty or not
def is_empty():
    if len(symbol_table) > 0:
        return False

    return True

# num1, Integer  --> 44
# check the uesr_input is comma separated or not
def is_comma_separated(my_string):
    for chacter in my_string:
        if chacter == ',':
            return True
    return False


# to find the existing name in the symbol table
def is_match_found(label):
    index = -1
    if len(symbol_table) > 0:
        for index, element in enumerate(symbol_table):
            if label == element.label:
                return True, index
        return False, index

    return False, index

# Insert new Data in the symbol table
def insert(my_input):
    if is_comma_separated(my_input):
        my_input = my_input.split(',')
        label = my_input[0].strip()
        symbol = my_input[1].strip()
        value = my_input[2].strip()

        if len(symbol_table) > 100:
            print('')
            return "Symtem table reached it's max limit"

        match_found, index = is_match_found(label)
        if not match_found:
            symbol_table.append(Entry(label,symbol,value))
            return "Insert Successful"
        print('')

        return "Sorry! Name alredy exits. Enter an unique name."

    return "Sorry! You didn't enter comma separated value."


# Search provided name in the symbol table
def search(my_input):
    match_found, index = is_match_found(my_input)

    if match_found:
        return f'Match found. label is => {symbol_table[index].label} and symbol is => {symbol_table[index].symbol} and value is => {symbol_table[index].value}'

    return 'Sorry, No Match!! Name not Found'


# Delete from the symbol table
def delete(my_input):
    match_found, index = is_match_found(my_input)
    if match_found:
        del symbol_table[index]
        return 'Delete successful'

    return 'Name not found!! No data is Deleted'


# Display the symbol talbe
def show():
    for entry in symbol_table:
        print(f"lab is: {entry.label} --&&--> symbol is : {entry.symbol}  --&&-->  valueis : {entry.value}")


# Update an exsiting data in the symbol table
def update(my_input):
    match_found, index = is_match_found(my_input)

    if match_found:
        label =input('Enter new label: ')
        symbol = input('Enter new symbol: ')
        value = input('Enter new value: ')
            
        if symbol_table[index].label == label:
            return 'Sorry you enter same label. Nothing to change'
        if symbol_table[index].symbol == symbol:
            return 'Sorry you enter same data type. Nothing to change'
        
        symbol_table[index].label = label
        symbol_table[index].symbol = symbol
        symbol_table[index].value = value
        return 'Update successful'
    return 'label not found!!'

while True:
    print('Enter 1 for Insert')
    print('Enter 2 for Search')
    print('Enter 3 for Delete')
    print('Enter 4 for Show')
    print('Enter 5 for Update')
    print('Enter 6 for Exit')
    user_choice = input('Enter your choice from the list: ')

    if user_choice == '1':
        user_input = input('Please insert data with comma separeted BE LIKE [ LABLE , SYMBOL ,VALUE ]--> ')
        print(insert(user_input))
        print('')

    elif user_choice == '2':
        if is_empty():
            print('Symble table is empty! Insert data.')
        else:
            user_input = input('Please insert existing label--> ')
            print(search(user_input))
            print('')
        print('')

    elif user_choice == '3':
        if is_empty():
            print('Symble table is empty! Insert data.')
        else:
            user_input = input('Please insert existing label--> ')
            print(delete(user_input))
            print('')
        print('')

    elif user_choice == '4':
        if is_empty():
            print('Symble table is empty! Insert data.')
        else:
            show()
            print('')
        print('')

    elif user_choice == '5':
        if is_empty():
            print('Symble table is empty! Insert data.')
        else:
            user_input = input('Please insert existing label--> ')
            print(update(user_input))
            print('')
        print('')
    elif user_choice == '6':
        print('Thank you. You exit from the program')
        break
    else:
        print('You enter a wrong choice. Try again.')
        print('')


# In[ ]:




