#main function
import sys
import printing_problems as pr
from question.easy_questions.Roman_Integer_Problem import Roman_Integer as Roman
import question.easy_questions.Common_letters_in_Array as Common
import question.medium_question.Longest_Palindromic_Substring as Palindromic

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
                            print("Largest Common Prefix Problem\n")
                            Common.reading_question() #reads the question
                            input("Press enter to continue...\n")
                            Common.reading_code() #reads the code i wrote
                            input("Press enter to continue...\n")
                            Common.solutions()  #showing the code works
                            input("Press enter to continue...\n")
                        case _:
                            print("Invalid Choice")
                case 2:
                    print("What question do you want to see?\n1.Longest Palindrome in Substring\n2.Longest Substring without Reacting Characters")
                    choice = int(input("Enter your choice:\n"))
                    match choice:
                        case 1:
                            print("Longest Palindrome in Substring problem")
                            Palindromic.read_question() #reads the question
                            input("Press enter to continue...\n")
                            Palindromic.reading_code()#reading the code i have on the area
                            input("Press enter to continue...\n")
                            Palindromic.solutions() #the solutions from my code
                            input("Press enter to continue...\n")
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