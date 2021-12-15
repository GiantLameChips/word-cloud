file1 = open('./2021dataparse/data2021.txt', 'r')
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
import random
import string

def transform_format(val):
    if val == 0:
        return 255
    else:
        return val
mask = np.array(Image.open("2021.png"))
mask2 = mask.copy()
mask2[mask2.sum(axis=2) == 0] = 255
#print(mask2)

word_could_dict=Counter(Lines)
def grey_color_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    rgb= string.Template("rgb(58, 11$randint, 18$randint)")
    return rgb.substitute(randint=random.randint(0,9))
wordcloud = WordCloud( mask=mask2, font_path='Fontspring-DEMO-FoundationSans-BoldEx.otf',
                background_color ='white', contour_width=2, contour_color='rgb(58, 117, 180)').generate_from_frequencies(word_could_dict)
plt.title("Custom colors")
plt.imshow(wordcloud.recolor(color_func=grey_color_func, random_state=3),
           interpolation="bilinear")
wordcloud.to_file("wordcloud2021.png")