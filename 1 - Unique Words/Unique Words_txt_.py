#Selecting the unique words from a txt document
import re
import pandas as pd

with open("test_text.txt", "r") as document:
    text = document.read().lower()

elements = r'[.,+-;:!?\" "\n"]'
result = re.split(elements, text)

#print(result)

words_dict = {}

for word in result:
    if word in words_dict.keys():
        words_dict[word] += 1
    else:
        words_dict[word] = 1

sorted_val = sorted(words_dict.items(), key= lambda x:x[1], reverse= True)
#print(sorted_val)

sorted_dict = dict(sorted_val)
#print(sorted_dict)

#print(f"All unique words are: {sorted_dict.keys()}.")
print(f"{len(sorted_dict.values())} in total")

single_words = []

for keys in sorted_dict:
    if sorted_dict[keys] == 1:
        single_words.append(keys)


#print(f"All words with single appearance are: {single_words}.")
print(f"{len(single_words)} in total")

del sorted_dict['']
df = pd.DataFrame.from_dict(data= sorted_dict, orient= 'index')
print(df.head(20))