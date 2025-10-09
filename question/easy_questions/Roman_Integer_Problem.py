import Reading_text_files as read

#showing the player the requirements for the code
def question():
    read.read_text_file('Text_Files_for_Questions/Roman_int.txt')

class Solution(object):
    #TODO make this shit possible
    def romanToInt(self, s):
        pass

def solutions():
    Solution().romanToInt('I') #number 1
    Solution().romanToInt('III') #number 3
    Solution().romanToInt('IV') # number 4