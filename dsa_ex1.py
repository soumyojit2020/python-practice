word_list = ['cat', 'dog', 'rabbit']
letter_list = []
for a_word in word_list:
    for a_letter in a_word:
        letter_list.append(a_letter)
# print(letter_list)

'''
Modify the given code so that the final list only contains a single copy of each letter.
Ans: We can convert the list into a set so that it removes duplicate characters
'''

letter_set = set(letter_list)
print(letter_set)
