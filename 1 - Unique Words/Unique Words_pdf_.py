from pypdf import PdfReader
import re

doc_path = "../../../../Downloads/receitas_carnes_aves.pdf"

reader = PdfReader(doc_path)
text= ""

for pages in reader.pages:
    text += pages.extract_text().lower() + "\n"

#print(text)

params = r'[.,_()\"!+" " "\n""\t"]'

words_split = re.split(params, text)
#print(words_split)

words_dict = {}

for word in words_split:
    if word in words_dict.keys():
        words_dict[word] += 1
    else:
        words_dict[word] = 1

sorted_words = sorted_val = sorted(words_dict.items(), key= lambda x:x[1], reverse= True)

sorted_dict = dict(sorted_words)
del sorted_dict[""]
print(sorted_dict["alho"])