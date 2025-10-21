#main function
import sys
import printing_problems as pr
from question.easy_questions.Roman_Integer_Problem import Roman_Integer as Roman
from question.easy_questions.Common_letters_in_Array import Common_letters as Common
from question.medium_question.Longest_Palindromic_Substring import Longest_Palindrome as Palindromic

def main():
    while True:
        print("What question do you like to see?\n1.Easy\n2.Medium\n3.Hard\n4.Exit")
        try:
            choice = int(input("Enter your choice:\n"))

            match choice:
                case 1:
                    print("What question do you want to see?\n1.Roman Integer\n2.Largest Common Prefix")
                    choice = int(input("Enter your choice:\n"))
                    match choice:
                        case 1:
                            roman = Roman()
                            pr.printing_display(roman)
                        case 2:
                            common = Common()
                            pr.printing_display(common)
                        case _:
                            print("Invalid Choice")
                case 2:
                    print("What question do you want to see?\n1.Longest Palindrome in Substring\n2.Longest Substring without Reacting Characters")
                    choice = int(input("Enter your choice:\n"))
                    match choice:
                        case 1:
                            long_palindrome = Palindromic()
                            pr.printing_display(long_palindrome)
                        case 2:
                            print("Longest Substring without Reacting Characters Problem")
                        case _:
                            print("Invalid Choice")
                case 3:
                    print("Hard")
                case 4:
                    sys.exit()
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