import sys
import string
import random
import password
import password16
import password32

def main():
    print("##############################")
    print("  STRONG PASSWORD GENERATOR")
    print("  Dev By Rakibul Hasan Asif")
    print("##############################")
    print("Available options for you:")
    print("1. 8  digit password generator")
    print("2. 16  digit password generator")
    print("3. 32  digit password generator")
    print("4. exit")
    try:
        choice = int(input("Enter your choice(ex:1,2,3 or 4): "))
        print("---------------------")
        if choice == 1:
            password.pass_8()
        elif choice == 2:
            password16.pass_16()
        elif choice == 3:
            password32.pass_32()
        elif choice == 4:
            print("Thanks for using me. Have a good day!")
            sys.exit()
        else:
            print("Invalid choice!")
            sys.exit()
    except KeyboardInterrupt:
        print("")
        print("Sorry! Keyboard Interrupted!")
        sys.exit()
    except ValueError:
        print("Invalid choice!")
        sys.exit()
    except IndexError:
        print("At least you have to say yes to any of these!")
main()
while True:
    print("")
    try:
        run = input("Do you want to run it again?(ex:y or n): ")
        if run.lower() == 'y':
            main()
        elif run.lower() == 'n':
            print("")
            print("Thanks for using me. Have a good day!")
            sys.exit()
    except KeyboardInterrupt:
        print("")
        print("Sorry! Keyboard Interrupted!")
        sys.exit()
    except ValueError:
        print("Invalid choice!")
        sys.exit()
