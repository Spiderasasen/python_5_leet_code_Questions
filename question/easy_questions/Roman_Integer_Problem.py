import Reading_text_files as read

class Roman_Integer:
    def __init__(self):
        pass

    def question(self) -> None:
        #showing the player the requirements for the code
        read.read_text_file('Text_Files_for_Questions/Roman_int.txt')

    def code(self) -> None:
        #reads the code i wrote
        read.read_text_file('Code_Text_files/Roman_int.txt')

    def solution(self) -> None:
        num1 = Solution().romanToInt('I')  # number 1
        num2 = Solution().romanToInt('III')  # number 3
        num3 = Solution().romanToInt(
            'IV')  # number 4, will continue looping, so we need to have a check that it did count 4
        print(f'Num1: {num1}, Num2: {num2}, Num3: {num3}')
        num4 = Solution().romanToInt('XXII')  # 22
        num5 = Solution().romanToInt('XLV')  # 45
        num6 = Solution().romanToInt('XCII')  # 92
        print(f'Num4: {num4}, Num5: {num5}, Num6: {num6}')
        num7 = Solution().romanToInt('MCMXCIV')  # 1994
        num8 = Solution().romanToInt('MMIV')  # 2004
        num9 = Solution().romanToInt('MDCCLXXVI')  # 1776
        print(f'Num7: {num7}, Num8: {num8}, Num9: {num9}')


class Solution(object):
    #TODO make this shit possible
    def romanToInt(self, s):
        #the value in int
        count = 0

        #booleans that will count if it was counted as a speical case
        was_4 = False
        was_9 = False
        was_40 = False
        was_90 = False
        was_400 = False
        was_900 = False

        #simple loop though the numbers
        for i in range(len(s)):
            match s[i]:
                case 'I': #if the value is 1
                    try:
                        if s[i + 1] == 'V': #if the next value is V then return 4
                            count += 4
                            was_4 = True
                        elif s[i + 1] == 'X': #if the next value is X then return 9
                            count += 9
                            was_9 = True
                        else: #no error, and not next to a V, then return 1
                            count += 1
                    except IndexError: #an error, then return 1
                        count += 1
                case 'V':
                    #checking if the last value was 4, if it was, then countine the loop
                    if was_4:
                        was_4 = False
                        continue
                    else: #otherwise, count 5 and put the boolean to false
                        count += 5
                        was_4 = False
                case 'X':
                    if was_9:
                        was_9 = False
                        continue
                    else:
                        try:
                            if s[i + 1] == 'L':
                                was_40 = True
                                count += 40
                            elif s[i + 1] == 'C':
                                was_90 = True
                                count += 90
                            else:
                                count += 10
                        except IndexError:
                            count += 10
                case 'L':
                    if was_40:
                        was_40 = False
                        continue
                    else:
                        count += 50
                case 'C':
                    if was_90:
                        was_90 = False
                        continue
                    else:
                        try:
                            if s[i + 1] == 'D':
                                was_400 = True
                                count += 400
                            elif s[i + 1] == 'M':
                                was_900 = True
                                count += 900
                            else:
                                count += 100
                        except IndexError:
                            count += 100
                case 'D':
                    if was_400:
                        was_400 = False
                        continue
                    else:
                        count += 500
                case 'M':
                    if was_900:
                        was_900 = False
                        continue
                    else:
                        count += 1000

        #returns the final count
        return count

# def solutions():
#     print("My Solutions that the code works\n")
#     num1 = Solution().romanToInt('I') #number 1
#     num2 = Solution().romanToInt('III') #number 3
#     num3 = Solution().romanToInt('IV') # number 4, will continue looping, so we need to have a check that it did count 4
#     print(f'Num1: {num1}, Num2: {num2}, Num3: {num3}')
#     num4 = Solution().romanToInt('XXII') #22
#     num5 = Solution().romanToInt('XLV') #45
#     num6 = Solution().romanToInt('XCII') #92
#     print(f'Num4: {num4}, Num5: {num5}, Num6: {num6}')
#     num7 = Solution().romanToInt('MCMXCIV') #1994
#     num8 = Solution().romanToInt('MMIV') #2004
#     num9 = Solution().romanToInt('MDCCLXXVI') #1776
#     print(f'Num7: {num7}, Num8: {num8}, Num9: {num9}')

