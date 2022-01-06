import sys
import random
import random
import string
global letter_list, number_list, special_lists
#def letter()
def pass_32():
    count = 0
    letter_list = []
    try:
        letters = input("1. Should your password contain letters?(ex:y or n):")
        while count <= 18:
            if letters.lower() == 'y':
                for letter in random.choice(string.ascii_letters):
                    letter_list.append(letter)
            elif letters.lower() == 'n':
                    break
            else:
                print("Invalid Input!")
                sys.exit()
            count +=1
        new_list_let = letter_list
        #print(new_list_let)
    except KeyboardInterrupt:
        print("")
        print("Sorry! Keyboard Interrupted.")
        sys.exit()

    #def number():
    count = 0
    number_list = []
    try:
        numbers = input("2. Should your password contain numbers?(ex:y or n):")
        while count <= 12:
            if numbers.lower() == 'y':
                number = random.randint(1,9)
                number_list.append(number)
            elif numbers.lower() == 'n':
                break
            else:
                print("Invalid input!")
                sys.exit()
            count +=1
        new_list_num = number_list
        #print(new_list_num)
    except KeyboardInterrupt:
        print("")
        print("Sorry! Keyboard Interrupted.")
        sys.exit()

    #special
    special_list = ['@', '!', '#', '$', '%', '^', '&', '*', '(', ')', '<', '>', '?']
    count = 0
    new_list = []
    special_lists = []
    try:
        chars = input("3. Should your password contain special characters?(ex:y or n):")
        while count <= 10:
            if chars.lower() == 'y':
                for i in random.choice(special_list):
                    special_lists.append(i)
            elif chars.lower() == 'n':
                break
            else:
                print("Invalid input!")
                sys.exit()
            count +=1
        new_list = special_lists
        #print(new_list)
    except KeyboardInterrupt:
        print("")
        print("Sorry! Keyboard Interrupted.")
        sys.exit()

    #def main():
    main_list = []
    list_1 = new_list_let
    list_2 = new_list_num
    list_3 = new_list
    main_list = list_1 + list_2 + list_3
    #print(main_list)
    random_list = []
    count = 0
    while count <= 31:
        random_pass = random.choice(main_list)
        random_list.append(random_pass)
        count += 1
    password = ''.join(str(e) for e in random_list)
    print("---------------------------------------")
    print(f"Your 32 digit password is: {password}")
    print("---------------------------------------")


