#main function
import sys


def main():
    while True:
        print("What question do you like to see?\n1.Easy\n2.Medium\n3.Hard")
        try:
            choice = int(input("Enter your choice:\n"))

            match choice:
                case 1:
                    print("Easy")
                case 2:
                    print("Medium")
                case 3:
                    print("Hard")
                case _:
                    print("Please enter a valid choice from 1 - 3")
        except ValueError: #user inputted the wrong number
            print("Please enter a number.")
            continue
        except Exception as e: #something broke
            print(f'Error: {e}')
            sys.exit(1)


#main statement
if __name__ == '__main__':
    main()