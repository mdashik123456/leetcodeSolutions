class Solution:
    def reverseWords(self, str):
        str_list = str.split()
        str_list.reverse()
        return ' '.join(str_list)
