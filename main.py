file1 = open('./2021dataparse/data2022.txt', 'r')
Lines = file1.read()
Lines = Lines.replace(',', '\n')
Lines = Lines.replace('.', '')
Lines = Lines.replace('and', '')
Lines = Lines.replace(' ', '')
Lines = Lines.replace('_', ' ')
Lines = Lines.lower().split('\n')
print(len(Lines))
from wordgenerator import *  
generate_wordcloud(Lines, 'wordcloud2022.png', '2022.png')
del Lines
del file1

file1 = open('./2021dataparse/data2021.txt', 'r')
Lines = file1.read()
Lines = Lines.replace(',', '\n')
Lines = Lines.replace('.', '')
Lines = Lines.replace('and', '')
Lines = Lines.replace(' ', '')
Lines = Lines.replace('_', ' ')
Lines = Lines.lower().split('\n')
print(len(Lines))
from wordgenerator import *  
generate_wordcloud(Lines, 'wordcloud2021.png', '2021.png')
