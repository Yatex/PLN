from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re

def wordcloud(stopwords, words):
    shortwords = re.compile(r'\b\w{1,3}\b')
    long_words = shortwords.sub('', words)
    wordcloud = WordCloud(width = 800, height = 800,
                    background_color ='white',
                    stopwords = stopwords,
                    min_font_size = 10).generate(long_words)
    
    # plot the WordCloud image                      
    plt.figure(figsize = (8, 8), facecolor = None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad = 0)
    
    plt.show()