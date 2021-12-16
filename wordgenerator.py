def generate_wordcloud(words_string, to_file, mask_file, font):
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
    def grey_color_func(word, font_size, position, orientation, random_state=None,
                        **kwargs):
        rgb= string.Template("rgb(58, 1$randint2, 1$randint2)")
        colors = ['rgb(44, 178, 204)', 'rgb(58, 180, 175)', 'rgb(98, 179, 143)', 'rgb(212, 175, 55)', 'rgb(171, 181, 160)', 'rgb(147, 184, 191)']
        #return rgb.substitute(randint=random.randint(0,9), randint2=random.randint(0,99))
        return colors[random.randint(0,5)]
    def transform_format(val):
        if val == 0:
            return 255
        else:
            return val


    mask = np.array(Image.open(mask_file))
    
    mask2 = mask.copy()
    mask2[mask2.sum(axis=2) == 0] = 255


    word_could_dict=Counter(words_string)

    wordcloud = WordCloud( mask=mask2, font_path='Fontspring-DEMO-FoundationSans-BoldEx.otf',
                    background_color ='white', min_font_size=font ,contour_width=8, contour_color='rgb(212, 175, 55)').generate_from_frequencies(word_could_dict)
    plt.title("Custom colors")
    plt.imshow(wordcloud.recolor(color_func=grey_color_func, random_state=3),
               interpolation="bilinear")    
    wordcloud.to_file(to_file)
    del mask
    del mask2
    del plt
    del wordcloud