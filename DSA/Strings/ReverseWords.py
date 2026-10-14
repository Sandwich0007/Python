'''Reverse Words in a String'''

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        words.reverse()
        result = ' '.join(words)
        return result

'''Without Python Functions'''

# class Solution:
#     def reverseWords(self, s: str) -> str:
#         word =""
#         words = []
#         for ch in s:
#             if ch !=' ':
#                 word +=ch
#             else:
#                 if word != "":
#                     words.append(word)
#                     word = ""
#         if word!="":
#             words.append(word)

#         result = ""
#         for i in range(len(words)-1,-1,-1):
#             result +=words[i]
#             if i !=0:
#                 result +=" "
        
#         return result