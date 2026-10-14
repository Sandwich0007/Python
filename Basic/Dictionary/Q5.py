'''
Q146. Ask a string from user. Display the dictionary where each key is a
character and value is the frequency of that character that comes in that
string.

Enter a string: hello world

# Output
{'h': 1, 'e' : 1, 'l': 3, 'o' : 2, ' ': 1, 'w': 1, 'r' : 1, 'd': 1}'''

string = input("Enter the string: ")
freq = {}

for ch in string:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print(freq)