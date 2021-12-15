file1 = open('./2021dataparse/data2022.txt', 'r')
Lines = file1.read()
Lines = Lines.replace(',', '\n')
Lines = Lines.replace('.', '')
Lines = Lines.replace('and', '')
Lines = Lines.replace(' ', '')
Lines = Lines.replace('_', ' ')
Lines = Lines.lower().split('\n')
print(Lines)

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os

def transform_format(val):
    if val == 0:
        return 255
    else:
        return val
mask = np.array(Image.open("2022.png"))
mask2 = mask.copy()
mask2[mask2.sum(axis=2) == 0] = 255
#print(mask2)

word_could_dict=Counter(Lines)

wordcloud = WordCloud( mask=mask2, font_path='Fontspring-DEMO-FoundationSans-BoldEx.otf',
                background_color ='white', contour_width=2, contour_color='rgb(58, 117, 180)').generate_from_frequencies(word_could_dict)
 
wordcloud.to_file("wordcloud2022.png")